import ROOT

def ApplyDataSettings(dataHistogram):
    dataHistogram.SetMarkerStyle(20)
    #dataHistogram.SetLineColor(ROOT.kBlack)    
    dataHistogram.SetBinErrorOption(ROOT.TH1.kPoisson)    
