import ROOT

stackOrder = ['jetFakes','Other','Top','ZL','ZT']
emuStackOrder = ['QCD','W','Other','Top','ZL','ZT']

def CreateStack(histogramDictionary):    
    if not 'jetFakes' in histogramDictionary:
        theStackOrder = emuStackOrder
    else:
        theStackOrder = stackOrder
    theStack = ROOT.THStack("Predictions","Predictions")
    for entry in theStackOrder:
        try:
            theStack.Add(histogramDictionary[entry],"HIST")
        except KeyError:
            print("Couldn't stack histogram: "+entry)
    return theStack
