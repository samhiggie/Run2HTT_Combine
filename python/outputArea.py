#!/usr/bin/env python

#Andrew Loeliger
#Just a replacement for some of the more common output creating features of RunCombineFits.py
#for eventual use between both RunCombineFits.py and the differential set-up and running script

import datetime
import string
import random
import os

def RandomStringTag(size=6,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def PrintSessionInfo(dateTag):
    print ''
    print "*********************************************"
    print("This session is run under tag: "+dateTag)
    print "*********************************************"
    print ''

def PrepareNewOutputArea():
    dateTag = datetime.datetime.now().strftime("%d%m%y_")+RandomStringTag()
    PrintSessionInfo(dateTag)
    if not os.path.isdir(os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output"):
        os.mkdir(os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output")
    outputDir = os.environ['CMSSW_BASE']+"/src/CombineHarvester/Run2HTT_Combine/HTT_Output/Output_"+dateTag+"/"
    os.mkdir(outputDir)
    return dateTag,outputDir
