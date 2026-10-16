#!/usr/bin/env python3

"""!
@brief  Download the output of a Hyperloop train test (full or quick) so that
        generate_cuts_doc.py can turn it into derived-data documentation.

Takes a small JSON config file (see configs/*.json for an example) with at
least a "train_id" field. It resolves the rest itself: calls the Hyperloop
API for the train's "full" test metadata (performance overview: reduction
factor, PSS memory, throughput, expected resources for the full run), and
downloads the test's cached output -- AnalysisResults.root,
configuration.json, etc. -- from the plain HTTPS directory Hyperloop serves
it from:

    https://alimonitor.cern.ch/train-workdir/tests/<id[:4]>/<id>/

Both the API and the directory require your personal grid certificate as a
TLS client cert -- the same usercert.pem/userkey.pem used for alien://
access.

Config file fields:
    comment              free text, for humans reading the config
    train_id             the Hyperloop train number (required)
    output_download_link link to the final merged production output, filled
                          in by hand once the real (non-test) train has run;
                          leave null/empty until then -- generate_cuts_doc.py
                          renders a placeholder in its place

Example:

    python3 download_test_output.py configs/LHC22o_pass7_minBias.json \\
        ./output/LHC22o_pass7_minBias

@author Anton Riedel <anton.riedel@cern.ch>, Technical University of Munich
"""

import argparse
import json
import os
import sys

from hyperloop_common import (
    API_BASE,
    human_bytes,
    human_seconds,
    make_session,
    parse_train_or_test_id,
    test_directory_url,
)

# Always small and always useful for documentation / provenance.
DEFAULT_FILES = [
    "AnalysisResults.root",
    "configuration.json",
    "dpl-config.json",
    "full_config.json",
    "OutputDirector.json",
    "status.json",
    "stdout.log",
    "stderr.log",
]

AOD_FILE = "AO2D.root"


def fetch_metadata(session, test_id, kind):
    """Pull the same JSON the Hyperloop train-run/general and wagon-test
    pages are built from, so we get the performance overview numbers
    without having to scrape HTML."""
    if kind == "train":
        resp = session.get(f"{API_BASE}/trains/train.jsp", params={"train_id": test_id, "type": "full"}, timeout=60)
    else:
        resp = session.get(f"{API_BASE}/trains/test-result.jsp", params={"test_id": test_id}, timeout=60)
    if resp.status_code != 200:
        print(f"  warning: could not fetch test metadata (HTTP {resp.status_code})")
        return None
    try:
        return resp.json()
    except ValueError:
        print("  warning: test metadata response was not JSON")
        return None


def compute_performance(meta):
    """Reconstruct the "performance overview" numbers Hyperloop shows for a
    test: reduction factor, PSS memory, throughput, and the resources/output
    size expected if the same ratios hold for the full dataset.

    - reduction factor: input size / AO2D output size of *this test*.
    - throughput: input size / wall time / cpu cores (this test).
    - expected resources: extrapolating this test's throughput to the full
      dataset size gives the core-seconds the full train run would need.
    - expected output size: extrapolating this test's reduction factor to
      the full dataset size gives the projected total AO2D size.
    """
    input_size = meta.get("input_size")
    output_size = meta.get("output_size")
    derived_output_size = meta.get("derived_output_size") or output_size
    wall_time = meta.get("wall_time")
    cpu_cores = meta.get("cpu_cores") or 1
    dataset_size = meta.get("dataset_size_with_parents") or meta.get("dataset_size")

    perf = {
        "mem_pss_avg_bytes": meta.get("mem_pss"),
        "mem_pss_max_bytes": meta.get("mem_pss_max"),
    }

    reduction_factor = None
    if input_size and derived_output_size:
        reduction_factor = input_size / derived_output_size
        perf["reduction_factor"] = reduction_factor

    if input_size and wall_time:
        perf["throughput_bytes_per_sec_per_core"] = input_size / wall_time / cpu_cores

    if dataset_size and reduction_factor:
        perf["expected_output_size_bytes"] = dataset_size / reduction_factor

    if dataset_size and input_size and wall_time:
        perf["expected_resources_core_seconds"] = dataset_size * wall_time * cpu_cores / input_size

    perf["_raw"] = {
        k: meta.get(k)
        for k in (
            "input_size", "output_size", "derived_output_size", "wall_time", "cpu_time",
            "cpu_cores", "dataset_size", "dataset_size_with_parents", "dataset_size_without_parents",
            "mem_pss", "mem_pss_max", "package_tag", "dataset_name",
        )
    }
    return perf


def print_performance(perf):
    print("\nPerformance overview (of this test, extrapolated where noted):")
    if "reduction_factor" in perf:
        print(f"  Reduction factor:   {perf['reduction_factor']:.1f}x")
    if "mem_pss_avg_bytes" in perf and perf["mem_pss_avg_bytes"] is not None:
        print(f"  PSS memory:         avg {human_bytes(perf['mem_pss_avg_bytes'])}, max {human_bytes(perf.get('mem_pss_max_bytes'))}")
    if "throughput_bytes_per_sec_per_core" in perf:
        print(f"  Throughput:         {human_bytes(perf['throughput_bytes_per_sec_per_core'])}/s per core")
    if "expected_resources_core_seconds" in perf:
        print(f"  Expected resources: {human_seconds(perf['expected_resources_core_seconds'])} (core-time) for the full run")
    if "expected_output_size_bytes" in perf:
        print(f"  Expected output:    {human_bytes(perf['expected_output_size_bytes'])} for the full run")


def download_file(session, base_url, filename, outdir):
    url = base_url + filename
    dest = os.path.join(outdir, filename)
    resp = session.get(url, stream=True, timeout=120)
    if resp.status_code != 200:
        print(f"  skip {filename}: HTTP {resp.status_code}")
        return False
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1 << 20):
            f.write(chunk)
    size = os.path.getsize(dest)
    print(f"  {filename} ({size/1024:.1f} kB)")
    return True


def load_config(config_path):
    with open(config_path) as f:
        cfg = json.load(f)
    if not cfg.get("train_id"):
        raise SystemExit(f"{config_path}: missing required field 'train_id'")
    return cfg


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", help="JSON config file with at least a train_id field (see configs/*.json)")
    parser.add_argument("outdir", help="Directory to download into (created if missing)")
    parser.add_argument("--cert", default=os.path.expanduser("~/.globus/usercert.pem"), help="Grid certificate (default: ~/.globus/usercert.pem)")
    parser.add_argument("--key", default=os.path.expanduser("~/.globus/userkey.pem"), help="Grid certificate key (default: ~/.globus/userkey.pem)")
    parser.add_argument("--with-aod", action="store_true", help=f"Also download {AOD_FILE} (tens of MB)")
    parser.add_argument("--only", nargs="+", default=None, help="Download only these filenames instead of the default set")
    args = parser.parse_args()

    if not os.path.exists(args.cert) or not os.path.exists(args.key):
        sys.exit(f"Grid certificate not found: {args.cert} / {args.key}\n"
                  f"Pass --cert/--key if your certificate lives elsewhere.")

    cfg = load_config(args.config)
    test_id, kind = parse_train_or_test_id(str(cfg["train_id"]))
    base_url = test_directory_url(test_id)
    os.makedirs(args.outdir, exist_ok=True)

    print(f"Resolved {kind} id {test_id} -> {base_url}")

    session = make_session(args.cert, args.key)

    meta = fetch_metadata(session, test_id, kind)
    perf = None
    if meta:
        meta_name = "train_meta.json" if kind == "train" else "test_meta.json"
        with open(os.path.join(args.outdir, meta_name), "w") as f:
            json.dump(meta, f, indent=2)
        perf = compute_performance(meta)
        with open(os.path.join(args.outdir, "performance.json"), "w") as f:
            json.dump(perf, f, indent=2)
        print_performance(perf)

    files = args.only if args.only else list(DEFAULT_FILES)
    if args.with_aod and AOD_FILE not in files:
        files.append(AOD_FILE)

    print()
    downloaded = []
    for filename in files:
        if download_file(session, base_url, filename, args.outdir):
            downloaded.append(filename)

    if "AnalysisResults.root" not in downloaded:
        print("\nWarning: AnalysisResults.root was not downloaded -- "
              "generate_cuts_doc.py needs it.")

    provenance = {
        "config_file": args.config,
        "resolved_id": test_id,
        "resolved_kind": kind,
        "resolved_directory": base_url,
        "downloaded_files": downloaded,
    }
    with open(os.path.join(args.outdir, "SOURCE.json"), "w") as f:
        json.dump(provenance, f, indent=2)

    print(f"\nSaved to {args.outdir}/ (see SOURCE.json for provenance)")


if __name__ == "__main__":
    main()
