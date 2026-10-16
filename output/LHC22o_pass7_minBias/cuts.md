# Configured cuts

> Femto producer cuts for the GP derived-data train, wagon AAA_FemtoProducer_GP_Derived_22_24_v3

**Download the derived data:** _pending -- added once the production train completes_

| | |
| --- | --- |
| Package tag | VO_ALICE@O2Physics::daily-20261008-0000-1 |
| Production type | DATA |
| Input data | /alice/data/2022/LHC22o/527041/apass7/0500 + 1 more |

## Performance overview

Measured on this test; "expected" rows extrapolate this test's ratios to the full dataset.

| | |
| --- | --- |
| Reduction factor | 94.4x |
| PSS memory | avg 4.6 GB, max 4.7 GB |
| Throughput | 3.8 MB/s per core |
| Expected resources (full run) | 976d 1h 56m 2s core-time |
| Expected output size (full run) | 3.2 TB |

## Collision

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Sel8 | optional | 1.000000 |  |
| RCT flags ok | minimal | 1.000000 | label = CBT_hadronPID; useZdc = 0; treatLimitedAcceptanceAsBad = 0 |
| No same bunch pileup | optional | 1.000000 |  |
| Is vertex ITS TPC | optional | 1.000000 |  |
| Is good zvtx FT0 vs PV | optional | 1.000000 |  |
| No collision in time range narrow | optional | 1.000000 |  |
| No collision in time range strict | optional | 1.000000 |  |
| No collision in time range standard | optional | 1.000000 |  |
| No collision in ROF strict | optional | 1.000000 |  |
| No collision in ROF standard | optional | 1.000000 |  |
| No high mult collisions in previous ROF | optional | 1.000000 |  |
| Is good ITS layer 3 | optional | 1.000000 |  |
| Is good ITS layer 0-3 | optional | 1.000000 |  |
| Is good ITS layer all | optional | 1.000000 |  |
| Minimum Sphericity | minimal | 0.000000 |  |
| Minimum Sphericity | minimal | 0.700000 |  |

## Track

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Min. number of TPC clusters | minimal | 90.000000 |  |
| Min. number of TPC clusters | minimal | 100.000000 |  |
| Min. number of TPC clusters | minimal | 110.000000 |  |
| Min. number of TPC clusters | minimal | 120.000000 |  |
| Min. number of crossed TPC rows | minimal | 80.000000 |  |
| Min. number of crossed TPC rows | minimal | 90.000000 |  |
| Min. number of crossed TPC rows | minimal | 100.000000 |  |
| Min. number of crossed TPC rows | minimal | 110.000000 |  |
| Min. fraction of TPC clusters over TPC crossed rows | minimal | 0.000000 |  |
| Max. number of shared TPC clusters | minimal | 160.000000 |  |
| Max. fractions of shared TPC clusters | minimal | 1.000000 |  |
| Max. fractions of shared TPC clusters | minimal | 0.800000 |  |
| Max. fractions of shared TPC clusters | minimal | 0.400000 |  |
| Min. number of ITS clusters | minimal | 5.000000 |  |
| Min. number of ITS clusters | minimal | 6.000000 |  |
| Min. number of ITS clusters | minimal | 7.000000 |  |
| Min. number of ITS clusters in the inner barrel | minimal | 1.000000 |  |
| Min. number of ITS clusters in the inner barrel | minimal | 3.000000 |  |
| Max. |DCA_xy| (cm) as a function of pT | minimal | 0.1 |  |
| Max. |DCA_xy| (cm) as a function of pT | minimal | 0.004+0.013*pow(x,-1) |  |
| Max. |DCA_z| (cm) as a function of pT | minimal | 0.2 |  |
| Max. |DCA_z| (cm) as a function of pT | minimal | 0.004+0.013*pow(x,-1) |  |
| ITS He3 PID | optional | -1.5;3.40282e+38 |  |
| ITS He3 PID | optional | -1.3;3.40282e+38 |  |
| TPC Pion PID | optional | -3.5;3 |  |
| TPC Pion PID | optional | -3;3 |  |
| TPC Pion PID | optional | -2.5;2.5 |  |
| TPC Kaon PID | optional | -3.5;3 |  |
| TPC Kaon PID | optional | -3;3 |  |
| TPC Kaon PID | optional | -2.5;2.5 |  |
| TPC Proton PID | optional | -3.5;3 |  |
| TPC Proton PID | optional | -3;3 |  |
| TPC Proton PID | optional | -2.5;2.5 |  |
| TPC He3 PID | optional | -2.5;2.5 |  |
| TPC He3 PID | optional | -2;2 |  |
| TPC He3 PID | optional | -1.5;1.5 |  |
| TPC+ITS Pion PID | optional | 3.500000 |  |
| TPC+ITS Pion PID | optional | 3.000000 |  |
| TPC+ITS Pion PID | optional | 2.500000 |  |
| TPC+ITS Kaon PID | optional | 3.500000 |  |
| TPC+ITS Kaon PID | optional | 3.000000 |  |
| TPC+ITS Kaon PID | optional | 2.500000 |  |
| TPC+ITS Proton PID | optional | 3.500000 |  |
| TPC+ITS Proton PID | optional | 3.000000 |  |
| TPC+ITS Proton PID | optional | 2.500000 |  |
| TPC+ITS Deuteron PID | optional | 3.500000 |  |
| TPC+ITS Deuteron PID | optional | 3.000000 |  |
| TPC+ITS Deuteron PID | optional | 2.500000 |  |
| TPC+ITS Triton PID | optional | 3.500000 |  |
| TPC+ITS Triton PID | optional | 3.000000 |  |
| TPC+ITS Triton PID | optional | 2.500000 |  |
| TPC+TOF Pion PID | optional | 3.500000 | minMomTofPion = 0.500000 |
| TPC+TOF Pion PID | optional | 3.000000 | minMomTofPion = 0.500000 |
| TPC+TOF Pion PID | optional | 2.500000 | minMomTofPion = 0.500000 |
| TPC+TOF Kaon PID | optional | 3.500000 | minMomTofKaon = 0.400000 |
| TPC+TOF Kaon PID | optional | 3.000000 | minMomTofKaon = 0.400000 |
| TPC+TOF Kaon PID | optional | 2.500000 | minMomTofKaon = 0.400000 |
| TPC+TOF Proton PID | optional | 3.500000 | minMomTofProton = 0.750000 |
| TPC+TOF Proton PID | optional | 3.000000 | minMomTofProton = 0.750000 |
| TPC+TOF Proton PID | optional | 2.500000 | minMomTofProton = 0.750000 |
| TPC+TOF Deuteron PID | optional | 3.500000 | minMomTofDeuteron = 1.200000 |
| TPC+TOF Deuteron PID | optional | 3.000000 | minMomTofDeuteron = 1.200000 |
| TPC+TOF Deuteron PID | optional | 2.500000 | minMomTofDeuteron = 1.200000 |
| TPC+TOF Triton PID | optional | 3.000000 | minMomTofTriton = 2.000000 |
| TPC+TOF Triton PID | optional | 2.500000 | minMomTofTriton = 2.000000 |
| TPC+TOF He3 PID | optional | 3.500000 | minMomTofHelium = 99.000000 |
| TPC+TOF He3 PID | optional | 3.000000 | minMomTofHelium = 99.000000 |
| TPC+TOF He3 PID | optional | 2.500000 | minMomTofHelium = 99.000000 |

## K0short

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | minimal | 0.988000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.990000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.992000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.500000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.200000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.000000 |  |
| Max. distance of decay vertex in x,y,z | minimal | 100.000000 |  |
| Min. transverse radius | minimal | 0.200000 |  |
| Min. transverse radius | minimal | 0.300000 |  |
| Min. transverse radius | minimal | 0.500000 |  |
| Max. transverse radius | minimal | 100.000000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.830000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.800000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.770000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.040000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.050000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.060000 |  |
| Min. number of TPC clusters of daughters | minimal | 70.000000 |  |
| Min. number of TPC clusters of daughters | minimal | 80.000000 |  |
| Min. number of TPC clusters of daughters | minimal | 90.000000 |  |
| TPC Pion PID for positive daughter | minimal | 5.000000 |  |
| TPC Pion PID for positive daughter | minimal | 4.000000 |  |
| TPC Pion PID for positive daughter | minimal | 3.000000 |  |
| TPC Pion PID for negative daughter | minimal | 5.000000 |  |
| TPC Pion PID for negative daughter | minimal | 4.000000 |  |
| TPC Pion PID for negative daughter | minimal | 3.000000 |  |
| TOF Pion PID for negative daughter | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Pion PID for negative daughter | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Pion PID for negative daughter | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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
| rejectK0short | 1 |
| k0shortMassMin | 0.48 |
| k0shortMassMax | 0.515 |
| rejectLambda | 0 |
| lambdaMassMin | 1 |
| lambdaMassMax | 1.18 |

### Cuts

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | minimal | 0.988000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.990000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.992000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.500000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.200000 |  |
| Max. DCA of the daughters at decay vertex | minimal | 1.000000 |  |
| Max. distance of decay vertex in x,y,z | minimal | 100.000000 |  |
| Min. transverse radius | minimal | 0.200000 |  |
| Min. transverse radius | minimal | 0.300000 |  |
| Min. transverse radius | minimal | 0.500000 |  |
| Max. transverse radius | minimal | 100.000000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.830000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.800000 |  |
| Max. absolute pseudo rapidity of daughters | minimal | 0.770000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.040000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.050000 |  |
| Min. |DCAxy| of the daughters from primary vertex | minimal | 0.060000 |  |
| Min. number of TPC clusters of daughters | minimal | 70.000000 |  |
| Min. number of TPC clusters of daughters | minimal | 80.000000 |  |
| Min. number of TPC clusters of daughters | minimal | 90.000000 |  |
| TPC Proton PID for positive daughter | minimal | 5.000000 |  |
| TPC Proton PID for positive daughter | minimal | 4.000000 |  |
| TPC Proton PID for positive daughter | minimal | 3.000000 |  |
| TPC Pion PID for negative daughter | minimal | 5.000000 |  |
| TPC Pion PID for negative daughter | minimal | 4.000000 |  |
| TPC Pion PID for negative daughter | minimal | 3.000000 |  |
| TOF Proton PID for positive daughter | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Proton PID for positive daughter | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Proton PID for positive daughter | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Pion PID for negative daughter | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Pion PID for negative daughter | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| TOF Pion PID for negative daughter | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| kinkTopoDcaMax | minimal | 2.000000 |  |
| transRadMin | minimal | 19.600000 |  |
| transRadMax | minimal | 100.000000 |  |
| dauAbsEtaMax | minimal | 1.000000 |  |
| dauAbsEtaMax | minimal | 0.900000 |  |
| dauAbsEtaMax | minimal | 0.800000 |  |
| dauDcaPvMin | minimal | 0.100000 |  |
| mothDcaPvMax | minimal | 0.025000 |  |
| mothDcaPvMax | minimal | 0.020000 |  |
| chaDauTpcPion | minimal | 5.000000 |  |
| chaDauTpcPion | minimal | 4.000000 |  |
| alphaAPMin | minimal | -1.000000 |  |
| alphaAPMax | minimal | 0.000000 |  |
| qtAPMin | minimal | 0.145000 |  |
| qtAPMin | minimal | 0.150000 |  |
| qtAPMin | minimal | 0.155000 |  |
| qtAPMax | minimal | 0.210000 |  |
| qtAPMax | minimal | 0.205000 |  |
| qtAPMax | minimal | 0.200000 |  |
| cosPointingAngleMin | minimal | 0.988000 |  |
| cosPointingAngleMin | minimal | 0.990000 |  |
| cosPointingAngleMin | minimal | 0.992000 |  |
| ptOriginalMin | minimal | 1.200000 |  |
| ptOriginalMin | minimal | 1.400000 |  |
| ptOriginalMin | minimal | 1.600000 |  |
| ptOriginalMin | minimal | 1.800000 |  |
| ptOriginalMax | minimal | 10.000000 |  |

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| kinkTopoDcaMax | minimal | 2.000000 |  |
| transRadMin | minimal | 19.600000 |  |
| transRadMax | minimal | 100.000000 |  |
| dauAbsEtaMax | minimal | 1.000000 |  |
| dauAbsEtaMax | minimal | 0.900000 |  |
| dauAbsEtaMax | minimal | 0.800000 |  |
| dauDcaPvMin | minimal | 0.100000 |  |
| mothDcaPvMax | minimal | 0.025000 |  |
| mothDcaPvMax | minimal | 0.020000 |  |
| chaDauTpcProton | minimal | 5.000000 |  |
| chaDauTpcProton | minimal | 4.000000 |  |
| chaDauTofProton | neutral | 4.500000 | requireTof = 0; keepTracksWithoutTof = 1 |
| chaDauTofProton | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| chaDauTofProton | neutral | 3.500000 | requireTof = 0; keepTracksWithoutTof = 1 |
| alphaAPMin | minimal | 0.000000 |  |
| alphaAPMax | minimal | 1.000000 |  |
| qtAPMin | minimal | 0.100000 |  |
| qtAPMin | minimal | 0.125000 |  |
| qtAPMin | minimal | 0.150000 |  |
| qtAPMax | minimal | 0.220000 |  |
| qtAPMax | minimal | 0.210000 |  |
| qtAPMax | minimal | 0.200000 |  |
| cosPointingAngleMin | minimal | 0.988000 |  |
| cosPointingAngleMin | minimal | 0.990000 |  |
| cosPointingAngleMin | minimal | 0.992000 |  |
| ptOriginalMin | minimal | 1.200000 |  |
| ptOriginalMin | minimal | 1.400000 |  |
| ptOriginalMin | minimal | 1.600000 |  |
| ptOriginalMin | minimal | 1.800000 |  |
| ptOriginalMax | minimal | 10.000000 |  |

## Xi

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Cascade CPA Min | minimal | 0.98 |  |
| Cascade CPA Min | minimal | 0.9947 |  |
| Cascade DCA Daughters Max | minimal | 0.600000 |  |
| Cascade DCA Daughters Max | minimal | 0.500000 |  |
| Cascade DCA Daughters Max | minimal | 0.250000 |  |
| Cascade Transverse Radius Min | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | minimal | 1.100000 |  |
| Lambda CPA Min | minimal | 0.970000 |  |
| Lambda CPA Min | minimal | 0.980000 |  |
| Lambda CPA Min | minimal | 0.987600 |  |
| Lambda DCA Daughter Max | minimal | 1.000000 |  |
| Lambda DCA Daughter Max | minimal | 0.600000 |  |
| Lambda DCA Daughter Max | minimal | 0.500000 |  |
| Lambda Transverse Radius Min | minimal | 1.400000 |  |
| Lambda Transverse Radius Min | minimal | 2.500000 |  |
| Lambda DCA to PV Min | minimal | 0.020000 |  |
| Lambda DCA to PV Min | minimal | 0.030000 |  |
| Lambda DCA to PV Min | minimal | 0.040000 |  |
| Daughter Abs Eta Max | minimal | 0.830000 |  |
| Daughter Abs Eta Max | minimal | 0.800000 |  |
| Daughter Abs Eta Max | minimal | 0.770000 |  |
| Daughter TPC Clusters Min | minimal | 70.000000 |  |
| Daughter TPC Clusters Min | minimal | 80.000000 |  |
| Daughter TPC Clusters Min | minimal | 90.000000 |  |
| Daughter |DCAxy| Min | minimal | 0.040000 |  |
| Daughter |DCAxy| Min | minimal | 0.050000 |  |
| Daughter |DCAxy| Min | minimal | 0.060000 |  |
| Bachelor TPC Pion PID | minimal | 5.000000 |  |
| Bachelor TPC Pion PID | minimal | 4.000000 |  |
| Bachelor TPC Pion PID | minimal | 3.000000 |  |
| Bachelor TOF Pion PID | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Bachelor TOF Pion PID | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Bachelor TOF Pion PID | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TPC PID | minimal | 5.000000 |  |
| Positive Daughter TPC PID | minimal | 4.000000 |  |
| Positive Daughter TPC PID | minimal | 3.000000 |  |
| Negative Daughter TPC PID | minimal | 5.000000 |  |
| Negative Daughter TPC PID | minimal | 4.000000 |  |
| Negative Daughter TPC PID | minimal | 3.000000 |  |
| Positive Daughter TOF PID | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TOF PID | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TOF PID | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Negative Daughter TOF PID | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Negative Daughter TOF PID | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Negative Daughter TOF PID | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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
| lambdaMassMin | 1.092 |
| lambdaMassMax | 1.139 |
| xiMassMin | 1.313 |
| xiMassMax | 1.332 |
| rejectOmega | 0 |
| omegaMassMin | 1.55 |
| omegaMassMax | 1.8 |
| rejectXi | 1 |

### Cuts

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Cascade CPA Min | minimal | 0.98 |  |
| Cascade CPA Min | minimal | 0.9947 |  |
| Cascade DCA Daughters Max | minimal | 0.600000 |  |
| Cascade DCA Daughters Max | minimal | 0.500000 |  |
| Cascade DCA Daughters Max | minimal | 0.250000 |  |
| Cascade Transverse Radius Min | minimal | 0.800000 |  |
| Cascade Transverse Radius Min | minimal | 1.100000 |  |
| Lambda CPA Min | minimal | 0.970000 |  |
| Lambda CPA Min | minimal | 0.980000 |  |
| Lambda CPA Min | minimal | 0.987600 |  |
| Lambda DCA Daughter Max | minimal | 1.000000 |  |
| Lambda DCA Daughter Max | minimal | 0.600000 |  |
| Lambda DCA Daughter Max | minimal | 0.500000 |  |
| Lambda Transverse Radius Min | minimal | 1.400000 |  |
| Lambda Transverse Radius Min | minimal | 2.500000 |  |
| Lambda DCA to PV Min | minimal | 0.020000 |  |
| Lambda DCA to PV Min | minimal | 0.030000 |  |
| Lambda DCA to PV Min | minimal | 0.040000 |  |
| Daughter Abs Eta Max | minimal | 0.830000 |  |
| Daughter Abs Eta Max | minimal | 0.800000 |  |
| Daughter Abs Eta Max | minimal | 0.770000 |  |
| Daughter TPC Clusters Min | minimal | 70.000000 |  |
| Daughter TPC Clusters Min | minimal | 80.000000 |  |
| Daughter TPC Clusters Min | minimal | 90.000000 |  |
| Daughter |DCAxy| Min | minimal | 0.040000 |  |
| Daughter |DCAxy| Min | minimal | 0.050000 |  |
| Daughter |DCAxy| Min | minimal | 0.060000 |  |
| Bachelor TPC Kaon PID | minimal | 5.000000 |  |
| Bachelor TPC Kaon PID | minimal | 4.000000 |  |
| Bachelor TPC Kaon PID | minimal | 3.000000 |  |
| Bachelor TOF Kaon PID | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Bachelor TOF Kaon PID | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Bachelor TOF Kaon PID | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TPC PID | minimal | 5.000000 |  |
| Positive Daughter TPC PID | minimal | 4.000000 |  |
| Positive Daughter TPC PID | minimal | 3.000000 |  |
| Negative Daughter TPC PID | minimal | 5.000000 |  |
| Negative Daughter TPC PID | minimal | 4.000000 |  |
| Negative Daughter TPC PID | minimal | 3.000000 |  |
| Positive Daughter TOF PID | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TOF PID | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| Positive Daughter TOF PID | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

| Selection | Type | Value | Comment |
| --- | --- | --- | --- |
| Min. CPA (cosine pointing angle) | minimal | 0.850000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.900000 |  |
| Min. CPA (cosine pointing angle) | minimal | 0.950000 |  |
| Max. |DCAxy| to PV | minimal | 999999995904.000000 |  |
| Max. |DCAz| to PV | minimal | 999999995904.000000 |  |
| Max. chi2/NDF of conversion vertex | minimal | 999999995904.000000 |  |
| Min. transverse radius | minimal | 0.000000 |  |
| Min. transverse radius | minimal | 5.000000 |  |
| Min. transverse radius | minimal | 10.000000 |  |
| Max. transverse radius | minimal | 180.000000 |  |
| Max. transverse radius | minimal | 160.000000 |  |
| Max. transverse radius | minimal | 120.000000 |  |
| Max. absolute pseudorapidity of daughters | minimal | 0.950000 |  |
| Max. absolute pseudorapidity of daughters | minimal | 0.900000 |  |
| Max. absolute pseudorapidity of daughters | minimal | 0.850000 |  |
| TPC electron PID for positive daughter | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for positive daughter | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| TPC electron PID for negative daughter | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |
