import ROOT

def AddYearsTogether(collection,channel,category,prefitOrPostfit):
    for dictType in ['Full','Slimmed','Signals','Data']:        
        collection[channel]['Run2'][category][prefitOrPostfit][dictType] = {}
        for histogram in collection[channel]['2016'][category][prefitOrPostfit][dictType]:            
            #try:
            Run2Histo = collection[channel]['2016'][category][prefitOrPostfit][dictType][histogram].Clone()
            Run2Histo.Add(collection[channel]['2017'][category][prefitOrPostfit][dictType][histogram])
            Run2Histo.Add(collection[channel]['2018'][category][prefitOrPostfit][dictType][histogram])
            collection[channel]['Run2'][category][prefitOrPostfit][dictType][histogram] = Run2Histo
            #except:
            #    print("Problem creating full run2 histo for "+channel+" "+category+" "+prefitOrPostfit+" "+dictType+" "+histogram)

def PerformAllAdditions(collection):
    #we'll also need a full run 2 dictionary. Let's make that.
    for channel in collection:
        collection[channel]['Run2'] = {}
        for category in collection[channel]['2016']:
            collection[channel]['Run2'][category] = {}
            for prefitOrPostfit in ['prefit','postfit']:
                collection[channel]['Run2'][category][prefitOrPostfit] = {}            
                AddYearsTogether(collection,channel,category,prefitOrPostfit)
