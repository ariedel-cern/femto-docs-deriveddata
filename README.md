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
  "title": "doc title (H1); falls back to \"Configured cuts\"",
  "comment": "free text, for humans reading the config",
  "production_train_id": 778977,
  "cutculator_input_link": null,
  "hyperloop_dataset_link": null,
  "species_comments": {
    "Track": "optional, rendered under that species' heading"
  }
}
```

`production_train_id` -- the train composed on the full dataset -- is the
only train id you need to give it. Some production trains are composed
from ("based on") a smaller validation train run first; `download_test_output.py`
checks the production train's own Hyperloop metadata for a `short_train_id`
and, if there is one, downloads `AnalysisResults.root` from that smaller
train instead (this is what the Hyperloop train-run page shows as the
train it's "based on"). If there's no base train, it just uses the
production train's own test output. Either way, both trains end up linked
in the doc from their permanent Hyperloop overview pages -- no need to
look up or specify the base train id by hand. (An explicit `test_train_id`
field still overrides this auto-lookup, if you ever need it to.)

`cutculator_input_link` points at an `AnalysisResults.root` from the
production train, for analysers to feed into `cutculator.py` themselves.
`hyperloop_dataset_link` points at the Hyperloop dataset for the derived
data. Both are filled in by hand once available -- the first once the
production train has run, the second once operators hand over the dataset
link after the derived data has been produced -- and until then stay
`null`, showing a placeholder. `comment` and any entry in
`species_comments` are skipped if empty or missing.

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
#    cuts as Lambda), links/comment/software-tag as a header, and the
#    performance overview at the very end (analysers don't need it).
python3 scripts/generate_cuts_doc.py \
    configs/LHC22o_pass7_minBias.json ./output/LHC22o_pass7_minBias
```

This reuses the same bin-label format that `cutculator.py`
(`O2Physics/PWGCF/Femto/Macros/`) parses interactively, but lists every
configured threshold per selection, with its bit position, rather than
asking the user to pick one. `generate_cuts_doc.py` needs a PyROOT-enabled
environment (e.g. an alienv O2Physics env); `download_test_output.py` only
needs `requests`.

## Status

Cuts-listing pipeline (`scripts/`) in place. Still to do: hand-written prose
around table schemas, column meanings, and versioning policy — see
`femto-docs-userguide` for the first deck.
