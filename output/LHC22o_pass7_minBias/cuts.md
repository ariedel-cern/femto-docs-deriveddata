# Configured cuts

Source: 778977 (resolved train id 778977, [test output](https://alimonitor.cern.ch/train-workdir/tests/0077/00778977/))

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

## Anti Lambda

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

**Min. CPA (cosine pointing angle)**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.988000 |  |
| 0 | minimal | 0.990000 |  |
| 1 | minimal | 0.992000 |  |

**Max. DCA of the daughters at decay vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.500000 |  |
| 2 | minimal | 1.200000 |  |
| 3 | minimal | 1.000000 |  |

**Max. distance of decay vertex in x,y,z**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Min. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.200000 |  |
| 4 | minimal | 0.300000 |  |
| 5 | minimal | 0.500000 |  |

**Max. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Max. absolute pseudo rapidity of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.830000 |  |
| 6 | minimal | 0.800000 |  |
| 7 | minimal | 0.770000 |  |

**Min. |DCAxy| of the daughters from primary vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.040000 |  |
| 8 | minimal | 0.050000 |  |
| 9 | minimal | 0.060000 |  |

**Min. number of TPC clusters of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 70.000000 |  |
| 10 | minimal | 80.000000 |  |
| 11 | minimal | 90.000000 |  |

**TPC Pion PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 12 | minimal | 4.000000 |  |
| 13 | minimal | 3.000000 |  |

**TPC Proton PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 14 | minimal | 4.000000 |  |
| 15 | minimal | 3.000000 |  |

**TOF Pion PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 16 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 17 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 18 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

**TOF Proton PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 19 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 20 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 21 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

**Sel8**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 0 | optional | 1.000000 |  |

**RCT flags ok**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 | label = CBT_hadronPID; useZdc = 0; treatLimitedAcceptanceAsBad = 0 |

**No same bunch pileup**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 1 | optional | 1.000000 |  |

**Is vertex ITS TPC**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 2 | optional | 1.000000 |  |

**Is good zvtx FT0 vs PV**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 3 | optional | 1.000000 |  |

**No collision in time range narrow**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 4 | optional | 1.000000 |  |

**No collision in time range strict**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 5 | optional | 1.000000 |  |

**No collision in time range standard**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 6 | optional | 1.000000 |  |

**No collision in ROF strict**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 7 | optional | 1.000000 |  |

**No collision in ROF standard**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 8 | optional | 1.000000 |  |

**No high mult collisions in previous ROF**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 9 | optional | 1.000000 |  |

**Is good ITS layer 3**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 10 | optional | 1.000000 |  |

**Is good ITS layer 0-3**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 11 | optional | 1.000000 |  |

**Is good ITS layer all**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 12 | optional | 1.000000 |  |

**Minimum Sphericity**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.000000 |  |
| 13 | minimal | 0.700000 |  |

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

**Min. CPA (cosine pointing angle)**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.988000 |  |
| 0 | minimal | 0.990000 |  |
| 1 | minimal | 0.992000 |  |

**Max. DCA of the daughters at decay vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.500000 |  |
| 2 | minimal | 1.200000 |  |
| 3 | minimal | 1.000000 |  |

**Max. distance of decay vertex in x,y,z**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Min. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.200000 |  |
| 4 | minimal | 0.300000 |  |
| 5 | minimal | 0.500000 |  |

**Max. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Max. absolute pseudo rapidity of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.830000 |  |
| 6 | minimal | 0.800000 |  |
| 7 | minimal | 0.770000 |  |

**Min. |DCAxy| of the daughters from primary vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.040000 |  |
| 8 | minimal | 0.050000 |  |
| 9 | minimal | 0.060000 |  |

**Min. number of TPC clusters of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 70.000000 |  |
| 10 | minimal | 80.000000 |  |
| 11 | minimal | 90.000000 |  |

**TPC Pion PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 12 | minimal | 4.000000 |  |
| 13 | minimal | 3.000000 |  |

**TPC Pion PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 14 | minimal | 4.000000 |  |
| 15 | minimal | 3.000000 |  |

**TOF Pion PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 16 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 17 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 18 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

**Min. CPA (cosine pointing angle)**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.988000 |  |
| 0 | minimal | 0.990000 |  |
| 1 | minimal | 0.992000 |  |

**Max. DCA of the daughters at decay vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.500000 |  |
| 2 | minimal | 1.200000 |  |
| 3 | minimal | 1.000000 |  |

**Max. distance of decay vertex in x,y,z**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Min. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.200000 |  |
| 4 | minimal | 0.300000 |  |
| 5 | minimal | 0.500000 |  |

**Max. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**Max. absolute pseudo rapidity of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.830000 |  |
| 6 | minimal | 0.800000 |  |
| 7 | minimal | 0.770000 |  |

**Min. |DCAxy| of the daughters from primary vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.040000 |  |
| 8 | minimal | 0.050000 |  |
| 9 | minimal | 0.060000 |  |

**Min. number of TPC clusters of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 70.000000 |  |
| 10 | minimal | 80.000000 |  |
| 11 | minimal | 90.000000 |  |

**TPC Proton PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 12 | minimal | 4.000000 |  |
| 13 | minimal | 3.000000 |  |

**TPC Pion PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 14 | minimal | 4.000000 |  |
| 15 | minimal | 3.000000 |  |

**TOF Proton PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 16 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 17 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 18 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

**TOF Pion PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 19 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 20 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 21 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

**Cascade CPA Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.98 |  |
| 0 | minimal | 0.9947 |  |

**Cascade DCA Daughters Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.600000 |  |
| 1 | minimal | 0.500000 |  |
| 2 | minimal | 0.250000 |  |

**Cascade Transverse Radius Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.800000 |  |
| 3 | minimal | 1.100000 |  |

**Lambda CPA Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.970000 |  |
| 4 | minimal | 0.980000 |  |
| 5 | minimal | 0.987600 |  |

**Lambda DCA Daughter Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 6 | minimal | 0.600000 |  |
| 7 | minimal | 0.500000 |  |

**Lambda Transverse Radius Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.400000 |  |
| 8 | minimal | 2.500000 |  |

**Lambda DCA to PV Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.020000 |  |
| 9 | minimal | 0.030000 |  |
| 10 | minimal | 0.040000 |  |

**Daughter Abs Eta Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.830000 |  |
| 11 | minimal | 0.800000 |  |
| 12 | minimal | 0.770000 |  |

**Daughter TPC Clusters Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 70.000000 |  |
| 13 | minimal | 80.000000 |  |
| 14 | minimal | 90.000000 |  |

**Daughter |DCAxy| Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.040000 |  |
| 15 | minimal | 0.050000 |  |
| 16 | minimal | 0.060000 |  |

**Bachelor TPC Kaon PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 17 | minimal | 4.000000 |  |
| 18 | minimal | 3.000000 |  |

**Bachelor TOF Kaon PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 19 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 20 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 21 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

**Positive Daughter TPC PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 22 | minimal | 4.000000 |  |
| 23 | minimal | 3.000000 |  |

**Negative Daughter TPC PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 24 | minimal | 4.000000 |  |
| 25 | minimal | 3.000000 |  |

**Positive Daughter TOF PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 26 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 27 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 28 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

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

**Min. CPA (cosine pointing angle)**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.850000 |  |
| 0 | minimal | 0.900000 |  |
| 1 | minimal | 0.950000 |  |

**Max. |DCAxy| to PV**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 999999995904.000000 |  |

**Max. |DCAz| to PV**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 999999995904.000000 |  |

**Max. chi2/NDF of conversion vertex**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 999999995904.000000 |  |

**Min. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.000000 |  |
| 2 | minimal | 5.000000 |  |
| 3 | minimal | 10.000000 |  |

**Max. transverse radius**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 180.000000 |  |
| 4 | minimal | 160.000000 |  |
| 5 | minimal | 120.000000 |  |

**Max. absolute pseudorapidity of daughters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.950000 |  |
| 6 | minimal | 0.900000 |  |
| 7 | minimal | 0.850000 |  |

**TPC electron PID for positive daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| 8 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| 9 | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |

**TPC electron PID for negative daughter**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 3.500000 | keepDaughtersWithoutTpc = 1 |
| 10 | minimal | 3.000000 | keepDaughtersWithoutTpc = 1 |
| 11 | minimal | 2.500000 | keepDaughtersWithoutTpc = 1 |

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

**kinkTopoDcaMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 2.000000 |  |

**transRadMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 19.600000 |  |

**transRadMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**dauAbsEtaMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 0 | minimal | 0.900000 |  |
| 1 | minimal | 0.800000 |  |

**dauDcaPvMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.100000 |  |

**mothDcaPvMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.025000 |  |
| 2 | minimal | 0.020000 |  |

**chaDauTpcPion**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 3 | minimal | 4.000000 |  |

**alphaAPMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | -1.000000 |  |

**alphaAPMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.000000 |  |

**qtAPMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.145000 |  |
| 4 | minimal | 0.150000 |  |
| 5 | minimal | 0.155000 |  |

**qtAPMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.210000 |  |
| 6 | minimal | 0.205000 |  |
| 7 | minimal | 0.200000 |  |

**cosPointingAngleMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.988000 |  |
| 8 | minimal | 0.990000 |  |
| 9 | minimal | 0.992000 |  |

**ptOriginalMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.200000 |  |
| 10 | minimal | 1.400000 |  |
| 11 | minimal | 1.600000 |  |
| 12 | minimal | 1.800000 |  |

**ptOriginalMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 10.000000 |  |

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

**kinkTopoDcaMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 2.000000 |  |

**transRadMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 19.600000 |  |

**transRadMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 100.000000 |  |

**dauAbsEtaMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 0 | minimal | 0.900000 |  |
| 1 | minimal | 0.800000 |  |

**dauDcaPvMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.100000 |  |

**mothDcaPvMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.025000 |  |
| 2 | minimal | 0.020000 |  |

**chaDauTpcProton**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 3 | minimal | 4.000000 |  |

**chaDauTofProton**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | neutral | 4.500000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 4 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 5 | neutral | 3.500000 | requireTof = 0; keepTracksWithoutTof = 1 |

**alphaAPMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.000000 |  |

**alphaAPMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |

**qtAPMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.100000 |  |
| 6 | minimal | 0.125000 |  |
| 7 | minimal | 0.150000 |  |

**qtAPMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.220000 |  |
| 8 | minimal | 0.210000 |  |
| 9 | minimal | 0.200000 |  |

**cosPointingAngleMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.988000 |  |
| 10 | minimal | 0.990000 |  |
| 11 | minimal | 0.992000 |  |

**ptOriginalMin**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.200000 |  |
| 12 | minimal | 1.400000 |  |
| 13 | minimal | 1.600000 |  |
| 14 | minimal | 1.800000 |  |

**ptOriginalMax**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 10.000000 |  |

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

**Min. number of TPC clusters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 90.000000 |  |
| 0 | minimal | 100.000000 |  |
| 1 | minimal | 110.000000 |  |
| 2 | minimal | 120.000000 |  |

**Min. number of crossed TPC rows**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 80.000000 |  |
| 3 | minimal | 90.000000 |  |
| 4 | minimal | 100.000000 |  |
| 5 | minimal | 110.000000 |  |

**Min. fraction of TPC clusters over TPC crossed rows**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.000000 |  |

**Max. number of shared TPC clusters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 160.000000 |  |

**Max. fractions of shared TPC clusters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 6 | minimal | 0.800000 |  |
| 7 | minimal | 0.400000 |  |

**Min. number of ITS clusters**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 8 | minimal | 6.000000 |  |
| 9 | minimal | 7.000000 |  |

**Min. number of ITS clusters in the inner barrel**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 10 | minimal | 3.000000 |  |

**Max. |DCA_xy| (cm) as a function of pT**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.1 |  |
| 11 | minimal | 0.004+0.013*pow(x,-1) |  |

**Max. |DCA_z| (cm) as a function of pT**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.2 |  |
| 12 | minimal | 0.004+0.013*pow(x,-1) |  |

**ITS He3 PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 13 | optional | -1.5;3.40282e+38 |  |
| 14 | optional | -1.3;3.40282e+38 |  |

**TPC Pion PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 15 | optional | -3.5;3 |  |
| 16 | optional | -3;3 |  |
| 17 | optional | -2.5;2.5 |  |

**TPC Kaon PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 18 | optional | -3.5;3 |  |
| 19 | optional | -3;3 |  |
| 20 | optional | -2.5;2.5 |  |

**TPC Proton PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 21 | optional | -3.5;3 |  |
| 22 | optional | -3;3 |  |
| 23 | optional | -2.5;2.5 |  |

**TPC He3 PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 24 | optional | -2.5;2.5 |  |
| 25 | optional | -2;2 |  |
| 26 | optional | -1.5;1.5 |  |

**TPC+ITS Pion PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 27 | optional | 3.500000 |  |
| 28 | optional | 3.000000 |  |
| 29 | optional | 2.500000 |  |

**TPC+ITS Kaon PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 30 | optional | 3.500000 |  |
| 31 | optional | 3.000000 |  |
| 32 | optional | 2.500000 |  |

**TPC+ITS Proton PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 33 | optional | 3.500000 |  |
| 34 | optional | 3.000000 |  |
| 35 | optional | 2.500000 |  |

**TPC+ITS Deuteron PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 36 | optional | 3.500000 |  |
| 37 | optional | 3.000000 |  |
| 38 | optional | 2.500000 |  |

**TPC+ITS Triton PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 39 | optional | 3.500000 |  |
| 40 | optional | 3.000000 |  |
| 41 | optional | 2.500000 |  |

**TPC+TOF Pion PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 42 | optional | 3.500000 | minMomTofPion = 0.500000 |
| 43 | optional | 3.000000 | minMomTofPion = 0.500000 |
| 44 | optional | 2.500000 | minMomTofPion = 0.500000 |

**TPC+TOF Kaon PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 45 | optional | 3.500000 | minMomTofKaon = 0.400000 |
| 46 | optional | 3.000000 | minMomTofKaon = 0.400000 |
| 47 | optional | 2.500000 | minMomTofKaon = 0.400000 |

**TPC+TOF Proton PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 48 | optional | 3.500000 | minMomTofProton = 0.750000 |
| 49 | optional | 3.000000 | minMomTofProton = 0.750000 |
| 50 | optional | 2.500000 | minMomTofProton = 0.750000 |

**TPC+TOF Deuteron PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 51 | optional | 3.500000 | minMomTofDeuteron = 1.200000 |
| 52 | optional | 3.000000 | minMomTofDeuteron = 1.200000 |
| 53 | optional | 2.500000 | minMomTofDeuteron = 1.200000 |

**TPC+TOF Triton PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 54 | optional | 3.000000 | minMomTofTriton = 2.000000 |
| 55 | optional | 2.500000 | minMomTofTriton = 2.000000 |

**TPC+TOF He3 PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 56 | optional | 3.500000 | minMomTofHelium = 99.000000 |
| 57 | optional | 3.000000 | minMomTofHelium = 99.000000 |
| 58 | optional | 2.500000 | minMomTofHelium = 99.000000 |

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

**Cascade CPA Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.98 |  |
| 0 | minimal | 0.9947 |  |

**Cascade DCA Daughters Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.600000 |  |
| 1 | minimal | 0.500000 |  |
| 2 | minimal | 0.250000 |  |

**Cascade Transverse Radius Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.800000 |  |
| 3 | minimal | 1.100000 |  |

**Lambda CPA Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.970000 |  |
| 4 | minimal | 0.980000 |  |
| 5 | minimal | 0.987600 |  |

**Lambda DCA Daughter Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.000000 |  |
| 6 | minimal | 0.600000 |  |
| 7 | minimal | 0.500000 |  |

**Lambda Transverse Radius Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 1.400000 |  |
| 8 | minimal | 2.500000 |  |

**Lambda DCA to PV Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.020000 |  |
| 9 | minimal | 0.030000 |  |
| 10 | minimal | 0.040000 |  |

**Daughter Abs Eta Max**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.830000 |  |
| 11 | minimal | 0.800000 |  |
| 12 | minimal | 0.770000 |  |

**Daughter TPC Clusters Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 70.000000 |  |
| 13 | minimal | 80.000000 |  |
| 14 | minimal | 90.000000 |  |

**Daughter |DCAxy| Min**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 0.040000 |  |
| 15 | minimal | 0.050000 |  |
| 16 | minimal | 0.060000 |  |

**Bachelor TPC Pion PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 17 | minimal | 4.000000 |  |
| 18 | minimal | 3.000000 |  |

**Bachelor TOF Pion PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 19 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 20 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 21 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

**Positive Daughter TPC PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 22 | minimal | 4.000000 |  |
| 23 | minimal | 3.000000 |  |

**Negative Daughter TPC PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| always applied | minimal | 5.000000 |  |
| 24 | minimal | 4.000000 |  |
| 25 | minimal | 3.000000 |  |

**Positive Daughter TOF PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 26 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 27 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 28 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |

**Negative Daughter TOF PID**

| Bit | Type | Value | Comment |
| --- | --- | --- | --- |
| 29 | neutral | 5.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 30 | neutral | 4.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
| 31 | neutral | 3.000000 | requireTof = 0; keepTracksWithoutTof = 1 |
