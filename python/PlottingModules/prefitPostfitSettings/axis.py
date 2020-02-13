import ROOT
from rebinning import GetNSlices

#axisLabels = ['-----','','#uparrow','50.0-170.0','#downarrow','-----','170.0-210.0','210.0-250.0','250.0+']
genericAxisLabels = ['50-70','70-90','90-110','110-130','130-150','150-170','170-210','210-250','250-290']

plotXAxisTitleSize = 0.12
plotXAxisTitleOffset = 1.7

xAxisLeftBound = 0.16

plotYAxisTitle= 'Events'
plotYAxisSize = 0.1
plotYAxisTitleOffset = 1.0
plotYAxisLabelSize = 0.075

#approximately 0.0305 per bin at 3 slices.
#approximate left bound at 0.16?

def CreateAxisLabels(theHist,category):
    theAxis = theHist.GetXaxis()
    theAxis.SetTitle('m_{#tau#tau} (GeV)')
    theAxis.SetTitleSize(plotXAxisTitleSize)
    theAxis.SetTitleOffset(plotXAxisTitleOffset)
    nSlices = GetNSlices(category)
    nBins = 9 * nSlices    
    for i in range(1,nBins+1):
        theAxis.SetBinLabel(i,genericAxisLabels[(i-1)%9])

    if nSlices == 0:
        plotXAxisLabelSize = 0.3
    else:
        plotXAxisLabelSize = 0.3/(1.0*nSlices)

    theAxis.SetLabelSize(plotXAxisLabelSize)

    theAxis.LabelsOption("Mv")
    #theAxis.CenterTitle()
    #theAxis.SetLabelOffset(999)
    #theAxis.SetLabelSize(0.0)
    #theAxis.SetAlphanumeric
    #theAxis.LabelsOption('v')
    #for i in range(1,10):
    #    theAxis.SetBinLabel(i,axisLabels[i-1])
        
def SetPlotXaxis(theHist):
    theAxis = theHist.GetXaxis()

def SetPlotYAxis(theHist):
    theAxis = theHist.GetYaxis()
    theAxis.SetTitle(plotYAxisTitle)
    theAxis.SetTitleOffset(plotYAxisTitleOffset)
    theAxis.SetTitleSize(plotYAxisLabelSize)
    theAxis.CenterTitle()
