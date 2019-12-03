import ROOT
import CombineHarvester.Run2HTT_Combine.CategoryConfigurations as catConfig

binsPerSlice = 9

def CreateSliceLines(category,originalHistogram,pad):    
    if (category == catConfig.tt_boosted_1J_category
        or category == catConfig.tt_boosted_GE2J_category
        or category == catConfig.mt_boosted_1J_category
        or category == catConfig.mt_boosted_GE2J_category
        or category == catConfig.et_boosted_1J_category
        or category == catConfig.et_boosted_GE2J_category
        or category == catConfig.em_boosted_1J_category
        or category == catConfig.em_boosted_GE2J_category
        or category == catConfig.tt_vbf_high_category
        or category == catConfig.tt_vbf_low_category):
        nSlices = 6
    elif (category == catConfig.mt_vbf_low_category          
          or category == catConfig.et_vbf_low_category          
          or category == catConfig.em_vbf_low_category
          or category == catConfig.mt_0jet_high_category
          or category == catConfig.et_0jet_high_category
          or category == catConfig.em_0jet_high_category):
        nSlices = 5
    elif (category == catConfig.mt_vbf_high_category
          or category == catConfig.et_vbf_high_category
          or category == catConfig.em_vbf_high_category
          or category == catConfig.mt_0jet_low_category
          or category == catConfig.et_0jet_low_category
          or category == catConfig.em_0jet_low_category):
        nSlices = 3    
    elif (category == catConfig.tt_0jet_category):
        nSlices = 0    

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
    
    pad.cd()
    return gridPad,gridHisto

def CreateRatioSliceLines(category,histogram):
    if (category == catConfig.tt_boosted_1J_category
        or category == catConfig.tt_boosted_GE2J_category
        or category == catConfig.mt_boosted_1J_category
        or category == catConfig.mt_boosted_GE2J_category
        or category == catConfig.et_boosted_1J_category
        or category == catConfig.et_boosted_GE2J_category
        or category == catConfig.em_boosted_1J_category
        or category == catConfig.em_boosted_GE2J_category
        or category == catConfig.tt_vbf_high_category
        or category == catConfig.tt_vbf_low_category):
        nSlices = 6
    elif (category == catConfig.mt_vbf_low_category          
          or category == catConfig.et_vbf_low_category          
          or category == catConfig.em_vbf_low_category
          or category == catConfig.mt_0jet_high_category
          or category == catConfig.et_0jet_high_category
          or category == catConfig.em_0jet_high_category):
        nSlices = 5
    elif (category == catConfig.mt_vbf_high_category
          or category == catConfig.et_vbf_high_category
          or category == catConfig.em_vbf_high_category
          or category == catConfig.mt_0jet_low_category
          or category == catConfig.et_0jet_low_category
          or category == catConfig.em_0jet_low_category):
        nSlices = 3    
    elif (category == catConfig.tt_0jet_category):
        nSlices = 0    

    histogram.GetXaxis().SetNdivisions(-100*binsPerSlice-nSlices)
