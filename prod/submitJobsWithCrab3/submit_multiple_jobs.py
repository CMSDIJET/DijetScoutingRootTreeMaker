##################################################################
########   TO RUN THIS: python submit_multiple_jobs.py
########   DO NOT DO: crab submit submit_multiple_jobs.py
########
########   From https://github.com/alefisico/RUNA
##################################################################

from CRABClient.UserUtilities import config
from httplib import HTTPException
from multiprocessing import Process
from CRABAPI.RawCommand import crabCommand
import os


def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException, hte:
        print 'Cannot execute command'
        print hte.headers


if __name__ == '__main__':
    gg_samples = [
        '/RSGravitonToGluonGluon_kMpl01_M_500_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_750_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-Asympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_2000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_3000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_5000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_6000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_7000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_8000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToGluonGluon_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'
        ]
    qq_samples = [
        '/RSGravitonToQuarkQuark_kMpl01_M_500_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_750_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-Asympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_2000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_3000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_5000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_6000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_7000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_8000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/RSGravitonToQuarkQuark_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM']
    gq_samples = [
        '/QstarToJJ_M_500_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        #QstarToJJ_M_750
        '/QstarToJJ_M_1000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_2000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_3000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_4000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_5000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_6000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_7000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_8000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM',
        '/QstarToJJ_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'
        ]
    Samples = []
    Samples += gg_samples
    Samples += qq_samples
    Samples += gq_samples

    CMSSW_BASE = os.environ['CMSSW_BASE']
    mc_campaign = "Spring15_25ns"
    JEC = "Summer15_25nsV7"

    config = config()

    config.General.transferOutputs = True
    config.General.transferLogs = True
    config.General.requestName = ''
    config.General.workArea = 'jobs'

    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = '{0}/src/CMSDIJET/DijetScoutingRootTreeMaker/prod/flat-signal_cfg.py'.format(
        CMSSW_BASE)
    config.JobType.outputFiles = ['dijetscouting_bigtree.root']

    config.Data.inputDataset = ''
    config.Data.splitting = 'LumiBased'
    config.Data.unitsPerJob = 10000
    config.Data.publication = False
    config.Data.ignoreLocality = True
    config.Data.outLFNDirBase = '/store/group/phys_exotica/dijet/Dijet13TeVScouting/rootTrees_big/MC/signal/{0}_JEC_{1}/'.format(
        mc_campaign, JEC)

    config.Site.storageSite = 'T2_CH_CERN'

    for dataset in Samples:
        parts = dataset.split('/')
        name = "{0}__{1}__{2}".format(parts[1], parts[2], parts[3])
        config.General.requestName = parts[1]
        output_name = '{0}_JEC_{1}.root'.format(name, JEC)
        config.JobType.pyCfgParams = ['outputFile={0}'.format(output_name)]
        config.JobType.outputFiles = [output_name]
        config.Data.inputDataset = dataset
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
