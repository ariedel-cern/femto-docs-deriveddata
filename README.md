# Femto Framework — Derived Data Documentation

Documentation of the derived data produced by the PWGCF/Femto analysis framework
(O2Physics): table schemas, column meanings, bitmask layouts, and versioning policy.
One of three sibling repos:

- `femto-docs-code` — code-level documentation (architecture, class reference)
- `femto-docs-userguide` — how to configure and run the framework
- `femto-docs-deriveddata` — **this repo**: the derived data format

## Generating a production's cuts documentation

`scripts/` contains a two-step pipeline that turns a Hyperloop train test into
a markdown document listing every configured cut. Each production gets a
small JSON config in `configs/` (see `configs/LHC22o_pass7_minBias.json`):

```json
{
  "comment": "free text, for humans reading the config",
  "train_id": 778977,
  "output_download_link": null,
  "species_comments": {
    "Track": "optional, rendered under that species' heading"
  }
}
```

`output_download_link` is filled in by hand once the real (non-test)
production train has finished and the merged derived data has somewhere to
be downloaded from; until then it stays `null` and the doc shows a
placeholder. Both `comment` and any entry in `species_comments` are skipped
entirely in the doc if empty or missing.

```bash
# 1. resolves the train's "full" test itself, pulls the performance overview
#    (reduction factor, PSS memory, throughput, expected resources for the
#    full run), and downloads AnalysisResults.root + config files. Needs
#    your grid cert, default ~/.globus/user{cert,key}.pem.
python3 scripts/download_test_output.py \
    configs/LHC22o_pass7_minBias.json ./output/LHC22o_pass7_minBias

# 2. turn AnalysisResults.root's self-documenting histogram bin labels into
#    a markdown doc: one merged cuts table per particle species (tracks,
#    K0short, Lambda, Sigma(+), Xi, Omega, ...; AntiLambda is skipped, same
#    cuts as Lambda), with the performance overview and config comment/link
#    as a header.
python3 scripts/generate_cuts_doc.py \
    configs/LHC22o_pass7_minBias.json ./output/LHC22o_pass7_minBias
```

This reuses the same bin-label format that `cutculator.py`
(`O2Physics/PWGCF/Femto/Macros/`) parses interactively, but lists every
configured threshold per selection rather than asking the user to pick one
(bit positions are left out of the table -- they're just the row order
within each selection). `generate_cuts_doc.py` needs a PyROOT-enabled
environment (e.g. an alienv O2Physics env); `download_test_output.py` only
needs `requests`.

## Status

Cuts-listing pipeline (`scripts/`) in place. Still to do: hand-written prose
around table schemas, column meanings, and versioning policy — see
`femto-docs-userguide` for the first deck.
