import ROOT
import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for removing negative bins from shapes")
    parser.add_argument("FileIn",help="File to remove the negative bins from")
    
    args = parser.parse_args()
    
    TheFile = ROOT.TFile(args.FileIn,"UPDATE")

    for i in range(TheFile.GetListOfKeys().GetEntries()):
        TheDirectory = TheFile.Get(TheFile.GetListOfKeys().At(i).GetName())                                   
        #print(TheDirectory.GetName())
        #print(TheDirectory.GetListOfKeys().GetEntries())
        #print(range(10))
        #print(range(TheDirectory.GetListOfKeys().GetEntries()))
        #for j in range(TheDirectory.GetListOfKeys().GetEntries()):            
        numEntries = TheDirectory.GetListOfKeys().GetEntries()
        #for j in range(40):            
        j=0
        while j < numEntries:
            #print(j)
            HasNegativeBins=False            
            #TheHisto = TheDirectory.Get(TheDirectory.GetListOfKeys().At(j).GetName()).Clone()
            TheHisto = TheDirectory.Get(TheDirectory.GetListOfKeys().At(j).GetName())
            #print(TheDirectory.GetListOfKeys().At(j).GetName())
            #raw_input()
            for k in range(1,TheHisto.GetNbinsX()):
                if TheHisto.GetBinContent(k) < 0.0:
                    HasNegativeBins=True
                    TheHisto.SetBinContent(k,0.0)
            if HasNegativeBins:     
                j+=2
                numEntries+=1
                #print("!")
                TheDirectory.cd()
                TheHisto.Write()                                
            else:
                j+=1
