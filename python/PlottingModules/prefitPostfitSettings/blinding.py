import ROOT
import math

#clculate the background content at given point
#takes the point number, and the full histogram dictionary
def CalculateB(i,FullDictionary):
    try:
        content = FullDictionary['jetFakes'].GetBinContent(i)
    except KeyError:
        content = FullDictionary['QCD'].GetBinContent(i)
        content += FullDictionary['W'].GetBinContent(i)
    content += FullDictionary['ZT'].GetBinContent(i)
    content += FullDictionary['ZL'].GetBinContent(i)
    content += FullDictionary['TTL'].GetBinContent(i)
    try:
        content += FullDictionary['TTT'].GetBinContent(i)
    except KeyError:
        pass
    content += FullDictionary['VVL'].GetBinContent(i)
    try:
        content += FullDictionary['VVT'].GetBinContent(i)
    except KeyError:
        pass
    content += FullDictionary['STL'].GetBinContent(i)
    try:
        content += FullDictionary['STT'].GetBinContent(i)
    except KeyError:
        pass
    return content

#this function will blind our datapoints,
#i.e set them to -1 upon a given condition
#the current condition is just S/root(B) > 0.5
def BlindDataPoints(SignalDictionary,FullDictionary,DataDictionary):
    dataPointRangeLow = 1
    dataPointRangeHigh = DataDictionary['data_obs'].GetNbinsX() + 1
    for i in range(dataPointRangeLow,dataPointRangeHigh):
        backgroundContentAtPoint = CalculateB(i,FullDictionary)
        signalContentAtPoint = SignalDictionary['Higgs'].GetBinContent(i)        
        try:
            if signalContentAtPoint / math.sqrt(backgroundContentAtPoint) > 0.5:
                DataDictionary['data_obs'].SetBinContent(i,0.0)
        except ZeroDivisionError:
            print("Skipping zero prediction bin...")

def BlindRatioPlot(SignalDictionary,FullDictionary,ratioPlot):
    ratioRangeLow = 1
    ratioRangeHigh = ratioPlot.GetN()
    for i in range(ratioRangeLow,ratioRangeHigh):
        backgroundContentAtPoint = CalculateB(i,FullDictionary)
        signalContentAtPoint = SignalDictionary['Higgs'].GetBinContent(i)
        try:
            if signalContentAtPoint / math.sqrt(backgroundContentAtPoint) > 0.5:
                ratioPlot.SetPoint(i,-1,-1)
        except ZeroDivisionError:
            print("Skipping zero prediction bin...")
