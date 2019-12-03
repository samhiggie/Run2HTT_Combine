import ROOT
legendPosition = (0,0,1,1)
histogramEntries = {
    'jetFakes':'Jet mis-ID',
    'ZT':'Z #rightarrow #tau#tau',
    'ZL':'Z #rightarrow ee/#mu#mu',
    'Top':'t#bar{t} + Jets',
    'Other':'Others',
    'Higgs':'Higgs #rightarrow #tau#tau (#times 20)',
    'data_obs':'Data',
    'background_error':'Bkg. uncertainty',
    }
histogramFormats = {
    'jetFakes':'f',
    'ZT':'f',
    'ZL':'f',
    'Top':'f',
    'Other':'f',
    'Higgs':'l',
    'data_obs':'pe',
    'background_error':'f',
    }
nLegendColumns = 2

theLegend = ROOT.TLegend(legendPosition[0],legendPosition[1],legendPosition[2],legendPosition[3])

def CreateLegend(histogramDictionary):    
    
    theLegend.SetNColumns(nLegendColumns)

    for entry in histogramDictionary:
        AppendToLegend(histogramDictionary[entry],entry)        
    

def AppendToLegend(histogram,entry):    
    try:
        theLegend.AddEntry(histogram,histogramEntries[entry],histogramFormats[entry])
    except KeyError:
        print("Failed to properly make entry for: "+str(entry))

def DrawLegend(outputDir):
    legendCanvas = ROOT.TCanvas("legend","legend",300,600)
    theLegend.Draw()
    legendCanvas.Draw()
    legendCanvas.SaveAs(outputDir+"legend.png")
    legendCanvas.SaveAs(outputDir+"legend.pdf")
    legendCanvas.Write()
