import ROOT

fillColoringScheme = {
        'jetFakes':"#ffccff",
        'ZT':"#ffcc66",
        'ZL':'#4496c8',
        'Top':'#9999cc',
        'Other':'#12cadd',
        }

lineColoringScheme = {
        'Higgs': ROOT.kRed,
        'jetFakes':ROOT.kBlack,
        'ZT':ROOT.kBlack,
        'ZL':ROOT.kBlack,
        'Top':ROOT.kBlack,
        'Other':ROOT.kBlack,
        }

lineWidthScheme = {
    'Higgs':2
    }

def ColorizePrefitDistribution(histogramDictionary):            
    for entry in histogramDictionary:
        try:
            histogramDictionary[entry].SetFillColor(ROOT.TColor.GetColor(fillColoringScheme[entry]))
        except KeyError:
            print("Failed to colorize the fill of distribution: "+str(entry))
        except AttributeError:
            print("Histogram does not seem to properly exist: "+str(entry))
    for entry in histogramDictionary:
        try:            
            histogramDictionary[entry].SetLineColor(lineColoringScheme[entry])
        except KeyError:
            print("Failed to colorize the line of distribution: "+str(entry))
        except AttributeError:
            print("Histogram does not seem to properly exist: "+str(entry))

    for entry in histogramDictionary:
        try:
            histogramDictionary[entry].SetLineWidth(lineWidthScheme[entry])
        except KeyError:
            print("Failed to set line width of distribution "+str(entry))
        except AttributeError:
            print("Histogram does no exist: "+str(entry))
