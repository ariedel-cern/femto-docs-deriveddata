#!/usr/bin/env python3

"""!
@brief  Turn the AnalysisResults.root of a Femto producer test (downloaded
        with download_test_output.py) into a markdown document listing every
        configured cut, per particle species.

This reads the same self-documenting bin labels that cutculator.py uses
interactively (SelectionName/FilterName/BitPosition/.../Comment, parsed with
the "___"/":::" delimiters), but instead of asking the user to pick one
threshold per selection, it lists every configured threshold -- i.e. the
full menu a downstream analysis can choose from -- grouped by species and
selection.

Example:

    python3 generate_cuts_doc.py ./train_778977 --output cuts.md

@author Anton Riedel <anton.riedel@cern.ch>, Technical University of Munich
"""

import argparse
import json
import os
import re

import ROOT  # pylint: disable=import-error

from hyperloop_common import human_bytes, human_seconds

VALUE_DELIM = "___"
SECTION_DELIM = ":::"

SPECIES_RE = re.compile(r"^h(.+?)(Filters|Selection)$")


def parse_bin_label(label):
    result = {}
    for sec in label.split(SECTION_DELIM):
        if VALUE_DELIM not in sec:
            continue
        key, value = sec.split(VALUE_DELIM, 1)
        result[key] = value
    return result


def format_value_with_comment(b):
    val = b.get("Value", "")
    comment = b.get("Comment", "")
    if comment and comment.upper() != "X":
        return f"{val} (comment={comment})"
    return val


def is_minimal_bin(b):
    return b.get("MinimalCut", "0") == "1" and b.get("OptionalCut", "0") == "0"


def bin_kind(b):
    if is_minimal_bin(b):
        return "minimal"
    if b.get("OptionalCut", "0") == "1":
        return "optional"
    return "neutral"


def read_bins(hist):
    """Parse all bins of a histogram, dropping the two trailing
    'All analyzed'/'All passed' bins present on every histogram."""
    nbins = hist.GetNbinsX()
    bins = []
    for i in range(1, nbins - 2 + 1):
        label = hist.GetXaxis().GetBinLabel(i)
        if not label:
            continue
        bdict = parse_bin_label(label)
        if bdict:
            bins.append(bdict)
    return bins


def discover_species(tdir):
    """Group hXFilters/hXSelection histogram names by species name X."""
    species = {}
    for key in tdir.GetListOfKeys():
        m = SPECIES_RE.match(key.GetName())
        if not m:
            continue
        name, kind = m.group(1), m.group(2)
        species.setdefault(name, {})[kind] = key.GetName()
    return species


def render_filters_table(bins):
    lines = ["| Filter | Value |", "| --- | --- |"]
    for b in bins:
        lines.append(f"| {b.get('FilterName', 'unknown')} | {b.get('FilterValue', '')} |")
    return "\n".join(lines)


def render_selection_tables(bins):
    groups = {}
    for b in bins:
        sel_name = b.get("SelectionName", "unknown")
        groups.setdefault(sel_name, []).append(b)

    sections = []
    for sel_name, group in groups.items():
        lines = [f"**{sel_name}**", "", "| Bit | Type | Value | Comment |", "| --- | --- | --- | --- |"]

        def sort_key(b):
            pos = b.get("BitPosition", "X")
            return (0, -1) if pos.upper() == "X" else (1, int(pos))

        for b in sorted(group, key=sort_key):
            pos = b.get("BitPosition", "X")
            bit_label = "always applied" if pos.upper() == "X" else pos
            comment = b.get("Comment", "")
            comment = "" if comment.upper() == "X" else comment
            lines.append(f"| {bit_label} | {bin_kind(b)} | {b.get('Value', '')} | {comment} |")
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def humanize(species_name):
    # insert spaces before capitals that follow lowercase letters: "AntiLambda" -> "Anti Lambda"
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", species_name)


def render_species(name, hists_by_kind, tdir):
    parts = [f"## {humanize(name)}"]

    if "Filters" in hists_by_kind:
        bins = read_bins(tdir.Get(hists_by_kind["Filters"]))
        if bins:
            parts.append("### Prefilters")
            parts.append(render_filters_table(bins))

    if "Selection" in hists_by_kind:
        bins = read_bins(tdir.Get(hists_by_kind["Selection"]))
        if bins:
            parts.append("### Cuts")
            parts.append(render_selection_tables(bins))

    return "\n\n".join(parts)


def render_header(outdir):
    lines = ["# Configured cuts"]
    source_path = os.path.join(outdir, "SOURCE.json")
    config_path = os.path.join(outdir, "full_config.json")

    if os.path.exists(source_path):
        with open(source_path) as f:
            source = json.load(f)
        url = source["source_url"]
        shown = f"[{url}]({url})" if url.startswith("http") else url
        lines.append(f"\nSource: {shown} (resolved {source['resolved_kind']} id {source['resolved_id']}, "
                     f"[test output]({source['resolved_directory']}))")

    if os.path.exists(config_path):
        with open(config_path) as f:
            cfg = json.load(f)
        lines.append("")
        lines.append("| | |")
        lines.append("| --- | --- |")
        lines.append(f"| Package tag | {cfg.get('package_tag', '?')} |")
        lines.append(f"| Production type | {cfg.get('dataset_production_type', '?')} |")
        inputdata = cfg.get("inputdata") or []
        if inputdata:
            lines.append(f"| Input data | {inputdata[0]}{' + ' + str(len(inputdata) - 1) + ' more' if len(inputdata) > 1 else ''} |")

    perf_path = os.path.join(outdir, "performance.json")
    if os.path.exists(perf_path):
        with open(perf_path) as f:
            perf = json.load(f)
        lines.append("")
        lines.append("## Performance overview")
        lines.append("")
        lines.append("Measured on this test; \"expected\" rows extrapolate this test's ratios to the full dataset.")
        lines.append("")
        lines.append("| | |")
        lines.append("| --- | --- |")
        if "reduction_factor" in perf:
            lines.append(f"| Reduction factor | {perf['reduction_factor']:.1f}x |")
        if perf.get("mem_pss_avg_bytes") is not None:
            lines.append(f"| PSS memory | avg {human_bytes(perf['mem_pss_avg_bytes'])}, max {human_bytes(perf.get('mem_pss_max_bytes'))} |")
        if "throughput_bytes_per_sec_per_core" in perf:
            lines.append(f"| Throughput | {human_bytes(perf['throughput_bytes_per_sec_per_core'])}/s per core |")
        if "expected_resources_core_seconds" in perf:
            lines.append(f"| Expected resources (full run) | {human_seconds(perf['expected_resources_core_seconds'])} core-time |")
        if "expected_output_size_bytes" in perf:
            lines.append(f"| Expected output size (full run) | {human_bytes(perf['expected_output_size_bytes'])} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("outdir", help="Directory produced by download_test_output.py")
    parser.add_argument("--rootfile", default="AnalysisResults.root", help="ROOT file name inside outdir")
    parser.add_argument("--dir", default="femto-producer", help="TDirectory in the ROOT file to document")
    parser.add_argument("--output", default=None, help="Output markdown file (default: <outdir>/cuts.md)")
    args = parser.parse_args()

    rootfile_path = os.path.join(args.outdir, args.rootfile)
    f = ROOT.TFile.Open(rootfile_path)
    if not f or f.IsZombie():
        raise SystemExit(f"Cannot open ROOT file: {rootfile_path}")

    tdir = f.Get(args.dir)
    if not tdir:
        raise SystemExit(f"Cannot find directory '{args.dir}' in {rootfile_path}")

    species = discover_species(tdir)
    if not species:
        raise SystemExit(f"No h<Species>Filters/h<Species>Selection histograms found in '{args.dir}'")

    doc = [render_header(args.outdir)]
    for name in sorted(species):
        doc.append(render_species(name, species[name], tdir))

    output_path = args.output or os.path.join(args.outdir, "cuts.md")
    with open(output_path, "w") as out:
        out.write("\n\n".join(doc) + "\n")

    print(f"Wrote {output_path} ({len(species)} species)")


if __name__ == "__main__":
    main()
