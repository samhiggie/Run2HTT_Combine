import ROOT
import CombineHarvester.Run2HTT_Combine.CategoryConfigurations as catConfig
from rebinning import GetNSlices
from rebinning import standardSliceSetup

binsPerSlice = standardSliceSetup[len(standardSliceSetup)-1]

def CreateSliceLines(category,originalHistogram,pad):    
    nSlices = GetNSlices(category)

    originalHistogram.GetXaxis().SetNdivisions(-100*binsPerSlice-nSlices)
    
    gridPad = ROOT.TPad('slices_'+pad.GetName(),'slices_'+pad.GetName(),0,0,1,1)    
    gridPad.SetGridx()
    gridPad.SetTopMargin(pad.GetTopMargin())
    gridPad.SetBottomMargin(pad.GetBottomMargin())
    gridPad.SetFillStyle(4000)

    gridHisto = originalHistogram.Clone()
    gridHisto.Reset()
    gridHisto.GetXaxis().SetLabelSize(0.0)
    gridHisto.GetYaxis().SetLabelSize(0.0)
    gridHisto.GetXaxis().SetTickLength(0)
    gridHisto.GetYaxis().SetTickLength(0)
    gridHisto.GetYaxis().SetTitleSize(0)
    #gridHisto.GetXaxis().SetNdivisions(-100*binsPerSlice-nSlices)
    
    pad.cd()
    return gridPad,gridHisto

def CreateRatioSliceLines(plotSlices,pad):
    ratioGridPad = ROOT.TPad('slices_'+pad.GetName(),'slices_'+pad.GetName(),0,0,1,1)
    ratioGridPad.SetGridx()    
    ratioGridPad.SetTopMargin(pad.GetTopMargin())
    ratioGridPad.SetBottomMargin(pad.GetBottomMargin())
    ratioGridPad.SetFillStyle(4000)
    
    ratioGridHisto = plotSlices.Clone()    

    return ratioGridPad,ratioGridHisto
    
