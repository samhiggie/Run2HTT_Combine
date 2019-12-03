import ROOT

stackOrder = ['jetFakes','Other','Top','ZL','ZT']

def CreateStack(histogramDictionary):
    theStack = ROOT.THStack("Predictions","Predictions")
    for entry in stackOrder:
        try:
            theStack.Add(histogramDictionary[entry],"HIST")
        except KeyError:
            print("Couldn't stack histogram: "+entry)
    return theStack
