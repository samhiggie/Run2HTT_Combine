import ROOT

lumiTextColor = ROOT.kBlack
lumiTextFont = 42
lumiTextAlignment = 31
lumiTextSize = 0.04
lumiTextPosition = (0.98,0.96)
lumi2016Text = '35.9 fb^{-1} (13 TeV)'
lumi2017Text = '41.5 fb^{-1} (13 TeV)'
lumi2018Text = '59.7 fb^{-1} (13 TeV)'
lumiRun2Text = '137.1 fb^{-1} (13 TeV)'

def CreateLumiText(year):
    lumiText = ROOT.TLatex()
    lumiText.SetNDC()
    lumiText.SetTextColor(lumiTextColor)
    lumiText.SetTextFont(lumiTextFont)
    lumiText.SetTextAlign(lumiTextAlignment)
    lumiText.SetTextSize(lumiTextSize)
    if year == '2016':
        lumiText.DrawLatex(lumiTextPosition[0],lumiTextPosition[1],lumi2016Text)
    elif year == '2017':
        lumiText.DrawLatex(lumiTextPosition[0],lumiTextPosition[1],lumi2017Text)
    elif year == '2018':
        lumiText.DrawLatex(lumiTextPosition[0],lumiTextPosition[1],lumi2018Text)
    elif year == 'Run2':
        lumiText.DrawLatex(lumiTextPosition[0],lumiTextPosition[1],lumiRun2Text)
    
