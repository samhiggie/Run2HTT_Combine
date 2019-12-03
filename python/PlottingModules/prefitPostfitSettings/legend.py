import ROOT

legendPosition = (0.7,0.82,0.95,0.97)
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

def CreateLegend(histogramDictionary):
    pass
    """
    theLegend = ROOT.TLegend(legendPosition[0],legendPosition[1],legendPosition[2],legendPosition[3])
    
    theLegend.SetNColumns(nLegendColumns)

    for entry in histogramDictionary:
        AppendToLegend(theLegend,histogramDictionary[entry],entry)
    return theLegend
    """

def AppendToLegend(theLegend,histogram,entry):
    pass
    """
    try:
        theLegend.AddEntry(histogram,histogramEntries[entry],histogramFormats[entry])
    except KeyError:
        print("Failed to properly make entry for: "+str(entry))
    """
