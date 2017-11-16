DijetScoutingRootTreeMaker
==========================

Information: https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoDijet13TeV#Analysis_code_data_scouting_anal

To run over MC MINIAOD with Scouting content in 94x, setup release:

```
cmsrel CMSSW_9_4_0
cd CMSSW_9_4_0/src/
cmsenv
```

Clone and compile repository:

```
git clone https://github.com/CMSDIJET/DijetScoutingRootTreeMaker.git CMSDIJET/DijetScoutingRootTreeMaker
scram b -j4
```

Run with:

```
cd CMSDIJET/DijetScoutingRootTreeMaker/prod/
cmsRun flat-MC-calo_cfg.py local=True
```

Use the configuration file `flat-data-monitor_cfg.py` to run over the ParkingScoutingMonitor datasets.
Use the configuration file `flat-data-calo_cfg.py` to run over the CaloScouting datasets.
Use the configuration file `flat-MC-calo_cfg.py` to run over the MC MINIAOD with Scouting content datasets.


In order to keep running in 80x, setup release:

```
cmsrel CMSSW_8_0_10
cd CMSSW_8_0_10/src/
cmsenv
git clone -b branch_80x https://github.com/CMSDIJET/DijetScoutingRootTreeMaker.git CMSDIJET/DijetScoutingRootTreeMaker
scram b -j4
cd CMSDIJET/DijetScoutingRootTreeMaker/prod/
cmsRun flat-data_cfg.py local=True
```

In order to keep running in 74x replace the instructions above with:

```
cmsrel CMSSW_7_4_15
cd CMSSW_7_4_15/src
cmsenv
git clone https://github.com/CMSDIJET/DijetScoutingRootTreeMaker.git CMSDIJET/DijetScoutingRootTreeMaker
git fetch origin branch_74x:branch_74x
git checkout branch_74x
scram b -j4

cmsRun flat-data_cfg.py
```
