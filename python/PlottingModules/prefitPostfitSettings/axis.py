import ROOT

#axisLabels = ['-----','','#uparrow','50.0-170.0','#downarrow','-----','170.0-210.0','210.0-250.0','250.0+']

plotYAxisTitle= 'Events'
plotYAxisSize = 0.1
plotYAxisTitleOffset = 1.0
plotYAxisLabelSize = 0.075


def CreateAxisLabels(theHist):
    theAxis = theHist.GetXaxis()
    theAxis.SetTitle('m_{#tau#tau}')
    #theAxis.SetAlphanumeric
    #theAxis.LabelsOption('v')
    #for i in range(1,10):
    #    theAxis.SetBinLabel(i,axisLabels[i-1])

def SetPlotYAxis(theHist):
    theAxis = theHist.GetYaxis()
    theAxis.SetTitle(plotYAxisTitle)
    theAxis.SetTitleOffset(plotYAxisTitleOffset)
    theAxis.SetTitleSize(plotYAxisLabelSize)
    theAxis.CenterTitle()
