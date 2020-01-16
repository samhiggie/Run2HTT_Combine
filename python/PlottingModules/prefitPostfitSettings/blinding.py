import ROOT
import math
from CombineHarvester.Run2HTT_Combine.PlottingModules.prefitPostfitSettings.rebinning import GetNSlices

#this function will blind our datapoints,
#current blinding scheme is to just blind mtt range 90-150
#this corresponds to bins 3,4 and 5, in each slices.
def BlindDataPoints(DataDictionary,category):
    nSlices = GetNSlices(category)    
    for i in range(nSlices):
        #backgroundContentAtPoint = CalculateB(i,FullDictionary)
        #signalContentAtPoint = SignalDictionary['Higgs'].GetBinContent(i)        
        #try:
        #    if signalContentAtPoint / math.sqrt(backgroundContentAtPoint) > 0.5:
        bin_3 = 3+i*9
        bin_4 = 4+i*9
        bin_5 = 5+i*9
        DataDictionary['data_obs'].SetBinContent(bin_3,0.0)
        DataDictionary['data_obs'].SetBinContent(bin_4,0.0)
        DataDictionary['data_obs'].SetBinContent(bin_5,0.0)
        #except ZeroDivisionError:
        #    print("Skipping zero prediction bin...")        

def BlindRatioPlot(ratioPlot,category):
    nSlices = GetNSlices(category)    
    for i in range(nSlices):        
        bin_3 = 3+i*9
        bin_4 = 4+i*9
        bin_5 = 5+i*9
        ratioPlot.SetPoint(bin_3,-1,-1)
        ratioPlot.SetPoint(bin_4,-1,-1)
        ratioPlot.SetPoint(bin_5,-1,-1)
        
