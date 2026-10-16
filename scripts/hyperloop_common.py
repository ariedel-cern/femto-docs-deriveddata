#!/usr/bin/env python3

"""!
@brief  Shared helpers for talking to alimonitor.cern.ch (Hyperloop) from the
        command line: resolving a train/test id, building the cached test
        output directory URL, and a grid-cert-authenticated requests session.

@author Anton Riedel <anton.riedel@cern.ch>, Technical University of Munich
"""

import re

import requests
import urllib3

TRAIN_WORKDIR_BASE = "https://alimonitor.cern.ch/train-workdir/tests"
API_BASE = "https://alimonitor.cern.ch/alihyperloop-data"
HYPERLOOP_BASE = "https://alimonitor.cern.ch/hyperloop"


def train_run_url(train_id):
    """The permanent Hyperloop overview page for a train run (unlike the
    cached test-output directory, this isn't cleaned up)."""
    return f"{HYPERLOOP_BASE}/train-run/{train_id}/general"


def parse_train_or_test_id(url_or_id):
    """Accept a bare train/test id, or any Hyperloop train-run/wagon-test
    URL (general overview, test/full, test/quick, ...), and return
    (id, kind) where kind is "train" (a whole composed train, identified by
    train_id) or "wagon" (a single wagon's quick test, identified by its own
    test_id)."""
    s = str(url_or_id).strip()
    if s.isdigit():
        return int(s), "train"
    m = re.search(r"/train-run/(\d+)", s)
    if m:
        return int(m.group(1)), "train"
    m = re.search(r"/wagon-test/(\d+)", s)
    if m:
        return int(m.group(1)), "wagon"
    digit_runs = re.findall(r"\d+", s)
    if digit_runs:
        return int(digit_runs[-1]), "train"
    raise ValueError(f"Could not find a numeric train/test id in: {url_or_id}")


def test_directory_url(test_id):
    """The cached, plain-HTTPS directory Hyperloop serves a test's merged
    output from (AnalysisResults.root, AO2D.root, configs, logs, ...)."""
    padded = f"{test_id:08d}"
    return f"{TRAIN_WORKDIR_BASE}/{padded[:4]}/{padded}/"


def make_session(cert, key):
    session = requests.Session()
    session.cert = (cert, key)
    # CERN's grid CA chain is not in standard OS trust stores; this is the
    # same trust model alien_cp / TGrid use under the hood.
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    return session


def human_bytes(n):
    if n is None:
        return "?"
    n = float(n)
    sign = "-" if n < 0 else ""
    n = abs(n)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if n < 1024:
            return f"{sign}{n:.1f} {unit}"
        n /= 1024
    return f"{sign}{n:.1f} EB"


def human_seconds(n):
    if n is None:
        return "?"
    n = float(n)
    units = (("d", 86400), ("h", 3600), ("m", 60), ("s", 1))
    parts = []
    for name, size in units:
        if n >= size:
            value = int(n // size)
            n -= value * size
            parts.append(f"{value}{name}")
    return " ".join(parts) if parts else "0s"
