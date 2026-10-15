# Femto Framework — Derived Data Documentation

Documentation of the derived data produced by the PWGCF/Femto analysis framework
(O2Physics): table schemas, column meanings, bitmask layouts, and versioning policy.
One of three sibling repos:

- `femto-docs-code` — code-level documentation (architecture, class reference)
- `femto-docs-userguide` — how to configure and run the framework
- `femto-docs-deriveddata` — **this repo**: the derived data format

## Generating a production's cuts documentation

`scripts/` contains a two-step pipeline that turns a Hyperloop train test into
a markdown document listing every configured cut:

```bash
# 1. just the train number is enough -- it resolves the train's "full" test
#    itself, pulls the performance overview (reduction factor, PSS memory,
#    throughput, expected resources for the full run), and downloads
#    AnalysisResults.root + config files. Needs your grid cert, default
#    ~/.globus/user{cert,key}.pem. A train-run/wagon-test URL also works.
python3 scripts/download_test_output.py 778977 ./output/778977

# 2. turn AnalysisResults.root's self-documenting histogram bin labels into
#    a markdown doc, one section per particle species, with the performance
#    overview as a header
python3 scripts/generate_cuts_doc.py ./output/778977
```

This reuses the same bin-label format that `cutculator.py`
(`O2Physics/PWGCF/Femto/Macros/`) parses interactively, but lists every
configured threshold per selection rather than asking the user to pick one.
`generate_cuts_doc.py` needs a PyROOT-enabled environment (e.g. an alienv
O2Physics env); `download_test_output.py` only needs `requests`.

## Status

Cuts-listing pipeline (`scripts/`) in place. Still to do: hand-written prose
around table schemas, column meanings, and versioning policy — see
`femto-docs-userguide` for the first deck.
