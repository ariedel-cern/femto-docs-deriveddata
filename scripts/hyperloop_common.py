#!/usr/bin/env python3

"""!
@brief  Shared helpers for talking to alimonitor.cern.ch (Hyperloop) from the
        command line: Hyperloop train-run/test-output URL builders, and a
        grid-cert-authenticated requests session.

@author Anton Riedel <anton.riedel@cern.ch>, Technical University of Munich
"""

import requests
import urllib3

TRAIN_WORKDIR_BASE = "https://alimonitor.cern.ch/train-workdir/tests"
API_BASE = "https://alimonitor.cern.ch/alihyperloop-data"
HYPERLOOP_BASE = "https://alimonitor.cern.ch/hyperloop"


def train_run_url(train_id):
    """The permanent Hyperloop overview page for a train run (unlike the
    cached test-output directory, this isn't cleaned up)."""
    return f"{HYPERLOOP_BASE}/train-run/{train_id}/general"


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
