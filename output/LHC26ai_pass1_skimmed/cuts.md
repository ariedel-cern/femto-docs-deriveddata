# CF_LHC26ai_pass1_skimmed_Femto_GP

> Activated triggers: rho-d, phi-d, p-p-rho, p-p-phi, p-p-L, p-L-L, L-L-L, etaPrime-d, omega-d, etaPrime-d, omega-p

**AnalysisResults.root for cutculator.py:** [https://alimonitor.cern.ch/catalogue/?path=/alice/cern.ch/user/a/alihyperloop/jobs/0660/hy_6607057/AOD#/alice/cern.ch/user/a/alihyperloop/jobs/0660/hy_6607057/AOD](https://alimonitor.cern.ch/catalogue/?path=/alice/cern.ch/user/a/alihyperloop/jobs/0660/hy_6607057/AOD#/alice/cern.ch/user/a/alihyperloop/jobs/0660/hy_6607057/AOD)

**Hyperloop dataset:** [https://alimonitor.cern.ch/hyperloop/view-dataset/3812](https://alimonitor.cern.ch/hyperloop/view-dataset/3812)

| | |
| --- | --- |
| Software tag | VO_ALICE@O2Physics::daily-20261116-0000-1 |
| Test train | [806592](https://alimonitor.cern.ch/hyperloop/train-run/806592/general) |
| Production train | [806592](https://alimonitor.cern.ch/hyperloop/train-run/806592/general) |

## Collision

> RCT flags are checked implicitly and Sel8 is an optional cut. Please make sure to check that NOT using Sel8 does not change your physics signal.

### Prefilters

| Filter | Value |
| --- | --- |
| vtxZMin | -10 |
| vtxZMax | 10 |
| multMin | 0 |
| multMax | 9999 |
| centMin | 0 |
| centMax | 999 |
| magFieldMin | -10 |
| magFieldMax | 10 |
| sphericityMin | 0 |
| sphericityMax | 2 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Sel8 | always applied | minimal | 1.000000 |  |
| RCT flags ok | always applied | minimal | 1.000000 | label = CBT_hadronPID; useZdc = 0; treatLimitedAcceptanceAsBad = 0 |
| No same bunch pileup | 0 | optional | 1.000000 |  |
| Is good zvtx FT0 vs PV | 1 | optional | 1.000000 |  |
| Minimum Sphericity | always applied | minimal | 0.000000 |  |
| Triggers | 2 | optional | 1.000000 |  |
| Triggers | 3 | optional | 1.000000 |  |
| Triggers | 4 | optional | 1.000000 |  |
| Triggers | 5 | optional | 1.000000 |  |
| Triggers | 6 | optional | 1.000000 |  |
| Triggers | 7 | optional | 1.000000 |  |
| Triggers | 8 | optional | 1.000000 |  |
| Triggers | 9 | optional | 1.000000 |  |
| Triggers | 10 | optional | 1.000000 |  |
| Triggers | 11 | optional | 1.000000 |  |
| Triggers | 12 | optional | 1.000000 |  |
| Triggers | 13 | optional | 1.000000 |  |

## Track

> Lower pT cut in prefilter of 0.136 necessary for ordering of DCA cuts.

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0.136 |
| ptMax | 6 |
| etaMin | -0.83 |
| etaMax | 0.83 |
| phiMin | 0 |
| phiMax | 6.28319 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. number of TPC clusters | always applied | minimal | 90.000000 |  |
| Min. number of TPC clusters | 0 | minimal | 100.000000 |  |
| Min. number of TPC clusters | 1 | minimal | 110.000000 |  |
| Min. number of TPC clusters | 2 | minimal | 120.000000 |  |
| Min. number of crossed TPC rows | always applied | minimal | 80.000000 |  |
| Min. number of crossed TPC rows | 3 | minimal | 90.000000 |  |
| Min. number of crossed TPC rows | 4 | minimal | 100.000000 |  |
| Min. number of crossed TPC rows | 5 | minimal | 110.000000 |  |
| Min. fraction of TPC clusters over TPC crossed rows | always applied | minimal | 0.000000 |  |
| Max. number of shared TPC clusters | always applied | minimal | 160.000000 |  |
| Max. fractions of shared TPC clusters | always applied | minimal | 1.000000 |  |
| Max. fractions of shared TPC clusters | 6 | minimal | 0.800000 |  |
| Max. fractions of shared TPC clusters | 7 | minimal | 0.400000 |  |
| Min. number of ITS clusters | always applied | minimal | 5.000000 |  |
| Min. number of ITS clusters | 8 | minimal | 6.000000 |  |
| Min. number of ITS clusters | 9 | minimal | 7.000000 |  |
| Min. number of ITS clusters in the inner barrel | always applied | minimal | 1.000000 |  |
| Min. number of ITS clusters in the inner barrel | 10 | minimal | 3.000000 |  |
| Max. \|DCA_xy\| (cm) as a function of pT | always applied | minimal | 0.1 |  |
| Max. \|DCA_xy\| (cm) as a function of pT | 11 | minimal | 0.004+0.013*pow(x,-1) |  |
| Max. \|DCA_z\| (cm) as a function of pT | always applied | minimal | 0.2 |  |
| Max. \|DCA_z\| (cm) as a function of pT | 12 | minimal | 0.004+0.013*pow(x,-1) |  |
| TPC Pion PID | 13 | optional | -3.5;3.5 |  |
| TPC Pion PID | 14 | optional | -3;3 |  |
| TPC Pion PID | 15 | optional | -2.5;2.5 |  |
| TPC Kaon PID | 16 | optional | -3.5;3.5 |  |
| TPC Kaon PID | 17 | optional | -3;3 |  |
| TPC Kaon PID | 18 | optional | -2.5;2.5 |  |
| TPC Proton PID | 19 | optional | -3.5;3.5 |  |
| TPC Proton PID | 20 | optional | -3;3 |  |
| TPC Proton PID | 21 | optional | -2.5;2.5 |  |
| TPC+ITS Pion PID | 22 | optional | 3.500000 |  |
| TPC+ITS Pion PID | 23 | optional | 3.000000 |  |
| TPC+ITS Pion PID | 24 | optional | 2.500000 |  |
| TPC+ITS Kaon PID | 25 | optional | 3.500000 |  |
| TPC+ITS Kaon PID | 26 | optional | 3.000000 |  |
| TPC+ITS Kaon PID | 27 | optional | 2.500000 |  |
| TPC+ITS Proton PID | 28 | optional | 3.500000 |  |
| TPC+ITS Proton PID | 29 | optional | 3.000000 |  |
| TPC+ITS Proton PID | 30 | optional | 2.500000 |  |
| TPC+ITS Deuteron PID | 31 | optional | 3.500000 |  |
| TPC+ITS Deuteron PID | 32 | optional | 3.000000 |  |
| TPC+ITS Deuteron PID | 33 | optional | 2.500000 |  |
| TPC+ITS He3 PID | 34 | optional | 3.500000 |  |
| TPC+ITS He3 PID | 35 | optional | 3.000000 |  |
| TPC+ITS He3 PID | 36 | optional | 2.500000 |  |
| TPC+TOF Pion PID | 37 | optional | 3.500000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Pion PID | 38 | optional | 3.000000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Pion PID | 39 | optional | 2.500000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Kaon PID | 40 | optional | 3.500000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Kaon PID | 41 | optional | 3.000000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Kaon PID | 42 | optional | 2.500000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Proton PID | 43 | optional | 3.500000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Proton PID | 44 | optional | 3.000000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Proton PID | 45 | optional | 2.500000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Deuteron PID | 46 | optional | 3.500000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF Deuteron PID | 47 | optional | 3.000000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF Deuteron PID | 48 | optional | 2.500000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF He3 PID | 49 | optional | 3.500000 | TOF mandatory above 1.6 GeV/c |
| TPC+TOF He3 PID | 50 | optional | 3.000000 | TOF mandatory above 1.6 GeV/c |
| TPC+TOF He3 PID | 51 | optional | 2.500000 | TOF mandatory above 1.6 GeV/c |

## Lambda

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| massMin | 1 |
| massMax | 1.15 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | always applied | minimal | 0.988000 |  |
| Min. CPA (cosine pointing angle) | 0 | minimal | 0.990000 |  |
| Min. CPA (cosine pointing angle) | 1 | minimal | 0.992000 |  |
| Max. DCA of the daughters at decay vertex | always applied | minimal | 1.500000 |  |
| Max. DCA of the daughters at decay vertex | 2 | minimal | 1.200000 |  |
| Max. distance of decay vertex in x,y,z | always applied | minimal | 100.000000 |  |
| Min. transverse radius | always applied | minimal | 0.200000 |  |
| Min. transverse radius | 3 | minimal | 0.300000 |  |
| Max. transverse radius | always applied | minimal | 100.000000 |  |
| Max. absolute pseudo rapidity of daughters | always applied | minimal | 0.830000 |  |
| Max. absolute pseudo rapidity of daughters | 4 | minimal | 0.800000 |  |
| Max. absolute pseudo rapidity of daughters | 5 | minimal | 0.770000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | always applied | minimal | 0.050000 |  |
| Min. number of TPC clusters of daughters | always applied | minimal | 70.000000 |  |
| Min. number of TPC clusters of daughters | 6 | minimal | 80.000000 |  |
| Min. number of TPC clusters of daughters | 7 | minimal | 90.000000 |  |
| TPC Proton PID for positive daughter | always applied | minimal | 5.000000 |  |
| TPC Proton PID for positive daughter | 8 | minimal | 4.000000 |  |
| TPC Pion PID for negative daughter | always applied | minimal | 5.000000 |  |
| TPC Pion PID for negative daughter | 9 | minimal | 4.000000 |  |
| Reject K0short mass hypothesis | always applied | minimal | 0.475;0.515 |  |

## Xi

> No Omega rejection.

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| massMin | 1.282 |
| massMax | 1.362 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Cascade CPA Min | always applied | minimal | 0.95 |  |
| Cascade DCA Daughters Max | always applied | minimal | 0.300000 |  |
| Cascade DCA Daughters Max | 0 | minimal | 0.250000 |  |
| Cascade Transverse Radius Min | always applied | minimal | 0.900000 |  |
| Cascade Transverse Radius Min | 1 | minimal | 1.000000 |  |
| Lambda CPA Min | always applied | minimal | 0.970000 |  |
| Lambda CPA Min | 2 | minimal | 0.987600 |  |
| Lambda CPA Min | 3 | minimal | 0.988000 |  |
| Lambda DCA Daughter Max | always applied | minimal | 0.500000 |  |
| Lambda DCA Daughter Max | 4 | minimal | 0.400000 |  |
| Lambda Transverse Radius Min | always applied | minimal | 1.200000 |  |
| Lambda Transverse Radius Min | 5 | minimal | 1.400000 |  |
| Lambda DCA to PV Min | always applied | minimal | 0.020000 |  |
| Lambda DCA to PV Min | 6 | minimal | 0.030000 |  |
| Lambda Daughter Mass Range | always applied | minimal | 1;1.2 |  |
| Reject Omega mass hypothesis | always applied | minimal | 1.668;1.676 |  |
| Daughter Abs Eta Max | always applied | minimal | 0.830000 |  |
| Daughter Abs Eta Max | 7 | minimal | 0.800000 |  |
| Daughter Abs Eta Max | 8 | minimal | 0.770000 |  |
| Daughter TPC Clusters Min | always applied | minimal | 80.000000 |  |
| Daughter TPC Clusters Min | 9 | minimal | 90.000000 |  |
| Daughter \|DCAxy\| Min | always applied | minimal | 0.050000 |  |
| Bachelor TPC Pion PID | always applied | minimal | 5.000000 |  |
| Bachelor TPC Pion PID | 10 | minimal | 4.000000 |  |
| Positive Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Positive Daughter TPC PID | 11 | minimal | 4.000000 |  |
| Negative Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Negative Daughter TPC PID | 12 | minimal | 4.000000 |  |

## Omega

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| massMin | 1.632 |
| massMax | 1.712 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Cascade CPA Min | always applied | minimal | 0.95 |  |
| Cascade DCA Daughters Max | always applied | minimal | 0.900000 |  |
| Cascade DCA Daughters Max | 0 | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | always applied | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | 1 | minimal | 1.000000 |  |
| Lambda CPA Min | always applied | minimal | 0.984000 |  |
| Lambda CPA Min | 2 | minimal | 0.985000 |  |
| Lambda DCA Daughter Max | always applied | minimal | 0.500000 |  |
| Lambda DCA Daughter Max | 3 | minimal | 0.400000 |  |
| Lambda Transverse Radius Min | always applied | minimal | 1.200000 |  |
| Lambda Transverse Radius Min | 4 | minimal | 1.400000 |  |
| Lambda DCA to PV Min | always applied | minimal | 0.030000 |  |
| Lambda DCA to PV Min | 5 | minimal | 0.040000 |  |
| Lambda Daughter Mass Range | always applied | minimal | 1;1.2 |  |
| Reject Xi mass hypothesis | always applied | minimal | 1.317;1.325 |  |
| Daughter Abs Eta Max | always applied | minimal | 0.850000 |  |
| Daughter Abs Eta Max | 6 | minimal | 0.800000 |  |
| Daughter Abs Eta Max | 7 | minimal | 0.750000 |  |
| Daughter TPC Clusters Min | always applied | minimal | 70.000000 |  |
| Daughter TPC Clusters Min | 8 | minimal | 80.000000 |  |
| Daughter \|DCAxy\| Min | always applied | minimal | 0.050000 |  |
| Bachelor TPC Kaon PID | always applied | minimal | 5.000000 |  |
| Bachelor TPC Kaon PID | 9 | minimal | 4.000000 |  |
| Positive Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Positive Daughter TPC PID | 10 | minimal | 4.000000 |  |
| Negative Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Negative Daughter TPC PID | 11 | minimal | 4.000000 |  |

## Photon

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 6 |
| etaMin | -10 |
| etaMax | 10 |
| phiMin | 0 |
| phiMax | 6.28319 |
| mGammaAbsMax | 1e+10 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | always applied | minimal | 0.000000 |  |
| Min. CPA (cosine pointing angle) | 0 | minimal | 0.980000 |  |
| Min. CPA (cosine pointing angle) | 1 | minimal | 0.990000 |  |
| Max. \|DCAxy\| to PV | always applied | minimal | 10000000000.000000 |  |
| Max. \|DCAz\| to PV | always applied | minimal | 10000000000.000000 |  |
| Max. chi2/NDF of conversion vertex | always applied | minimal | 10000000000.000000 |  |
| Min. transverse radius | always applied | minimal | 0.000000 |  |
| Min. transverse radius | 2 | minimal | 16.000000 |  |
| Max. transverse radius | always applied | minimal | 10000000000.000000 |  |
| Max. absolute pseudorapidity of daughters | always applied | minimal | 0.900000 |  |
| Max. absolute pseudorapidity of daughters | 3 | minimal | 0.800000 |  |
| Max. absolute pseudorapidity of daughters | 4 | minimal | 0.750000 |  |
| TPC electron PID for positive daughter | always applied | minimal | 5.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | 5 | minimal | 4.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | 6 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | always applied | minimal | 5.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | 7 | minimal | 4.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | 8 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
