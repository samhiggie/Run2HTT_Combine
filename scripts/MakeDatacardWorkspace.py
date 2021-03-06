#!/usr/bin/env python
import os
import argparse
import ROOT
import logging
import datetime
import string
import random
import CombineHarvester.Run2HTT_Combine.CategoryConfigurations as cfg
from CombineHarvester.Run2HTT_Combine.EmbeddedConfiguration import EmbeddedConfiguration as embedded_cfg
from CombineHarvester.Run2HTT_Combine.SplitUncertainty import UncertaintySplitter
from CombineHarvester.Run2HTT_Combine.ThreadManager import ThreadManager

def RandomStringTag(size=6,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

parser = argparse.ArgumentParser(description="Centralized script for running combine fits on dynamically changing analysis categories.")
parser.add_argument('--years',nargs="+",choices=['2016','2017','2018'],help="Specify the year(s) to run the fit for",required=True)
parser.add_argument('--channels',nargs="+",choices=['mt','et','tt','em'],help="specify the channels to create data cards for",required=True)
parser.add_argument('--NoDatacards',help="Don't use combine harvester to collect the histograms from root files and make text datacards",default=False,action="store_true")
parser.add_argument('--RunShapeless',help="Run combine model without using any shape uncertainties",action="store_true")
parser.add_argument('--RunWithBinByBin',help="Run combine model without using bin-by-bin uncertainties",action="store_true")
parser.add_argument('--RunWithoutAutoMCStats',help="Run with auto mc stats command appended to data cards",action="store_true")
parser.add_argument('--MakeStage0',help="Run using only signals",action="store_true")
parser.add_argument('--MakeStage12',help="Make the workspace for all 1.2 categories",action="store_true")
parser.add_argument('--MakeStage12Merged',help="Run using only signals",action="store_true")
parser.add_argument('--Timeout', help="Trigger timeout as conditions on fits (prevents infinitely running fits)", action="store_true")
parser.add_argument('--TimeoutTime',nargs='?',help="Time allotted before a timeout (linux timeout syntax)",default="180s")
parser.add_argument('--SplitUncertainties', help="Create groups for helping to split the measurements",action="store_true")
parser.add_argument('--SplitInclusive',help="Split the inclusive measurements into component pieces. REQUIRES --SplitUncertainties",action="store_true")
parser.add_argument('--SplitSignals',help="Split signal measurements into component pieces. REQUIRES --SplitUncertainties",action="store_true")
parser.add_argument('--SplitSTXS',help="Split STXS measurements into component pieces. REQUIRES --SplitUncertainties",action="store_true")
parser.add_argument('--DecorrelateForMe',help="Run the decorrelator as part of the overall run. Looks for a datacard named smh<year><channel>_nocorrelation.root",action="store_true")
print("Parsing command line arguments.")
args = parser.parse_args() 

if (args.SplitInclusive or args.SplitSignals or args.SplitSTXS) and not (args.SplitUncertainties):
    parser.error("Tried to split a measurement without calling --SplitUncertainties!")

DateTag = datetime.datetime.now().strftime("%d%m%y_")+RandomStringTag()
print ''
print "*********************************************"
print("This session is run under tag: "+DateTag)
print "*********************************************"
print ''
#check if we have an output directory

if not os.path.isdir(os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output"):
    os.mkdir(os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output")
OutputDir = os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output/Output_"+DateTag+"/"
os.mkdir(OutputDir)

logging.basicConfig(filename=OutputDir+"CombineHistory_"+DateTag+".log",filemode="w",level=logging.INFO,format='%(asctime)s %(message)s')

DataCardCreationCommand = ""

ChannelCards = []

for year in args.years:    
    for channel in args.channels:

        if args.DecorrelateForMe:
            AddShapeCommand="python scripts/PrepDecorrelatedCard.py --year "+year+" --DataCard ../../auxiliaries/shapes/smh"+year+channel+"_nocorrelation.root --OutputFileName ../../auxiliaries/shapes/smh"+year+channel+".root "
            if channel=="et" or channel=="em":
                AddShapeCommand+="--TrimYears "
            print("Duplicating shapes for year correlations")
            logging.info("Shape duplication command:")
            logging.info('\n\n'+AddShapeCommand+'\n')
            os.system(AddShapeCommand)

        DataCardCreationCommand="SMHTT"+year
        DataCardCreationCommand+="_"+channel+" "+OutputDir
        if args.RunShapeless:
            DataCardCreationCommand+=" -s"
        if not args.RunWithBinByBin:
            DataCardCreationCommand+=" -b"
        #if args.RunEmbeddedLess:
        if not embedded_cfg[str(year)+str(channel)]: #load from config. If false, run embedded less
            DataCardCreationCommand+=" -e"
        if args.notRunInclusiveggH:
            DataCardCreationCommand+=" -g"
        if args.RunInclusiveqqH:
            DataCardCreationCommand+=" -q"
        DataCardCreationCommand+=" --Categories"
        for Category in cfg.Categories[channel]:
            DataCardCreationCommand+=" "+Category
        print("Creating data cards")
        logging.info("Data Card Creation Command:")
        logging.info('\n\n'+DataCardCreationCommand+'\n')
        os.system(DataCardCreationCommand)        
        

#cobmine all cards together
#we can't do this the old way of first mashing all channels together and then mashing those into a final card
#messes with paths somewhere
#we have to do this in one fell swoop.
if not args.NoDatacards:
    CombinedCardName = OutputDir+"FinalCard_"+DateTag+".txt"
    CombinedCardRootName = OutputDir+"FinalCard_"+DateTag+".root"
    CardCombiningCommand = "combineCards.py"
    if args.SplitUncertainties:
        Splitter = UncertaintySplitter()
    for year in args.years:
        for channel in args.channels:
            CardNum = 1
            TheFile = ROOT.TFile(os.environ['CMSSW_BASE']+"/src/auxiliaries/shapes/smh"+year+channel+".root")
            for Directory in TheFile.GetListOfKeys():
                if Directory.GetName() in cfg.Categories[channel]:
                    if not args.RunWithoutAutoMCStats:
                        CardFile = open(OutputDir+"smh"+year+"_"+channel+"_"+str(CardNum)+"_13TeV_.txt","a+")
                        CardFile.write("* autoMCStats 0.0\n")
                        CardFile.close()                
                    if args.SplitUncertainties:                    
                        Splitter.FindAndTagGroups(OutputDir+"smh"+year+"_"+channel+"_"+str(CardNum)+"_13TeV_.txt")
                    CardCombiningCommand += " "+Directory.GetName()+"_"+year+"="+OutputDir+"smh"+year+"_"+channel+"_"+str(CardNum)+"_13TeV_.txt "
                    CardNum+=1

    CardCombiningCommand+= " > "+CombinedCardName
    logging.info("Final Card Combining Command:")
    logging.info('\n\n'+CardCombiningCommand+'\n')
    os.system(CardCombiningCommand)


if args.MakeStage0:
    #per signal card workspace set up
    print("Setting up per signal workspace")
    PerSignalName = OutputDir+"Workspace_per_signal_breakdown_cmb_"+DateTag+".root"
    PerSignalWorkspaceCommand = " combineTool.py -M T2W -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --parallel 12"
    PerSignalWorkspaceCommand+= "--PO 'map=.*/ggH.*htt125.*:r_ggH[1,-25,25]' "
    PerSignalWorkspaceCommand+= "--PO 'map=.*/qqH.*htt125.*:r_qqH[1,-25,25]' "
    PerSignalWorkspaceCommand+= "--PO 'map=.*/WH_htt125.*:r_WH[1,-25,25]' "
    PerSignalWorkspaceCommand+= "--PO 'map=.*/ZH_htt125.*:r_ZH[1,-25,25]' "
    PerSignalWorkspaceCommand+= " -i "+OutputDir+"smh*_*_*_13TeV_.txt"+" -o "+PerSignalName+" -m 125"

    logging.info("Per Signal Workspace Command:")
    logging.info('\n\n'+PerSignalWorkspaceCommand+'\n')
    os.system(PerSignalWorkspaceCommand)


#per category
"""
if not args.DisableCategoryFits:
    print("Setting up per category command.")
    PerCategoryName = OutputDir+"workspace_per_cat_breakdown_cmb_"+DateTag+".root"
    PerCategoryWorkspaceCommand = "text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel "
    CategorySignalNames=[]
    for Directory in TheFile.GetListOfKeys():
        CategorySignalNames.append("r"+Directory.GetName()[2:])
        PerCategoryWorkspaceCommand += "--PO 'map=.*"+Directory.GetName()+".*/.*_htt.*:"+"r"+Directory.GetName()[2:]+"[1,-25,25]' "
    PerCategoryWorkspaceCommand+=CombinedCardName+" -o "+PerCategoryName+" -m 125"

    logging.info("Per Category Workspace Command: ")
    logging.info('\n\n'+PerCategoryWorkspaceCommand+'\n')
    os.system(PerCategoryWorkspaceCommand)
"""

#Set up the possible STXS bins list
if (args.MakeStage12):
    print("Setting up STXS commands")
    STXSBins = ["ggH_PTH_0_200_0J_PTH_10_200_htt125",
                "ggH_PTH_0_200_0J_PTH_0_10_htt125",
                "ggH_PTH_0_200_1J_PTH_0_60_htt125",
                "ggH_PTH_0_200_1J_PTH_60_120_htt125",
                "ggH_PTH_0_200_1J_PTH_120_200_htt125",
                "ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125",		   
                "ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125",		   
                "ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125",		   
                "ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125",		   
                "ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125",
                "ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125",		   
                "ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125",		   
                "ggH_FWDH_htt125",
                "ggH_PTH_200_300_htt125",
                "ggH_PTH_300_450_htt125",
                "ggH_PTH_450_650_htt125",
                "ggH_PTH_GE650_htt125",
                "qqH_0J_htt125",
                "qqH_1J_htt125",
                "qqH_GE2J_MJJ_0_60_htt125",
                "qqH_GE2J_MJJ_60_120_htt125",
                "qqH_GE2J_MJJ_120_350_htt125",
                "qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125",
                "qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125",
                "qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125",
                "qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125",
                "qqH_GE2J_MJJ_GE350_PTH_GE200_htt125",
                "qqH_FWDH_htt125"]
    PerSTXSBinsWorkSpaceCommand = "combineTool.py -M T2W -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --parallel 12 "
    STXSSignalNames=[]
    for Bin in STXSBins:
        STXSSignalNames.append("r_"+Bin)
        PerSTXSBinsWorkSpaceCommand += "--PO 'map=.*/"+Bin+":"+"r_"+Bin+"[1,-25,25]' "
    PerSTXSBinsWorkSpaceCommand += " -i "+OutputDir+"smh*_*_*_13TeV_.txt"+" -o "+PerSTXSName+" -m 125"

    logging.info("Per STXS Bins Work Space Command")
    logging.info('\n\n'+PerSTXSBinsWorkSpaceCommand+'\n')
    os.system(PerSTXSBinsWorkSpaceCommand+" | tee -a "+outputLoggingFile)

if (args.MakeStage12Merged):
    #add in the merged ones
    PerMergedBinName = OutputDir+"workspace_per_Merged_breakdown_cmb_"+DateTag+".root"
    PerMergedBinWorkspaceCommand = " combineTool.py -M T2W -o workspace_"+DateTag+"_stage1.2_merged.root -i "+OutputDir+"smh*_*_*_13TeV_.txt"+" --parallel 12 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125"
    MergedSignalNames=[]
    #qqH, less than 2 Jets
    MergedSignalNames.append("qqH_LT2J")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_0J_htt125:r_qqH_LT2J[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_1J_htt125:r_qqH_LT2J[1,-25,25]' "
    #qqH mjj 0-350
    MergedSignalNames.append("qqH_GE2J_MJJ_0_350")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_0_60_htt125:r_qqH_GE2J_MJJ_0_350[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_60_120_htt125:r_qqH_GE2J_MJJ_0_350[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_120_350_htt125:r_qqH_GE2J_MJJ_0_350[1,-25,25]' "
    #qqH mjj 350-700, all PtH
    MergedSignalNames.append("qqH_GE2J_MJJ_350_700_PTH_0_200")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125:r_qqH_GE2J_MJJ_350_700_PTH_0_200[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125:r_qqH_GE2J_MJJ_350_700_PTH_0_200[1,-25,25]' "
    #qqH mjj 700+, all PtH
    MergedSignalNames.append("qqH_GE2J_MJJ_GE700_PTH_0_200")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125:r_qqH_GE2J_MJJ_GE700_PTH_0_200[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125:r_qqH_GE2J_MJJ_GE700_PTH_0_200[1,-25,25]' "
    #ggH 2Jets, mjj 350+
    MergedSignalNames.append("ggH_PTH_0_200_GE2J_MJJ_GE350")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125:r_ggH_PTH_0_200_GE2J_MJJ_GE350[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125:r_ggH_PTH_0_200_GE2J_MJJ_GE350[1,-25,25]' " 
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125:r_ggH_PTH_0_200_GE2J_MJJ_GE350[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125:r_ggH_PTH_0_200_GE2J_MJJ_GE350[1,-25,25]' "     
    ##ggH, PTH 200+
    MergedSignalNames.append("ggH_PTH_GE200")
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_200_300_htt125:r_ggH_PTH_GE200[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_300_450_htt125:r_ggH_PTH_GE200[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_450_600_htt125:r_ggH_PTH_GE200[1,-25,25]' "
    PerMergedBinWorkSpaceCommand += "--PO 'map=.*/ggH_PTH_GE650_htt125:r_ggH_PTH_GE200[1,-25,25]' "


    logging.info("Per Merged Bin Work Space Command")
    logging.info('\n\n'+PerMergedBinWorkSpaceCommand+'\n')
    os.system(PerMergedBinWorkSpaceCommand)

TextWorkspaceCommand = "combineTool.py -M T2W --parallel 12 "+" -i "+OutputDir+"smh*_*_*_13TeV_.txt"+" -o "+CombinedCardRootName+" -m 125"
logging.info("Text 2 Worskpace Command:")
logging.info('\n\n'+TextWorkspaceCommand+'\n')
os.system(TextWorkspaceCommand+" | tee -a "+outputLoggingFile)
