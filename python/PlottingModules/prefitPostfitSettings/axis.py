import ROOT

#axisLabels = ['-----','','#uparrow','50.0-170.0','#downarrow','-----','170.0-210.0','210.0-250.0','250.0+']

plotXAxisTitleSize = 0.1

xAxisLeftBound = 0.16

plotYAxisTitle= 'Events'
plotYAxisSize = 0.1
plotYAxisTitleOffset = 1.0
plotYAxisLabelSize = 0.075

#approximately 0.0305 per bin at 3 slices.
#approximate left bound at 0.16?

def CreateAxisLabels(theHist):
    pass
    """
    theAxis = theHist.GetXaxis()
    theAxis.SetTitle('m_{#tau#tau}')
    theAxis.SetTitleSize(plotXAxisTitleSize)
    theAxis.SetTitleOffset(1.1)
    #theAxis.CenterTitle()
    theAxis.SetLabelOffset(999)
    theAxis.SetLabelSize(0.0)
    #theAxis.SetAlphanumeric
    #theAxis.LabelsOption('v')
    #for i in range(1,10):
    #    theAxis.SetBinLabel(i,axisLabels[i-1])
    labelOne = ROOT.TLatex()
    labelOne.SetNDC()
    labelOne.SetTextColor(ROOT.kBlack)
    labelOne.SetTextFont(42)
    labelOne.SetTextSize(0.08)
    #labelOne.DrawLatex(0.16,0.18,'50.0-170.0')
    labelTwo = ROOT.TLatex()
    labelTwo.SetNDC()
    labelTwo.SetTextColor(ROOT.kBlack)
    labelTwo.SetTextFont(42)
    labelTwo.SetTextSize(0.05)
    labelTwo.SetTextAngle(45)
    #labelTwo.DrawLatex(0.35,0.2,'170.0-210.0')    
    labelThree = ROOT.TLatex()
    labelThree.SetNDC()
    labelThree.SetTextColor(ROOT.kBlack)
    labelThree.SetTextFont(42)
    labelThree.SetTextSize(0.05)
    labelThree.SetTextAngle(45)
    #labelThree.DrawLatex(0.38,0.2,'210.0-250.0')    
    labelFour = ROOT.TLatex()
    labelFour.SetNDC()
    labelFour.SetTextColor(ROOT.kBlack)
    labelFour.SetTextFont(42)
    labelFour.SetTextSize(0.05)
    labelFour.SetTextAngle(45)
    #labelFour.DrawLatex(0.41,0.2,'250.0+')    
    for i in range(0,3):
        midValue = xAxisLeftBound + 2*0.0305 + i*9*0.0305
        labelOne.DrawLatex(midValue,0.18,'50.0-170.0')
        labelTwo.DrawLatex(0.315+i*9*0.0305,0.045,'170.0-210.0')
        labelThree.DrawLatex(0.315+0.0305+i*9*0.0305,0.045,'210.0-250.0')
        labelFour.DrawLatex(0.33+2*0.0305+i*9*0.0305,0.13,'250.0+')
    """
        
def SetPlotXaxis(theHist):
    theAxis = theHist.GetXaxis()

def SetPlotYAxis(theHist):
    theAxis = theHist.GetYaxis()
    theAxis.SetTitle(plotYAxisTitle)
    theAxis.SetTitleOffset(plotYAxisTitleOffset)
    theAxis.SetTitleSize(plotYAxisLabelSize)
    theAxis.CenterTitle()
