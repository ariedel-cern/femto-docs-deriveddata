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
selection, with the bit position of each threshold so minimal cuts'
always-enforced floor (no bit) can be told apart from their selectable
tightenings (bit N).

Takes the same JSON config file as download_test_output.py, so that the
"title", general "comment", "production_train_id" and the test train it
was actually downloaded from (download_test_output.py records that
resolved id in SOURCE.json; see its docstring for how it's found) -- both
linked to their Hyperloop train-run overview pages -- the
"cutculator_input_link" (a link to an AnalysisResults.root from the
production train, for analysers to feed into cutculator.py themselves),
the "hyperloop_dataset_link" (the Hyperloop dataset for the derived data,
from operators) -- the latter two added by hand once available -- and any
per-species comments ("species_comments": {species name: comment}) make
it into the doc. A comment that is empty or whose key is missing is
simply skipped. The performance overview (not needed by analysers reading
the cuts) is rendered last, after all species.

Example:

    python3 generate_cuts_doc.py configs/LHC22o_pass7_minBias.json \\
        ./output/LHC22o_pass7_minBias

@author Anton Riedel <anton.riedel@cern.ch>, Technical University of Munich
"""

import argparse
import json
import os
import re

import ROOT  # pylint: disable=import-error

from hyperloop_common import human_bytes, human_seconds, train_run_url

VALUE_DELIM = "___"
SECTION_DELIM = ":::"

SPECIES_RE = re.compile(r"^h(.+?)(Filters|Selection)$")

# Documentation order: tracks, then the particle species roughly in order of
# decay-topology complexity; cascades (Xi, Omega) last. AntiLambda is
# excluded -- it is configured with the same cuts as Lambda.
SPECIES_ORDER = ["Collision", "Track", "K0short", "Lambda", "Sigma", "SigmaPlus", "Xi", "Omega", "Photon"]
EXCLUDED_SPECIES = {"AntiLambda"}


def parse_bin_label(label):
    result = {}
    for sec in label.split(SECTION_DELIM):
        if VALUE_DELIM not in sec:
            continue
        key, value = sec.split(VALUE_DELIM, 1)
        result[key] = value
    return result


def is_minimal_bin(b):
    return b.get("MinimalCut", "0") == "1" and b.get("OptionalCut", "0") == "0"


def bin_kind(b):
    if is_minimal_bin(b):
        return "minimal"
    if b.get("OptionalCut", "0") == "1":
        return "optional"
    return "neutral"


def humanize_comment(raw):
    """Translate known raw 'key = value; ...' comments -- the "gates that
    don't show up as bits" the userguide describes -- into a short, plain
    note. Unrecognized keys are passed through as-is."""
    if not raw or raw.upper() == "X":
        return ""

    parts = {}
    for p in raw.split(";"):
        if "=" in p:
            key, val = p.split("=", 1)
            parts[key.strip()] = val.strip()

    notes = []
    for key in [k for k in parts if k.lower().startswith("minmomtof")]:
        notes.append(f"TOF mandatory above {float(parts.pop(key)):g} GeV/c")

    if "requireTof" in parts and "keepTracksWithoutTof" in parts:
        require_tof = parts.pop("requireTof")
        keep_without_tof = parts.pop("keepTracksWithoutTof")
        if require_tof == "1":
            notes.append("TOF mandatory")
        elif keep_without_tof == "1":
            notes.append("passes if daughter has no TOF; else nSigmaTOF computed with corrected time")
        else:
            notes.append("rejected if daughter has no TOF; else nSigmaTOF computed with corrected time")

    notes.extend(f"{k} = {v}" for k, v in parts.items())
    return "; ".join(notes)


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


def md_cell(value):
    """Escape markdown table-cell-breaking characters. Selection names like
    'Max. |DCA_xy| ...' and function-valued cuts like '0.004+0.013*pow(x,-1)'
    can contain a literal '|', which an unescaped table reads as a new
    column."""
    return str(value).replace("|", "\\|")


def render_filters_table(bins):
    lines = ["| Filter | Value |", "| --- | --- |"]
    for b in bins:
        lines.append(f"| {md_cell(b.get('FilterName', 'unknown'))} | {md_cell(b.get('FilterValue', ''))} |")
    return "\n".join(lines)


def render_selection_table(bins):
    """One table for every selection of a species, in ascending bit order
    per selection. The Bit column distinguishes, for minimal cuts
    especially, the always-enforced floor (no bit, "always applied") from
    the selectable tightenings above it (bit N)."""
    groups = {}
    for b in bins:
        sel_name = b.get("SelectionName", "unknown")
        groups.setdefault(sel_name, []).append(b)

    def sort_key(b):
        pos = b.get("BitPosition", "X")
        return (0, -1) if pos.upper() == "X" else (1, int(pos))

    lines = ["| Selection | Bit | Type | Value | Comment |", "| --- | --- | --- | --- | --- |"]
    for sel_name, group in groups.items():
        for b in sorted(group, key=sort_key):
            pos = b.get("BitPosition", "X")
            bit_label = "always applied" if pos.upper() == "X" else pos
            comment = humanize_comment(b.get("Comment", ""))
            lines.append(f"| {md_cell(sel_name)} | {bit_label} | {bin_kind(b)} | {md_cell(b.get('Value', ''))} | {md_cell(comment)} |")
    return "\n".join(lines)


def humanize(species_name):
    # insert spaces before capitals that follow lowercase letters: "AntiLambda" -> "Anti Lambda"
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", species_name)


def render_species(name, hists_by_kind, tdir, comment=None):
    parts = [f"## {humanize(name)}"]

    if comment:
        parts.append(f"> {comment}")

    if "Filters" in hists_by_kind:
        bins = read_bins(tdir.Get(hists_by_kind["Filters"]))
        if bins:
            parts.append("### Prefilters")
            parts.append(render_filters_table(bins))

    if "Selection" in hists_by_kind:
        bins = read_bins(tdir.Get(hists_by_kind["Selection"]))
        if bins:
            parts.append("### Cuts")
            parts.append(render_selection_table(bins))

    return "\n\n".join(parts)


def render_header(outdir, doc_config):
    lines = [f"# {doc_config.get('title') or 'Configured cuts'}"]

    comment = doc_config.get("comment")
    if comment:
        lines.append(f"\n> {comment}")

    cutculator_link = doc_config.get("cutculator_input_link")
    if cutculator_link:
        lines.append(f"\n**AnalysisResults.root for cutculator.py:** [{cutculator_link}]({cutculator_link})")
    else:
        lines.append("\n**AnalysisResults.root for cutculator.py:** _pending -- added once the production train completes_")

    dataset_link = doc_config.get("hyperloop_dataset_link")
    if dataset_link:
        lines.append(f"\n**Hyperloop dataset:** [{dataset_link}]({dataset_link})")
    else:
        lines.append("\n**Hyperloop dataset:** _pending -- added once the derived data has been produced_")

    full_config_path = os.path.join(outdir, "full_config.json")
    source_path = os.path.join(outdir, "SOURCE.json")
    test_train_id = doc_config.get("test_train_id")
    if os.path.exists(source_path):
        with open(source_path) as f:
            # input_train_id is whatever download_test_output.py actually
            # pulled AnalysisResults.root from: the short/base train if the
            # production train is based on one, else the production train
            # itself -- resolved automatically via its short_train_id.
            test_train_id = json.load(f).get("input_train_id", test_train_id)
    production_train_id = doc_config.get("production_train_id")
    rows = []
    if os.path.exists(full_config_path):
        with open(full_config_path) as f:
            cfg = json.load(f)
        rows.append(f"| Software tag | {cfg.get('package_tag', '?')} |")
    if test_train_id:
        rows.append(f"| Test train | [{test_train_id}]({train_run_url(test_train_id)}) |")
    if production_train_id:
        rows.append(f"| Production train | [{production_train_id}]({train_run_url(production_train_id)}) |")
    else:
        rows.append("| Production train | _pending -- added once the production train is composed_ |")
    if rows:
        lines.append("")
        lines.append("| | |")
        lines.append("| --- | --- |")
        lines.extend(rows)

    return "\n".join(lines)


def render_performance_table(perf):
    lines = ["| | |", "| --- | --- |"]
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


def render_performance(outdir):
    """Rendered at the very end of the doc -- it's operational information
    about the test run, not something an analyser needs to read the cuts.
    Shows the projection from the (smaller) test train first, if there is
    one, then the production train's own numbers."""
    perf_path = os.path.join(outdir, "performance.json")
    if not os.path.exists(perf_path):
        return None

    with open(perf_path) as f:
        performance = json.load(f)

    sections = [
        "## Performance overview",
        "\"Expected\" rows extrapolate the measured ratios to the full dataset.",
    ]
    if performance.get("test"):
        sections.append("### Projected from test")
        sections.append(render_performance_table(performance["test"]))
    if performance.get("full_train"):
        sections.append("### Full train")
        sections.append(render_performance_table(performance["full_train"]))

    return "\n\n".join(sections)


def ordered_species_names(species):
    names = [n for n in species if n not in EXCLUDED_SPECIES]
    known = [n for n in SPECIES_ORDER if n in names]
    unknown = sorted(n for n in names if n not in SPECIES_ORDER)
    return known + unknown


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", help="JSON config file with comment/output_download_link (see configs/*.json)")
    parser.add_argument("outdir", help="Directory produced by download_test_output.py")
    parser.add_argument("--rootfile", default="AnalysisResults.root", help="ROOT file name inside outdir")
    parser.add_argument("--dir", default="femto-producer", help="TDirectory in the ROOT file to document")
    parser.add_argument("--output", default=None, help="Output markdown file (default: <outdir>/cuts.md)")
    args = parser.parse_args()

    with open(args.config) as f:
        doc_config = json.load(f)

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

    species_comments = doc_config.get("species_comments") or {}

    doc = [render_header(args.outdir, doc_config)]
    names = ordered_species_names(species)
    for name in names:
        doc.append(render_species(name, species[name], tdir, species_comments.get(name)))

    performance = render_performance(args.outdir)
    if performance:
        doc.append(performance)

    output_path = args.output or os.path.join(args.outdir, "cuts.md")
    with open(output_path, "w") as out:
        out.write("\n\n".join(doc) + "\n")

    print(f"Wrote {output_path} ({len(names)} species)")


if __name__ == "__main__":
    main()
