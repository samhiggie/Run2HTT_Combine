import ROOT

prelimTextFont = 52
prelimTextAlign = 31
prelimTextSize = 0.05
prelimPosition = (0.42,0.96)

cmsTextFont = 61
cmsTextAlign = 31
cmsTextSize = 0.05
cmsPosition = (0.23,0.96)

def DrawCMSText():
    prelimText = ROOT.TLatex()
    prelimText.SetNDC()    
    prelimText.SetTextColor(ROOT.kBlack)
    prelimText.SetTextFont(prelimTextFont)
    prelimText.SetTextAlign(prelimTextAlign)
    prelimText.SetTextSize(prelimTextSize)
    prelimText.DrawLatex(prelimPosition[0],prelimPosition[1],"Preliminary")

    cmsText = ROOT.TLatex()
    cmsText.SetNDC()
    cmsText.SetTextColor(ROOT.kBlack)
    cmsText.SetTextFont(cmsTextFont)
    cmsText.SetTextAlign(cmsTextAlign)
    cmsText.SetTextSize(cmsTextSize)
    cmsText.DrawLatex(cmsPosition[0],cmsPosition[1],"CMS")
