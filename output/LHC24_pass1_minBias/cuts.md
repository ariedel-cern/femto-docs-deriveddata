# CF_LHC24_pass1_minBias_Femto_GP

**AnalysisResults.root for cutculator.py:** [https://alimonitor.cern.ch/catalogue/?path=/alice/cern.ch/user/a/alihyperloop/jobs/0624/hy_6246406/AOD#/alice/cern.ch/user/a/alihyperloop/jobs/0624/hy_6246406/AOD/002/](https://alimonitor.cern.ch/catalogue/?path=/alice/cern.ch/user/a/alihyperloop/jobs/0624/hy_6246406/AOD#/alice/cern.ch/user/a/alihyperloop/jobs/0624/hy_6246406/AOD/002/)

**Hyperloop dataset:** [https://alimonitor.cern.ch/hyperloop/view-dataset/2668](https://alimonitor.cern.ch/hyperloop/view-dataset/2668)

| | |
| --- | --- |
| Software tag | VO_ALICE@O2Physics::daily-20261008-0000-1 |
| Test train | [777635](https://alimonitor.cern.ch/hyperloop/train-run/777635/general) |
| Production train | [777635](https://alimonitor.cern.ch/hyperloop/train-run/777635/general) |

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
| Sel8 | 0 | optional | 1.000000 |  |
| RCT flags ok | always applied | minimal | 1.000000 | label = CBT_hadronPID; useZdc = 0; treatLimitedAcceptanceAsBad = 0 |
| No same bunch pileup | 1 | optional | 1.000000 |  |
| Is vertex ITS TPC | 2 | optional | 1.000000 |  |
| Is good zvtx FT0 vs PV | 3 | optional | 1.000000 |  |
| No collision in time range narrow | 4 | optional | 1.000000 |  |
| No collision in time range strict | 5 | optional | 1.000000 |  |
| No collision in time range standard | 6 | optional | 1.000000 |  |
| No collision in ROF strict | 7 | optional | 1.000000 |  |
| No collision in ROF standard | 8 | optional | 1.000000 |  |
| No high mult collisions in previous ROF | 9 | optional | 1.000000 |  |
| Is good ITS layer 3 | 10 | optional | 1.000000 |  |
| Is good ITS layer 0-3 | 11 | optional | 1.000000 |  |
| Is good ITS layer all | 12 | optional | 1.000000 |  |
| Minimum Sphericity | always applied | minimal | 0.000000 |  |
| Minimum Sphericity | 13 | minimal | 0.700000 |  |

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
| ITS He3 PID | 13 | optional | -1.5;3.40282e+38 |  |
| ITS He3 PID | 14 | optional | -1.3;3.40282e+38 |  |
| TPC Pion PID | 15 | optional | -3.5;3 |  |
| TPC Pion PID | 16 | optional | -3;3 |  |
| TPC Pion PID | 17 | optional | -2.5;2.5 |  |
| TPC Kaon PID | 18 | optional | -3.5;3 |  |
| TPC Kaon PID | 19 | optional | -3;3 |  |
| TPC Kaon PID | 20 | optional | -2.5;2.5 |  |
| TPC Proton PID | 21 | optional | -3.5;3 |  |
| TPC Proton PID | 22 | optional | -3;3 |  |
| TPC Proton PID | 23 | optional | -2.5;2.5 |  |
| TPC He3 PID | 24 | optional | -2.5;2.5 |  |
| TPC He3 PID | 25 | optional | -2;2 |  |
| TPC He3 PID | 26 | optional | -1.5;1.5 |  |
| TPC+ITS Pion PID | 27 | optional | 3.500000 |  |
| TPC+ITS Pion PID | 28 | optional | 3.000000 |  |
| TPC+ITS Pion PID | 29 | optional | 2.500000 |  |
| TPC+ITS Kaon PID | 30 | optional | 3.500000 |  |
| TPC+ITS Kaon PID | 31 | optional | 3.000000 |  |
| TPC+ITS Kaon PID | 32 | optional | 2.500000 |  |
| TPC+ITS Proton PID | 33 | optional | 3.500000 |  |
| TPC+ITS Proton PID | 34 | optional | 3.000000 |  |
| TPC+ITS Proton PID | 35 | optional | 2.500000 |  |
| TPC+ITS Deuteron PID | 36 | optional | 3.500000 |  |
| TPC+ITS Deuteron PID | 37 | optional | 3.000000 |  |
| TPC+ITS Deuteron PID | 38 | optional | 2.500000 |  |
| TPC+ITS Triton PID | 39 | optional | 3.500000 |  |
| TPC+ITS Triton PID | 40 | optional | 3.000000 |  |
| TPC+ITS Triton PID | 41 | optional | 2.500000 |  |
| TPC+TOF Pion PID | 42 | optional | 3.500000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Pion PID | 43 | optional | 3.000000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Pion PID | 44 | optional | 2.500000 | TOF mandatory above 0.5 GeV/c |
| TPC+TOF Kaon PID | 45 | optional | 3.500000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Kaon PID | 46 | optional | 3.000000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Kaon PID | 47 | optional | 2.500000 | TOF mandatory above 0.4 GeV/c |
| TPC+TOF Proton PID | 48 | optional | 3.500000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Proton PID | 49 | optional | 3.000000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Proton PID | 50 | optional | 2.500000 | TOF mandatory above 0.75 GeV/c |
| TPC+TOF Deuteron PID | 51 | optional | 3.500000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF Deuteron PID | 52 | optional | 3.000000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF Deuteron PID | 53 | optional | 2.500000 | TOF mandatory above 1.2 GeV/c |
| TPC+TOF Triton PID | 54 | optional | 3.000000 | TOF mandatory above 2 GeV/c |
| TPC+TOF Triton PID | 55 | optional | 2.500000 | TOF mandatory above 2 GeV/c |
| TPC+TOF He3 PID | 56 | optional | 3.500000 | TOF mandatory above 99 GeV/c |
| TPC+TOF He3 PID | 57 | optional | 3.000000 | TOF mandatory above 99 GeV/c |
| TPC+TOF He3 PID | 58 | optional | 2.500000 | TOF mandatory above 99 GeV/c |

## K0short

> Lambda rejection via prefilter, cannot be changed during analysis.

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| rejectK0short | 0 |
| k0shortMassMin | 0.43 |
| k0shortMassMax | 0.58 |
| rejectLambda | 1 |
| lambdaMassMin | 1.108 |
| lambdaMassMax | 1.122 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | always applied | minimal | 0.988000 |  |
| Min. CPA (cosine pointing angle) | 0 | minimal | 0.990000 |  |
| Min. CPA (cosine pointing angle) | 1 | minimal | 0.992000 |  |
| Max. DCA of the daughters at decay vertex | always applied | minimal | 1.500000 |  |
| Max. DCA of the daughters at decay vertex | 2 | minimal | 1.200000 |  |
| Max. DCA of the daughters at decay vertex | 3 | minimal | 1.000000 |  |
| Max. distance of decay vertex in x,y,z | always applied | minimal | 100.000000 |  |
| Min. transverse radius | always applied | minimal | 0.200000 |  |
| Min. transverse radius | 4 | minimal | 0.300000 |  |
| Min. transverse radius | 5 | minimal | 0.500000 |  |
| Max. transverse radius | always applied | minimal | 100.000000 |  |
| Max. absolute pseudo rapidity of daughters | always applied | minimal | 0.830000 |  |
| Max. absolute pseudo rapidity of daughters | 6 | minimal | 0.800000 |  |
| Max. absolute pseudo rapidity of daughters | 7 | minimal | 0.770000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | always applied | minimal | 0.040000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | 8 | minimal | 0.050000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | 9 | minimal | 0.060000 |  |
| Min. number of TPC clusters of daughters | always applied | minimal | 70.000000 |  |
| Min. number of TPC clusters of daughters | 10 | minimal | 80.000000 |  |
| Min. number of TPC clusters of daughters | 11 | minimal | 90.000000 |  |
| TPC Pion PID for positive daughter | always applied | minimal | 5.000000 |  |
| TPC Pion PID for positive daughter | 12 | minimal | 4.000000 |  |
| TPC Pion PID for positive daughter | 13 | minimal | 3.000000 |  |
| TPC Pion PID for negative daughter | always applied | minimal | 5.000000 |  |
| TPC Pion PID for negative daughter | 14 | minimal | 4.000000 |  |
| TPC Pion PID for negative daughter | 15 | minimal | 3.000000 |  |
| TOF Pion PID for negative daughter | 16 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Pion PID for negative daughter | 17 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Pion PID for negative daughter | 18 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |

## Lambda

> K0short rejection via prefilter, cannot be changed during analysis.

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| rejectK0short | 1 |
| k0shortMassMin | 0.48 |
| k0shortMassMax | 0.515 |
| rejectLambda | 0 |
| lambdaMassMin | 1 |
| lambdaMassMax | 1.18 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | always applied | minimal | 0.988000 |  |
| Min. CPA (cosine pointing angle) | 0 | minimal | 0.990000 |  |
| Min. CPA (cosine pointing angle) | 1 | minimal | 0.992000 |  |
| Max. DCA of the daughters at decay vertex | always applied | minimal | 1.500000 |  |
| Max. DCA of the daughters at decay vertex | 2 | minimal | 1.200000 |  |
| Max. DCA of the daughters at decay vertex | 3 | minimal | 1.000000 |  |
| Max. distance of decay vertex in x,y,z | always applied | minimal | 100.000000 |  |
| Min. transverse radius | always applied | minimal | 0.200000 |  |
| Min. transverse radius | 4 | minimal | 0.300000 |  |
| Min. transverse radius | 5 | minimal | 0.500000 |  |
| Max. transverse radius | always applied | minimal | 100.000000 |  |
| Max. absolute pseudo rapidity of daughters | always applied | minimal | 0.830000 |  |
| Max. absolute pseudo rapidity of daughters | 6 | minimal | 0.800000 |  |
| Max. absolute pseudo rapidity of daughters | 7 | minimal | 0.770000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | always applied | minimal | 0.040000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | 8 | minimal | 0.050000 |  |
| Min. \|DCAxy\| of the daughters from primary vertex | 9 | minimal | 0.060000 |  |
| Min. number of TPC clusters of daughters | always applied | minimal | 70.000000 |  |
| Min. number of TPC clusters of daughters | 10 | minimal | 80.000000 |  |
| Min. number of TPC clusters of daughters | 11 | minimal | 90.000000 |  |
| TPC Proton PID for positive daughter | always applied | minimal | 5.000000 |  |
| TPC Proton PID for positive daughter | 12 | minimal | 4.000000 |  |
| TPC Proton PID for positive daughter | 13 | minimal | 3.000000 |  |
| TPC Pion PID for negative daughter | always applied | minimal | 5.000000 |  |
| TPC Pion PID for negative daughter | 14 | minimal | 4.000000 |  |
| TPC Pion PID for negative daughter | 15 | minimal | 3.000000 |  |
| TOF Proton PID for positive daughter | 16 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Proton PID for positive daughter | 17 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Proton PID for positive daughter | 18 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Pion PID for negative daughter | 19 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Pion PID for negative daughter | 20 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| TOF Pion PID for negative daughter | 21 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |

## Sigma

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0.4 |
| ptMax | 6 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| massMin | 1.1 |
| massMax | 1.3 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| kinkTopoDcaMax | always applied | minimal | 2.000000 |  |
| transRadMin | always applied | minimal | 19.600000 |  |
| transRadMax | always applied | minimal | 100.000000 |  |
| dauAbsEtaMax | always applied | minimal | 1.000000 |  |
| dauAbsEtaMax | 0 | minimal | 0.900000 |  |
| dauAbsEtaMax | 1 | minimal | 0.800000 |  |
| dauDcaPvMin | always applied | minimal | 0.100000 |  |
| mothDcaPvMax | always applied | minimal | 0.025000 |  |
| mothDcaPvMax | 2 | minimal | 0.020000 |  |
| chaDauTpcPion | always applied | minimal | 5.000000 |  |
| chaDauTpcPion | 3 | minimal | 4.000000 |  |
| alphaAPMin | always applied | minimal | -1.000000 |  |
| alphaAPMax | always applied | minimal | 0.000000 |  |
| qtAPMin | always applied | minimal | 0.145000 |  |
| qtAPMin | 4 | minimal | 0.150000 |  |
| qtAPMin | 5 | minimal | 0.155000 |  |
| qtAPMax | always applied | minimal | 0.210000 |  |
| qtAPMax | 6 | minimal | 0.205000 |  |
| qtAPMax | 7 | minimal | 0.200000 |  |
| cosPointingAngleMin | always applied | minimal | 0.988000 |  |
| cosPointingAngleMin | 8 | minimal | 0.990000 |  |
| cosPointingAngleMin | 9 | minimal | 0.992000 |  |
| ptOriginalMin | always applied | minimal | 1.200000 |  |
| ptOriginalMin | 10 | minimal | 1.400000 |  |
| ptOriginalMin | 11 | minimal | 1.600000 |  |
| ptOriginalMin | 12 | minimal | 1.800000 |  |
| ptOriginalMax | always applied | minimal | 10.000000 |  |

## Sigma Plus

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0.4 |
| ptMax | 6 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| massMin | 1.1 |
| massMax | 1.3 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| kinkTopoDcaMax | always applied | minimal | 2.000000 |  |
| transRadMin | always applied | minimal | 19.600000 |  |
| transRadMax | always applied | minimal | 100.000000 |  |
| dauAbsEtaMax | always applied | minimal | 1.000000 |  |
| dauAbsEtaMax | 0 | minimal | 0.900000 |  |
| dauAbsEtaMax | 1 | minimal | 0.800000 |  |
| dauDcaPvMin | always applied | minimal | 0.100000 |  |
| mothDcaPvMax | always applied | minimal | 0.025000 |  |
| mothDcaPvMax | 2 | minimal | 0.020000 |  |
| chaDauTpcProton | always applied | minimal | 5.000000 |  |
| chaDauTpcProton | 3 | minimal | 4.000000 |  |
| chaDauTofProton | always applied | neutral | 4.500000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| chaDauTofProton | 4 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| chaDauTofProton | 5 | neutral | 3.500000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| alphaAPMin | always applied | minimal | 0.000000 |  |
| alphaAPMax | always applied | minimal | 1.000000 |  |
| qtAPMin | always applied | minimal | 0.100000 |  |
| qtAPMin | 6 | minimal | 0.125000 |  |
| qtAPMin | 7 | minimal | 0.150000 |  |
| qtAPMax | always applied | minimal | 0.220000 |  |
| qtAPMax | 8 | minimal | 0.210000 |  |
| qtAPMax | 9 | minimal | 0.200000 |  |
| cosPointingAngleMin | always applied | minimal | 0.988000 |  |
| cosPointingAngleMin | 10 | minimal | 0.990000 |  |
| cosPointingAngleMin | 11 | minimal | 0.992000 |  |
| ptOriginalMin | always applied | minimal | 1.200000 |  |
| ptOriginalMin | 12 | minimal | 1.400000 |  |
| ptOriginalMin | 13 | minimal | 1.600000 |  |
| ptOriginalMin | 14 | minimal | 1.800000 |  |
| ptOriginalMax | always applied | minimal | 10.000000 |  |

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
| lambdaMassMin | 1.092 |
| lambdaMassMax | 1.139 |
| xiMassMin | 1.26 |
| xiMassMax | 1.38 |
| rejectOmega | 0 |
| omegaMassMin | 0 |
| omegaMassMax | 0 |
| rejectXi | 0 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Cascade CPA Min | always applied | minimal | 0.98 |  |
| Cascade CPA Min | 0 | minimal | 0.9947 |  |
| Cascade DCA Daughters Max | always applied | minimal | 0.600000 |  |
| Cascade DCA Daughters Max | 1 | minimal | 0.500000 |  |
| Cascade DCA Daughters Max | 2 | minimal | 0.250000 |  |
| Cascade Transverse Radius Min | always applied | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | 3 | minimal | 1.100000 |  |
| Lambda CPA Min | always applied | minimal | 0.970000 |  |
| Lambda CPA Min | 4 | minimal | 0.980000 |  |
| Lambda CPA Min | 5 | minimal | 0.987600 |  |
| Lambda DCA Daughter Max | always applied | minimal | 1.000000 |  |
| Lambda DCA Daughter Max | 6 | minimal | 0.600000 |  |
| Lambda DCA Daughter Max | 7 | minimal | 0.500000 |  |
| Lambda Transverse Radius Min | always applied | minimal | 1.400000 |  |
| Lambda Transverse Radius Min | 8 | minimal | 2.500000 |  |
| Lambda DCA to PV Min | always applied | minimal | 0.020000 |  |
| Lambda DCA to PV Min | 9 | minimal | 0.030000 |  |
| Lambda DCA to PV Min | 10 | minimal | 0.040000 |  |
| Daughter Abs Eta Max | always applied | minimal | 0.830000 |  |
| Daughter Abs Eta Max | 11 | minimal | 0.800000 |  |
| Daughter Abs Eta Max | 12 | minimal | 0.770000 |  |
| Daughter TPC Clusters Min | always applied | minimal | 70.000000 |  |
| Daughter TPC Clusters Min | 13 | minimal | 80.000000 |  |
| Daughter TPC Clusters Min | 14 | minimal | 90.000000 |  |
| Daughter \|DCAxy\| Min | always applied | minimal | 0.040000 |  |
| Daughter \|DCAxy\| Min | 15 | minimal | 0.050000 |  |
| Daughter \|DCAxy\| Min | 16 | minimal | 0.060000 |  |
| Bachelor TPC Pion PID | always applied | minimal | 5.000000 |  |
| Bachelor TPC Pion PID | 17 | minimal | 4.000000 |  |
| Bachelor TPC Pion PID | 18 | minimal | 3.000000 |  |
| Bachelor TOF Pion PID | 19 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Bachelor TOF Pion PID | 20 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Bachelor TOF Pion PID | 21 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Positive Daughter TPC PID | 22 | minimal | 4.000000 |  |
| Positive Daughter TPC PID | 23 | minimal | 3.000000 |  |
| Negative Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Negative Daughter TPC PID | 24 | minimal | 4.000000 |  |
| Negative Daughter TPC PID | 25 | minimal | 3.000000 |  |
| Positive Daughter TOF PID | 26 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TOF PID | 27 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TOF PID | 28 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Negative Daughter TOF PID | 29 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Negative Daughter TOF PID | 30 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Negative Daughter TOF PID | 31 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |

## Omega

> Xi rejection via prefilter, cannot be changed during analysis.

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -99 |
| etaMax | 99 |
| phiMin | 0 |
| phiMax | 6.28319 |
| lambdaMassMin | 1.092 |
| lambdaMassMax | 1.139 |
| xiMassMin | 1.313 |
| xiMassMax | 1.332 |
| rejectOmega | 0 |
| omegaMassMin | 1.55 |
| omegaMassMax | 1.8 |
| rejectXi | 1 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Cascade CPA Min | always applied | minimal | 0.98 |  |
| Cascade CPA Min | 0 | minimal | 0.9947 |  |
| Cascade DCA Daughters Max | always applied | minimal | 0.600000 |  |
| Cascade DCA Daughters Max | 1 | minimal | 0.500000 |  |
| Cascade DCA Daughters Max | 2 | minimal | 0.250000 |  |
| Cascade Transverse Radius Min | always applied | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | 3 | minimal | 1.100000 |  |
| Lambda CPA Min | always applied | minimal | 0.970000 |  |
| Lambda CPA Min | 4 | minimal | 0.980000 |  |
| Lambda CPA Min | 5 | minimal | 0.987600 |  |
| Lambda DCA Daughter Max | always applied | minimal | 1.000000 |  |
| Lambda DCA Daughter Max | 6 | minimal | 0.600000 |  |
| Lambda DCA Daughter Max | 7 | minimal | 0.500000 |  |
| Lambda Transverse Radius Min | always applied | minimal | 1.400000 |  |
| Lambda Transverse Radius Min | 8 | minimal | 2.500000 |  |
| Lambda DCA to PV Min | always applied | minimal | 0.020000 |  |
| Lambda DCA to PV Min | 9 | minimal | 0.030000 |  |
| Lambda DCA to PV Min | 10 | minimal | 0.040000 |  |
| Daughter Abs Eta Max | always applied | minimal | 0.830000 |  |
| Daughter Abs Eta Max | 11 | minimal | 0.800000 |  |
| Daughter Abs Eta Max | 12 | minimal | 0.770000 |  |
| Daughter TPC Clusters Min | always applied | minimal | 70.000000 |  |
| Daughter TPC Clusters Min | 13 | minimal | 80.000000 |  |
| Daughter TPC Clusters Min | 14 | minimal | 90.000000 |  |
| Daughter \|DCAxy\| Min | always applied | minimal | 0.040000 |  |
| Daughter \|DCAxy\| Min | 15 | minimal | 0.050000 |  |
| Daughter \|DCAxy\| Min | 16 | minimal | 0.060000 |  |
| Bachelor TPC Kaon PID | always applied | minimal | 5.000000 |  |
| Bachelor TPC Kaon PID | 17 | minimal | 4.000000 |  |
| Bachelor TPC Kaon PID | 18 | minimal | 3.000000 |  |
| Bachelor TOF Kaon PID | 19 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Bachelor TOF Kaon PID | 20 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Bachelor TOF Kaon PID | 21 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Positive Daughter TPC PID | 22 | minimal | 4.000000 |  |
| Positive Daughter TPC PID | 23 | minimal | 3.000000 |  |
| Negative Daughter TPC PID | always applied | minimal | 5.000000 |  |
| Negative Daughter TPC PID | 24 | minimal | 4.000000 |  |
| Negative Daughter TPC PID | 25 | minimal | 3.000000 |  |
| Positive Daughter TOF PID | 26 | neutral | 5.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TOF PID | 27 | neutral | 4.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |
| Positive Daughter TOF PID | 28 | neutral | 3.000000 | passes if daughter has no TOF; else nSigmaTOF computed with corrected time |

## Photon

### Prefilters

| Filter | Value |
| --- | --- |
| ptMin | 0 |
| ptMax | 99 |
| etaMin | -10 |
| etaMax | 10 |
| phiMin | 0 |
| phiMax | 6.28319 |
| mGammaAbsMax | 1e+10 |

### Cuts

| Selection | Bit | Type | Value | Comment |
| --- | --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | always applied | minimal | 0.850000 |  |
| Min. CPA (cosine pointing angle) | 0 | minimal | 0.900000 |  |
| Min. CPA (cosine pointing angle) | 1 | minimal | 0.950000 |  |
| Max. \|DCAxy\| to PV | always applied | minimal | 999999995904.000000 |  |
| Max. \|DCAz\| to PV | always applied | minimal | 999999995904.000000 |  |
| Max. chi2/NDF of conversion vertex | always applied | minimal | 999999995904.000000 |  |
| Min. transverse radius | always applied | minimal | 0.000000 |  |
| Min. transverse radius | 2 | minimal | 5.000000 |  |
| Min. transverse radius | 3 | minimal | 10.000000 |  |
| Max. transverse radius | always applied | minimal | 180.000000 |  |
| Max. transverse radius | 4 | minimal | 160.000000 |  |
| Max. transverse radius | 5 | minimal | 120.000000 |  |
| Max. absolute pseudorapidity of daughters | always applied | minimal | 0.950000 |  |
| Max. absolute pseudorapidity of daughters | 6 | minimal | 0.900000 |  |
| Max. absolute pseudorapidity of daughters | 7 | minimal | 0.850000 |  |
| TPC electron PID for positive daughter | always applied | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | 8 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | 9 | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | always applied | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | 10 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | 11 | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |
