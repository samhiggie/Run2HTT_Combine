import ROOT
import os
import CombineHarvester.Run2HTT_Combine.CategoryConfigurations as CategoryConfigurations

#given the exact directory path we can try to retrive all plots we know and care about.
#takes as arguments a TDirectory
def RetrievePlotsFromDirectory(channel, directory):    
    jetFakes = directory.Get("jetFakes")
    if channel == 'em':        
        print("no jet fakes found, assuming this is an e mu channel")
        W = directory.Get("W")
        QCD = directory.Get("QCD")
    ZT = directory.Get("embedded")
    if channel == 'mt' or channel == 'tt':
        ZL = directory.Get("ZL")
    else:
        ZL = directory.Get("DYL")
    TTL = directory.Get("TTL")
    TTT = directory.Get("TTT")
    VVL = directory.Get("VVL")
    VVT = directory.Get("VVT")
    STL = directory.Get("STL")
    STT = directory.Get("STT")
    ggH = directory.Get("ggH_htt125")
    qqH = directory.Get("qqH_htt125")
    WH = directory.Get("WH_htt125")
    ZH = directory.Get("ZH_htt125")

    TT = TTL.Clone()
    TT.SetNameTitle("TT","TT")
    TT.Add(TTT)
    
    VV = VVL.Clone()
    VV.SetNameTitle("VV","VV")
    VV.Add(VVT)

    ST = STL.Clone()
    ST.SetNameTitle("ST","ST")
    ST.Add(STT)

    Top = TT.Clone()
    Top.SetNameTitle("Top","Top")
    Top.Add(ST)

    Higgs = ggH.Clone()
    Higgs.SetNameTitle("Higgs","Higgs")
    Higgs.Add(qqH)
    Higgs.Add(WH)
    Higgs.Add(ZH)

    Other = VV.Clone()
    Other.SetNameTitle("Other","Other")
    Other.Add(Higgs)    

    #create the Full histogram list
    fullDictionary = {        
        'ZT':ZT,
        'ZL':ZL,
        'TTL':TTL,
        'TTT':TTT,
        'VVL':VVL,
        'VVT':VVT,
        'STL':STL,
        'STT':STT,
        'ggH':ggH,
        'qqH':qqH,
        'WH':WH,
        'ZH':ZH,
        }
    slimmedDictionary = {        
        'ZT':ZT,
        'ZL':ZL,
        'Top':Top,        
        'Other':Other
        }
    if channel == 'em':
        fullDictionary['W'] = W
        fullDictionary['QCD'] = QCD
        slimmedDictionary['W'] = W
        slimmedDictionary['QCD'] = QCD
    else:
        fullDictionary['jetFakes'] = jetFakes
        slimmedDictionary['jetFakes'] = jetFakes

    signalDictionary = {
        'Higgs':Higgs,
        'ggH':ggH,
        'qqH':qqH,
        'WH':WH,
        'ZH':ZH,        
    }

    #create the slimmed histogram list with the plots common to most plotting schemes
    return {'Full':fullDictionary,'Slimmed':slimmedDictionary,'Signals':signalDictionary}

def RetrieveOriginalDatacardPath(channel,year):
    datacardPath = os.environ['CMSSW_BASE']+'/src/auxiliaries/shapes/'
    datacardName = 'smh'+year+channel+'.root'
    return datacardPath+datacardName

#retrieve all plots conforming to current category configuration specs.
#takes as arguments a list of channels from ['tt','mt','et','em']
#and a TFile or TDirectory.
#the years of the plot to be retrieved
def RetrievePlotsFromAllDirectories(channels,location,years,withYears = True):
    location.ls()
    histograms = {}
    for channel in channels:
        histograms[channel] = {}        
        for year in years:
            histograms[channel][year]={}
            for categoryName in CategoryConfigurations.Categories[channel]:
                histograms[channel][year][categoryName] = {}
                for prefitOrPostfit in ['prefit','postfit']:                    
                    directoryName = categoryName+'_'+year+'_'+prefitOrPostfit
                    candidateDirectory = location.Get(directoryName)
                    if candidateDirectory == None:
                        print("Could not load all histograms from the files because it was missing a directory: "+directoryName)
                        continue
                    else:
                        print("loading category: "+categoryName+" plots from : "+directoryName)
                        histograms[channel][year][categoryName][prefitOrPostfit] = RetrievePlotsFromDirectory(channel, candidateDirectory)                    
    return histograms
