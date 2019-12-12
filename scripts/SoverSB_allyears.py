import ROOT
import os
import CombineHarvester.Run2HTT_Combine.CategoryConfigurations as CategoryConfigurations
import numpy as np 
from CombineHarvester.Run2HTT_Combine.PlottingModules.globalSettings.style import setTDRStyle

#given the exact directory path we can try to retrive all plots we know and care about.
#takes as arguments a TDirectory
def RetrievePlotsFromDirectory(directory):
    jetFakes = directory.Get("jetFakes")
    ZT = directory.Get("embedded")
    ZL = directory.Get("ZL")
    TTL = directory.Get("TTL")
    TTT = directory.Get("TTT")
    VVL = directory.Get("VVL")
    VVT = directory.Get("VVT")
    STL = directory.Get("STL")
    STT = directory.Get("STT")
    ggH = directory.Get("ggH_htt125")
    qqH = directory.Get("qqH_htt125")
    WH = directory.Get("WH_htt125")
    ZH = directory.Get("ZH_htt125")
    ggH_PTH_0_200_0J_PTH_0_10_htt125 = directory.Get('ggH_PTH_0_200_0J_PTH_0_10_htt125')
    ggH_PTH_0_200_0J_PTH_10_200_htt125 = directory.Get('ggH_PTH_0_200_0J_PTH_10_200_htt125')
    ggH_PTH_0_200_1J_PTH_0_60_htt125 = directory.Get('ggH_PTH_0_200_1J_PTH_0_60_htt125')
    ggH_PTH_0_200_1J_PTH_120_200_htt125 = directory.Get('ggH_PTH_0_200_1J_PTH_120_200_htt125')
    ggH_PTH_0_200_1J_PTH_60_120_htt125 = directory.Get('ggH_PTH_0_200_1J_PTH_60_120_htt125')
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125')
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125')
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125')    
    ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125')
    ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125')
    ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125')
    ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125 = directory.Get('ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125')
    ggH_PTH_GE200_htt125 = directory.Get('ggH_PTH_GE200_htt125')
    qqH_0J_htt125 = directory.Get('qqH_0J_htt125')
    qqH_1J_htt125 = directory.Get('qqH_1J_htt125')
    qqH_GE2J_MJJ_0_60_htt125 = directory.Get('qqH_GE2J_MJJ_0_60_htt125')
    qqH_GE2J_MJJ_120_350_htt125 = directory.Get('qqH_GE2J_MJJ_120_350_htt125')
    qqH_GE2J_MJJ_60_120_htt125 = directory.Get('qqH_GE2J_MJJ_60_120_htt125')
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125 = directory.Get('qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125')
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125 = directory.Get('qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125')
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125 = directory.Get('qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125')
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125 = directory.Get('qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125')
    qqH_GE2J_MJJ_GE350_PTH_GE200_htt125 = directory.Get('qqH_GE2J_MJJ_GE350_PTH_GE200_htt125')

    TT = TTL.Clone()
    TT.SetNameTitle("TT","TT")
    TT.Add(TTT)
    
    VV = VVL.Clone()
    VV.SetNameTitle("VV","VV")
    VV.Add(VVT)

    ST = STL.Clone()
    ST.SetNameTitle("ST","ST")
    ST.Add(STT)

    Top = TT.Clone()
    Top.SetNameTitle("Top","Top")
    Top.Add(ST)

    Higgs = ggH.Clone()
    Higgs.SetNameTitle("Higgs","Higgs")
    Higgs.Add(qqH)
    Higgs.Add(WH)
    Higgs.Add(ZH)

    Other = VV.Clone()
    Other.SetNameTitle("Other","Other")
    Other.Add(Higgs)    

    #create the Full histogram list
    fullDictionary = {
        'jetFakes':jetFakes,
        'ZT':ZT,
        'ZL':ZL,
        'TTL':TTL,
        'TTT':TTT,
        'VVL':VVL,
        'VVT':VVT,
        'STL':STL,
        'STT':STT,
        'ggH':ggH,
        'qqH':qqH,
        'WH':WH,
        'ZH':ZH,
        }
    slimmedDictionary = {
        'jetFakes':jetFakes,
        'ZT':ZT,
        'ZL':ZL,
        'Top':Top,        
        'Other':Other
        }

    signalDictionary = {
        'Higgs':Higgs,
        'ggH':ggH,
        'qqH':qqH,
        'WH':WH,
        'ZH':ZH,
        'ggH_PTH_0_200_0J_PTH_0_10_htt125':ggH_PTH_0_200_0J_PTH_0_10_htt125,
        'ggH_PTH_0_200_0J_PTH_10_200_htt125':ggH_PTH_0_200_0J_PTH_10_200_htt125,
        'ggH_PTH_0_200_1J_PTH_0_60_htt125':ggH_PTH_0_200_1J_PTH_0_60_htt125,
        'ggH_PTH_0_200_1J_PTH_120_200_htt125':ggH_PTH_0_200_1J_PTH_120_200_htt125,
        'ggH_PTH_0_200_1J_PTH_60_120_htt125':ggH_PTH_0_200_1J_PTH_60_120_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125':ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125':ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125':ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125': ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125': ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125':ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125,
        'ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125':ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125,
        'ggH_PTH_GE200_htt125':ggH_PTH_GE200_htt125,
        'qqH_0J_htt125':qqH_0J_htt125,
        'qqH_1J_htt125':qqH_1J_htt125,
        'qqH_GE2J_MJJ_0_60_htt125':qqH_GE2J_MJJ_0_60_htt125,
        'qqH_GE2J_MJJ_120_350_htt125':qqH_GE2J_MJJ_120_350_htt125,
        'qqH_GE2J_MJJ_60_120_htt125': qqH_GE2J_MJJ_60_120_htt125,
        'qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125':qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125,
        'qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125':qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125,
        'qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125':qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125,
        'qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125':qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125,
        'qqH_GE2J_MJJ_GE350_PTH_GE200_htt125':qqH_GE2J_MJJ_GE350_PTH_GE200_htt125,
        
    }

    #create the slimmed histogram list with the plots common to most plotting schemes
    return {'Full':fullDictionary,'Slimmed':slimmedDictionary,'Signals':signalDictionary}

def RetrieveOriginalDatacardPath(channel,year):
    datacardPath = os.environ['CMSSW_BASE']+'/src/auxiliaries/shapes/'
    datacardName = 'smh'+year+channel+'.root'
    return datacardPath+datacardName

#retrieve all plots conforming to current category configuration specs.
#takes as arguments a list of channels from ['tt','mt','et','em']
#and a TFile or TDirectory.
#the years of the plot to be retrieved
def RetrievePlotsFromAllDirectories(channels,location,years,withYears = True):
    location.ls()
    histograms = {}
    for channel in channels:
        histograms[channel] = {}        
        for year in years:
            histograms[channel][year]={}
            for categoryName in CategoryConfigurations.Categories[channel]:
                histograms[channel][year][categoryName] = {}
                for prefitOrPostfit in ['prefit','postfit']:                    
                    directoryName = categoryName+'_'+year+'_'+prefitOrPostfit
                    candidateDirectory = location.Get(directoryName)
                    if candidateDirectory == None:
                        print("Could not load all histograms from the files because it was missing a directory: "+directoryName)
                        continue
                    else:
                        print("loading plots from : "+directoryName)
                        histograms[channel][year][categoryName][prefitOrPostfit] = RetrievePlotsFromDirectory(candidateDirectory)                    
    return histograms

def reBin(rb,histoDict,category):

    rebinned={}
    #old recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    #recoBins=[70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    #mergeBins=[[0,1],[8,9]]
    print histoDict

    recoBins=[50.0,90.,110.,130.,150.0,170.0,210.0,300.0]
    recobw=[40.0,20.,20.,20.,20.0,40.0,90.0,300.0]
    recoBins.sort()
    from array import array 
    
    c = ROOT.TCanvas("c1","c1",50,50,600,600)
    #leg = ROOT.TLegend(0.1,0.45,0.28,0.84)
    leg = ROOT.TLegend(0.59,0.65,0.83,0.84)
    leg2 = ROOT.TLegend(0.59,0.65,0.83,0.84)
    pad1 = ROOT.TPad("pad1","The pad",0.0016,0.0,1.0,1.0)
    pad2 = ROOT.TPad("pad2","The upper right pad",0.5,0.2,0.9,0.7)

    c.cd()
    c.SetTitle("Weighted Fitted Mass rebinned")
    #c.SetLogy()
   
    setTDRStyle()
    sigstack2 = ROOT.THStack()
    bkgstack2 = ROOT.THStack()
    dataclone2 = ROOT.TH1F()


    if rb==1: 

        for name in histoDict.keys():

            histo = histoDict[name]
            print"rebinning ",name," in category  ",category,"   bin 0   ",histo.GetBinContent(0)
            
            rebinned[name]=ROOT.TH1F(name,name,len(recoBins)-1,array('d',recoBins))
            #rebinned[name]=histo
            rebinned[name].SetBinContent(0,(histo.GetBinContent(0)+histo.GetBinContent(1))/recobw[0])
            rebinned[name].SetBinContent(1,(histo.GetBinContent(2))/recobw[1])
            rebinned[name].SetBinContent(2,(histo.GetBinContent(3))/recobw[2])
            rebinned[name].SetBinContent(3,(histo.GetBinContent(4))/recobw[3])
            rebinned[name].SetBinContent(4,(histo.GetBinContent(5))/recobw[4])
            rebinned[name].SetBinContent(5,(histo.GetBinContent(6))/recobw[5])
            rebinned[name].SetBinContent(6,(histo.GetBinContent(7))/recobw[6])
            rebinned[name].SetBinContent(7,(histo.GetBinContent(8)+histo.GetBinContent(9))/recobw[7])

            rebinned[name].SetBinError(0,np.sqrt(histo.GetBinError(0)**2+histo.GetBinContent(1)**2)/recobw[0])
            rebinned[name].SetBinError(1,(histo.GetBinError(2))/recobw[1])
            rebinned[name].SetBinError(2,(histo.GetBinError(3))/recobw[2])
            rebinned[name].SetBinError(3,(histo.GetBinError(4))/recobw[3])
            rebinned[name].SetBinError(4,(histo.GetBinError(5))/recobw[4])
            rebinned[name].SetBinError(5,(histo.GetBinError(6))/recobw[5])
            rebinned[name].SetBinError(6,(histo.GetBinError(7))/recobw[6])
            rebinned[name].SetBinError(7,np.sqrt(histo.GetBinError(8)**2+histo.GetBinContent(9)**2)/recobw[7])

    if rb==0:
        for name in histoDict.keys():

            histo = histoDict[name]
            print"rebinning ",name," in category  ",category,"   bin 0   ",histo.GetBinContent(0)
            
            rebinned[name]=ROOT.TH1F(name,name,len(recoBins)-1,array('d',recoBins))
            #rebinned[name]=histo
            rebinned[name].SetBinContent(0,(histo.GetBinContent(0)+histo.GetBinContent(1)))
            rebinned[name].SetBinContent(1,(histo.GetBinContent(2)))
            rebinned[name].SetBinContent(2,(histo.GetBinContent(3)))
            rebinned[name].SetBinContent(3,(histo.GetBinContent(4)))
            rebinned[name].SetBinContent(4,(histo.GetBinContent(5)))
            rebinned[name].SetBinContent(5,(histo.GetBinContent(6)))
            rebinned[name].SetBinContent(6,(histo.GetBinContent(7)))
            rebinned[name].SetBinContent(7,(histo.GetBinContent(8)+histo.GetBinContent(9)))

            rebinned[name].SetBinError(0,np.sqrt(histo.GetBinError(0)**2+histo.GetBinContent(1)**2))
            rebinned[name].SetBinError(1,(histo.GetBinError(2)))
            rebinned[name].SetBinError(2,(histo.GetBinError(3)))
            rebinned[name].SetBinError(3,(histo.GetBinError(4)))
            rebinned[name].SetBinError(4,(histo.GetBinError(5)))
            rebinned[name].SetBinError(5,(histo.GetBinError(6)))
            rebinned[name].SetBinError(6,(histo.GetBinError(7)))
            rebinned[name].SetBinError(7,np.sqrt(histo.GetBinError(8)**2+histo.GetBinContent(9)**2))
    #for bn in range(0,histo.GetNbinsX()):
    #    i=0
    #    for binpair in mergeBins:
    #        if bn in binpair:
    #            rebinned[name].SetBinContent(binpair[0],rebinned[name].GetBinContent(binpair[0])+histo.GetBinContent(bn))
    #            rebinned[name].SetBinError(binpair[0],np.sqrt((rebinned[name].GetBinError(binpair[0]))**2+(histo.GetBinError(bn))**2))
    #            break
    #        elif(i==0):
    #            rebinned[name].SetBinContent(bn,rebinned[name].GetBinContent(bn)+histo.GetBinContent(bn))
    #            rebinned[name].SetBinError(bn,np.sqrt((rebinned[name].GetBinError(bn))**2+(histo.GetBinError(bn))**2))
    #            i=i+1


    #rebinned[name].Write(name)
    rebinned["ggH_htt125"].SetFillStyle(0)
    rebinned["ggH_htt125"].SetFillColor(ROOT.kBlue+2)
    rebinned["ggH_htt125"].GetXaxis().SetTitle("m_{#tau#tau}")
    rebinned["ggH_htt125"].GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")
    rebinned["ggH_htt125"].SetTitle("")
    leg.AddEntry(rebinned["ggH_htt125"])
    sigstack2.Add(rebinned["ggH_htt125"])

    rebinned["qqH_htt125"].SetFillStyle(0)
    rebinned["qqH_htt125"].SetFillColor(ROOT.kRed)
    leg.AddEntry(rebinned["qqH_htt125"])
    sigstack2.Add(rebinned["qqH_htt125"])

    rebinned["jetFakes"].SetFillStyle(1001)
    rebinned["jetFakes"].SetFillColor(ROOT.kSpring+6)
    leg.AddEntry(rebinned["jetFakes"])
    bkgstack2.Add(rebinned["jetFakes"])

    rebinned["ZL"].SetFillStyle(1001)
    rebinned["ZL"].SetFillColor(ROOT.kAzure-9)
    leg.AddEntry(rebinned["ZL"])
    bkgstack2.Add(rebinned["ZL"])

    rebinned["TTT"].SetFillStyle(1001)
    rebinned["TTT"].SetFillColor(ROOT.kBlue-8)
    leg.AddEntry(rebinned["TTT"])
    bkgstack2.Add(rebinned["TTT"])

    rebinned["TTL"].SetFillStyle(1001)
    rebinned["TTL"].SetFillColor(ROOT.kBlue-8)
    leg.AddEntry(rebinned["TTL"])
    bkgstack2.Add(rebinned["TTL"])

    rebinned["STL"].SetFillStyle(1001)
    rebinned["STL"].SetFillColor(ROOT.kBlue)
    leg.AddEntry(rebinned["STL"])
    bkgstack2.Add(rebinned["STL"])

    rebinned["STT"].SetFillStyle(1001)
    rebinned["STT"].SetFillColor(ROOT.kBlue)
    leg.AddEntry(rebinned["STT"])
    bkgstack2.Add(rebinned["STT"])

    rebinned["VVL"].SetFillStyle(1001)
    rebinned["VVL"].SetFillColor(ROOT.kRed-6)
    leg.AddEntry(rebinned["VVL"])
    bkgstack2.Add(rebinned["VVL"])

    rebinned["VVT"].SetFillStyle(1001)
    rebinned["VVT"].SetFillColor(ROOT.kRed-6)
    leg.AddEntry(rebinned["VVT"])
    bkgstack2.Add(rebinned["VVT"])

    rebinned["embedded"].SetFillStyle(1001)
    rebinned["embedded"].SetFillColor(ROOT.kOrange-4)
    leg.AddEntry(rebinned["embedded"])
    bkgstack2.Add(rebinned["embedded"])


    rebinned["data_obs"].SetMarkerStyle(20)
    rebinned["data_obs"].SetMarkerSize(1)
    rebinned["data_obs"].SetLineWidth(2)
    rebinned["data_obs"].SetLineColor(ROOT.kBlack)
    dataclone2 = rebinned["data_obs"].Clone()
    leg.AddEntry(rebinned["data_obs"])

    bkgstack2.Print()
    sigstack2.Print()
    c.cd()

    bkgstack2.Draw("hist")  
    sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")
    c.cd()
    c.Draw()
    pad1.Draw()

    bkgstack2.SetTitle("Weighted Fitted Mass S/(S+B)")  
    bkgstack2.GetXaxis().SetTitle("m_{#tau#tau}")  
    bkgstack2.GetYaxis().SetTitle("(Events/(bin width)) X  S/(S+B)")  
    bkgstack2.GetYaxis().SetTitleOffset(1.0)  
    bkgstack2.GetYaxis().SetLabelSize(0.03)  
    #bkgstack2.GetYaxis().SetMaxDigits(2)  
    ROOT.TGaxis.SetMaxDigits(3)  
    sigstack2.GetXaxis().SetTitle("m_{#tau#tau}")  
    sigstack2.GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")  
    dataclone2.GetXaxis().SetTitle("m_{#tau#tau}")  
    dataclone2.GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")  
    pad1.SetTitle("Weighted Fitted Mass")
    c.SetTitle("Weighted Fitted Mass")
    cmsText="CMS"
    preText="Preliminary"
    lumi="137 pb^{-1} #mu#tau 2018 (13TeV) Run II"
    latex1 = ROOT.TLatex(.15,0.95,cmsText)
    latex2 = ROOT.TLatex(.25,0.95,preText)
    latex1.SetNDC()
    latex2.SetNDC()
    latex1.SetTextFont(61)
    latex1.SetTextAlign(13)
    latex1.Draw("same")
    latex2.SetTextFont(52)
    latex2.SetTextAlign(13)
    latex2.Draw("same")
    r=pad1.GetRightMargin()
    t=pad1.GetTopMargin()
    lumiTextOffset=0.07
    latex3 = ROOT.TLatex(1-r,1-t+lumiTextOffset*t,lumi)
    latex3.SetTextSize(0.4*t)
    latex3.SetNDC()
    latex3.SetTextAngle(0)
    latex3.SetTextColor(ROOT.kBlack)
    latex3.SetTextFont(42)
    latex3.SetTextAlign(31)
    latex3.Draw("same")



    pad2.Draw()
    pad1.cd()
    #pad1.SetGrid(15,15)
    ROOT.gStyle.SetOptStat(0)
    bkgstack2.Draw("hist")  
    sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")

    ROOT.gStyle.SetOptStat(0)

    leg.Draw("p")

    #c.cd()
    pad2.cd()
    #pad2.SetGrid(15,15)
    #pad2.SetGrid(0,0)
    #pad2.Draw()

    dataclone2.SetTitle("")
    dataclone2.GetYaxis().SetTitle()
    dataclone2.GetYaxis().SetTitle()
    dataclone2.Draw("ep")
    sigstack2.Draw("hist,same")  

    leg2.AddEntry(dataclone2,"data")
    leg2.AddEntry(sigstack2,"signal")
    leg2.Draw()

    c.SaveAs(category+"_rebinned_sb.png")
    c.SaveAs(category+"_rebinned_sb.root")
    c.SaveAs(category+"_rebinned_sb.pdf")

    return rebinned

def makePlots(inputfile,rerollfile,recoBins,rollingBins,recobw,rb,category):

    histoDict={}

    direct=inputfile.Get(category)
    for key in direct.GetListOfKeys():
        histoDict[key.GetName()]=key.ReadObj()
    #rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    #recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    rollnum = len(recoBins)
    print rollnum
    rerolledDict = {}

    rerollfile.cd()
    rerollfile.mkdir(category)
    rerollfile.cd(category)
    
    
    print "looping over histograms"
    print histoDict
    print np.asarray(recoBins)
    from array import array


    for name in histoDict.keys():
        print "working on",name
        histo = histoDict[name]
        #rerolledDict[name]=ROOT.TH1F(name,name,len(recoBins)+1,min(recoBins),max(recoBins))
        #rerolledDict[name]=ROOT.TH1F(name,name,len(recoBins),np.asarray(recoBins))
        rerolledDict[name]=ROOT.TH1F(category+"_"+name+"_rerolled",category+"_"+name+"_rerolled",len(recoBins)-1,0,len(recoBins)-2)
        #rerolledDict[name]=ROOT.TH1F(name,name,len(recoBins),array('d',recoBins))
       

        for bn in range(0,histo.GetNbinsX()):
            for nbn in range(0,len(recoBins)+1):
                if ((bn%(len(recoBins))==nbn)):
                    rerolledDict[name].SetBinContent(nbn,rerolledDict[name].GetBinContent(nbn)+histo.GetBinContent(bn))
                    rerolledDict[name].SetBinError(nbn,np.sqrt((rerolledDict[name].GetBinError(nbn))**2+(histo.GetBinError(bn))**2))
        rerolledDict[name].Write(name)


    #from globalSettings.style import setTDRStyle
    sigstack = ROOT.TH1F("sig","sig",len(recoBins)-1,0,len(recoBins)-2)
    bkgstack = ROOT.TH1F("bkg","bkg",len(recoBins)-1,0,len(recoBins)-2)
    dataclone = ROOT.TH1F("data","data",len(recoBins)-1,0,len(recoBins)-2)
    #sigstack = ROOT.TH1F("sig","sig",len(recoBins),array('d',recoBins))
    #bkgstack = ROOT.TH1F("bkg","bkg",len(recoBins),array('d',recoBins))
    #dataclone = ROOT.TH1F("data","data",len(recoBins),array('d',recoBins))

    
    for histo in rerolledDict.keys():
        if "ggH" in histo:
            sigstack.Add(rerolledDict[histo])
        if "qqH" in histo:
            sigstack.Add(rerolledDict[histo])
        if "embedded" in histo:
            bkgstack.Add(rerolledDict[histo])
        if "ZL" in histo:
            bkgstack.Add(rerolledDict[histo])
        if ("TTT" or "TTL")in histo:
            bkgstack.Add(rerolledDict[histo])
        if ("STT" or "STL")in histo:
            bkgstack.Add(rerolledDict[histo])
        if ("VVL" or "VVT")  in histo:
            bkgstack.Add(rerolledDict[histo])
        if "jet"  in histo:
            bkgstack.Add(rerolledDict[histo])
        if "data"  in histo:
            dataclone = rerolledDict[histo].Clone()

    
    sbweight=[]
    for bn in range(0,sigstack.GetNbinsX()+1):
        #print "signal in bin",bn,"   ",sigstack.GetBinContent(bn)
        #print "bkg in bin",bn,"   ",bkgstack.GetBinContent(bn)
        sbweight.append(sigstack.GetBinContent(bn)/(sigstack.GetBinContent(bn)+bkgstack.GetBinContent(bn)))             

    print "The sb weights",sbweight
    c = ROOT.TCanvas("c1","c1",50,50,600,600)
    #leg = ROOT.TLegend(0.1,0.45,0.28,0.84)
    leg = ROOT.TLegend(0.59,0.65,0.83,0.84)
    leg2 = ROOT.TLegend(0.59,0.65,0.83,0.84)
    pad1 = ROOT.TPad("pad1","The pad",0.0016,0.0,1.0,1.0)
    pad2 = ROOT.TPad("pad2","The upper right pad",0.5,0.2,0.9,0.7)

    c.cd()
    c.SetTitle("Weighted Fitted Mass")
    #c.SetLogy()
   
    setTDRStyle()
    sigstack2 = ROOT.THStack()
    bkgstack2 = ROOT.THStack()
    dataclone2 = ROOT.TH1F()
    #print rerolledDict
    rerolledRebinned={}

    for histo in rerolledDict.keys():
        print "working on ",histo
        rerolledRebinned[histo] = ROOT.TH1F(histo+"_rebin",histo+"_rebin",len(recoBins)-1,array('d',recoBins))
        for bn in range(0,rerolledDict[histo].GetNbinsX()+1):
            print "scaling histo new value",rerolledDict[histo].GetBinContent(bn),"    times  ",sbweight[bn]
            rerolledRebinned[histo].SetBinContent(bn,rerolledDict[histo].GetBinContent(bn)*sbweight[bn]/recobw[bn])
            rerolledRebinned[histo].SetBinError(bn,rerolledDict[histo].GetBinError(bn)*sbweight[bn]/recobw[bn])
            rerolledDict[histo].SetBinContent(bn,rerolledDict[histo].GetBinContent(bn)*sbweight[bn]/recobw[bn])
            rerolledDict[histo].SetBinError(bn,rerolledDict[histo].GetBinError(bn)*sbweight[bn]/recobw[bn])
        rerolledRebinned[histo].Write()





    rerolledRebinned["ggH_htt125"].SetFillStyle(0)
    rerolledRebinned["ggH_htt125"].SetFillColor(ROOT.kBlue+2)
    rerolledRebinned["ggH_htt125"].GetXaxis().SetTitle("m_{#tau#tau}")
    rerolledRebinned["ggH_htt125"].GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")
    rerolledRebinned["ggH_htt125"].SetTitle("")
    leg.AddEntry(rerolledRebinned["ggH_htt125"])
    sigstack2.Add(rerolledRebinned["ggH_htt125"])

    rerolledRebinned["qqH_htt125"].SetFillStyle(0)
    rerolledRebinned["qqH_htt125"].SetFillColor(ROOT.kRed)
    leg.AddEntry(rerolledRebinned["qqH_htt125"])
    sigstack2.Add(rerolledRebinned["qqH_htt125"])

    rerolledRebinned["jetFakes"].SetFillStyle(1001)
    rerolledRebinned["jetFakes"].SetFillColor(ROOT.kSpring+6)
    leg.AddEntry(rerolledRebinned["jetFakes"])
    bkgstack2.Add(rerolledRebinned["jetFakes"])

    rerolledRebinned["ZL"].SetFillStyle(1001)
    rerolledRebinned["ZL"].SetFillColor(ROOT.kAzure-9)
    leg.AddEntry(rerolledRebinned["ZL"])
    bkgstack2.Add(rerolledRebinned["ZL"])

    rerolledRebinned["TTT"].SetFillStyle(1001)
    rerolledRebinned["TTT"].SetFillColor(ROOT.kBlue-8)
    leg.AddEntry(rerolledRebinned["TTT"])
    bkgstack2.Add(rerolledRebinned["TTT"])

    rerolledRebinned["TTL"].SetFillStyle(1001)
    rerolledRebinned["TTL"].SetFillColor(ROOT.kBlue-8)
    leg.AddEntry(rerolledRebinned["TTL"])
    bkgstack2.Add(rerolledRebinned["TTL"])

    rerolledRebinned["STL"].SetFillStyle(1001)
    rerolledRebinned["STL"].SetFillColor(ROOT.kBlue)
    leg.AddEntry(rerolledRebinned["STL"])
    bkgstack2.Add(rerolledRebinned["STL"])

    rerolledRebinned["STT"].SetFillStyle(1001)
    rerolledRebinned["STT"].SetFillColor(ROOT.kBlue)
    leg.AddEntry(rerolledRebinned["STT"])
    bkgstack2.Add(rerolledRebinned["STT"])

    rerolledRebinned["VVL"].SetFillStyle(1001)
    rerolledRebinned["VVL"].SetFillColor(ROOT.kRed-6)
    leg.AddEntry(rerolledRebinned["VVL"])
    bkgstack2.Add(rerolledRebinned["VVL"])

    rerolledRebinned["VVT"].SetFillStyle(1001)
    rerolledRebinned["VVT"].SetFillColor(ROOT.kRed-6)
    leg.AddEntry(rerolledRebinned["VVT"])
    bkgstack2.Add(rerolledRebinned["VVT"])

    rerolledRebinned["embedded"].SetFillStyle(1001)
    rerolledRebinned["embedded"].SetFillColor(ROOT.kOrange-4)
    leg.AddEntry(rerolledRebinned["embedded"])
    bkgstack2.Add(rerolledRebinned["embedded"])


    rerolledRebinned["data_obs"].SetMarkerStyle(20)
    rerolledRebinned["data_obs"].SetMarkerSize(1)
    rerolledRebinned["data_obs"].SetLineWidth(2)
    rerolledRebinned["data_obs"].SetLineColor(ROOT.kBlack)
    dataclone2 = rerolledRebinned["data_obs"].Clone()
    leg.AddEntry(rerolledRebinned["data_obs"])

    bkgstack2.Print()
    sigstack2.Print()
    c.cd()

    bkgstack2.Draw("hist")  
    sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")
    c.cd()
    c.Draw()
    pad1.Draw()

    bkgstack2.SetTitle("Weighted Fitted Mass S/(S+B)")  
    bkgstack2.GetXaxis().SetTitle("m_{#tau#tau}")  
    bkgstack2.GetYaxis().SetTitle("(Events/(bin width)) X  S/(S+B)")  
    bkgstack2.GetYaxis().SetTitleOffset(1.0)  
    bkgstack2.GetYaxis().SetLabelSize(0.03)  
    #bkgstack2.GetYaxis().SetMaxDigits(2)  
    ROOT.TGaxis.SetMaxDigits(3)  
    sigstack2.GetXaxis().SetTitle("m_{#tau#tau}")  
    sigstack2.GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")  
    dataclone2.GetXaxis().SetTitle("m_{#tau#tau}")  
    dataclone2.GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")  
    pad1.SetTitle("Weighted Fitted Mass")
    c.SetTitle("Weighted Fitted Mass")
    cmsText="CMS"
    preText="Preliminary"
    lumi="137 pb^{-1} #mu#tau 2018 (13TeV) Run II"
    latex1 = ROOT.TLatex(.15,0.95,cmsText)
    latex2 = ROOT.TLatex(.25,0.95,preText)
    latex1.SetNDC()
    latex2.SetNDC()
    latex1.SetTextFont(61)
    latex1.SetTextAlign(13)
    latex1.Draw("same")
    latex2.SetTextFont(52)
    latex2.SetTextAlign(13)
    latex2.Draw("same")
    r=pad1.GetRightMargin()
    t=pad1.GetTopMargin()
    lumiTextOffset=0.07
    latex3 = ROOT.TLatex(1-r,1-t+lumiTextOffset*t,lumi)
    latex3.SetTextSize(0.4*t)
    latex3.SetNDC()
    latex3.SetTextAngle(0)
    latex3.SetTextColor(ROOT.kBlack)
    latex3.SetTextFont(42)
    latex3.SetTextAlign(31)
    latex3.Draw("same")



    pad2.Draw()
    pad1.cd()
    #pad1.SetGrid(15,15)
    ROOT.gStyle.SetOptStat(0)
    bkgstack2.Draw("hist")  
    sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")

    ROOT.gStyle.SetOptStat(0)

    leg.Draw("p")

    #c.cd()
    pad2.cd()
    #pad2.SetGrid(15,15)
    #pad2.SetGrid(0,0)
    #pad2.Draw()
    
    dataclone2.SetTitle("")
    dataclone2.GetYaxis().SetTitle()
    dataclone2.GetYaxis().SetTitle()
    dataclone2.Draw("ep")
    sigstack2.Draw("hist,same")  

    leg2.AddEntry(dataclone2,"data")
    leg2.AddEntry(sigstack2,"signal")
    leg2.Draw()

    c.SaveAs(category+"_sb.png")
    c.SaveAs(category+"_sb.root")
    c.SaveAs(category+"_sb.pdf")
    

    #return histoDict
    return rerolledRebinned

def main():
    fhisto=ROOT.TFile.Open("FitHistos.root","READ")

    rerollfile = ROOT.TFile.Open("rerolled.root","recreate")

    mt_0jet_PTH_0_10_2016_prefit  ={}                                                                             
    mt_0jet_PTH_GE10_2016_prefit  ={}  
    mt_boosted_1J_2016_prefit     ={}  
    mt_boosted_GE2J_2016_prefit   ={}  
    mt_vbf_PTH_0_200_2016_prefit  ={}  
    mt_vbf_PTH_GE_200_2016_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2016_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2016_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2016_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2016_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2016  = reBin(rb,mt_0jet_PTH_0_10_2016_prefit,"mt_0jet_PTH_0_10_2016_prefit")       
    mt_0jet_PTH_GE10_2016  = reBin(rb,mt_0jet_PTH_GE10_2016_prefit,"mt_0jet_PTH_GE10_2016_prefit")
    mt_boosted_1J_2016     = reBin(rb,mt_boosted_1J_2016_prefit,"mt_boosted_1J_2016_prefit") 
    mt_boosted_GE2J_2016   = reBin(rb,mt_boosted_GE2J_2016_prefit,"mt_boosted_GE2J_2016_prefit")           
    mt_vbf_PTH_0_200_2016  = reBin(rb,mt_vbf_PTH_0_200_2016_prefit,"mt_vbf_PTH_0_200_2016_prefit")
    mt_vbf_PTH_GE_200_2016 = reBin(rb,mt_vbf_PTH_GE_200_2016_prefit,"mt_vbf_PTH_GE_200_2016_prefit")                                                     

    mt_0jet_PTH_0_10_2016_subplot  ={}                                                                             
    mt_0jet_PTH_GE10_2016_subplot  ={}  
    mt_boosted_1J_2016_subplot     ={}  
    mt_boosted_GE2J_2016_subplot   ={}  
    mt_vbf_PTH_0_200_2016_subplot  ={}  
    mt_vbf_PTH_GE_200_2016_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2016_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2016_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2016_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2016_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2016_sb = reBin(rb,mt_0jet_PTH_0_10_2016_subplot,"mt_0jet_PTH_0_10_2016_subplot")       
    mt_0jet_PTH_GE10_2016_sb = reBin(rb,mt_0jet_PTH_GE10_2016_subplot,"mt_0jet_PTH_GE10_2016_subplot")
    mt_boosted_1J_2016_sb = reBin(rb,mt_boosted_1J_2016_subplot,"mt_boosted_1J_2016_subplot") 
    mt_boosted_GE2J_2016_sb = reBin(rb,mt_boosted_GE2J_2016_subplot,"mt_boosted_GE2J_2016_subplot")           
    mt_vbf_PTH_0_200_2016_sb = reBin(rb,mt_vbf_PTH_0_200_2016_subplot,"mt_vbf_PTH_0_200_2016_subplot")
    mt_vbf_PTH_GE_200_2016_sb = reBin(rb,mt_vbf_PTH_GE_200_2016_subplot,"mt_vbf_PTH_GE_200_2016_subplot")                                                     
    #Merge the categories
    print "merging the categories"
    masterDictionary=mt_0jet_PTH_0_10_2016
    masterDictionary_sb=mt_0jet_PTH_0_10_2016_sb

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(mt_0jet_PTH_GE10_2016[histo])         
        masterDictionary[histo].Add(mt_boosted_1J_2016[histo])   
        masterDictionary[histo].Add(mt_boosted_GE2J_2016[histo])  
        masterDictionary[histo].Add(mt_vbf_PTH_0_200_2016[histo]) 
        masterDictionary[histo].Add(mt_vbf_PTH_GE_200_2016[histo])
        masterDictionary_sb[histo].Add(mt_0jet_PTH_GE10_2016_subplot[histo])         
        masterDictionary_sb[histo].Add(mt_boosted_1J_2016_subplot[histo])   
        masterDictionary_sb[histo].Add(mt_boosted_GE2J_2016_subplot[histo])  
        masterDictionary_sb[histo].Add(mt_vbf_PTH_0_200_2016_subplot[histo]) 
        masterDictionary_sb[histo].Add(mt_vbf_PTH_GE_200_2016_subplot[histo])


    mt_0jet_PTH_0_10_2017_prefit  ={}                                                                             
    mt_0jet_PTH_GE10_2017_prefit  ={}  
    mt_boosted_1J_2017_prefit     ={}  
    mt_boosted_GE2J_2017_prefit   ={}  
    mt_vbf_PTH_0_200_2017_prefit  ={}  
    mt_vbf_PTH_GE_200_2017_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2017_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2017_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2017_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2017_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2017  = reBin(rb,mt_0jet_PTH_0_10_2017_prefit,"mt_0jet_PTH_0_10_2017_prefit")       
    mt_0jet_PTH_GE10_2017  = reBin(rb,mt_0jet_PTH_GE10_2017_prefit,"mt_0jet_PTH_GE10_2017_prefit")
    mt_boosted_1J_2017     = reBin(rb,mt_boosted_1J_2017_prefit,"mt_boosted_1J_2017_prefit") 
    mt_boosted_GE2J_2017   = reBin(rb,mt_boosted_GE2J_2017_prefit,"mt_boosted_GE2J_2017_prefit")           
    mt_vbf_PTH_0_200_2017  = reBin(rb,mt_vbf_PTH_0_200_2017_prefit,"mt_vbf_PTH_0_200_2017_prefit")
    mt_vbf_PTH_GE_200_2017 = reBin(rb,mt_vbf_PTH_GE_200_2017_prefit,"mt_vbf_PTH_GE_200_2017_prefit")                                                     

    mt_0jet_PTH_0_10_2017_subplot  ={}                                                                             
    mt_0jet_PTH_GE10_2017_subplot  ={}  
    mt_boosted_1J_2017_subplot     ={}  
    mt_boosted_GE2J_2017_subplot   ={}  
    mt_vbf_PTH_0_200_2017_subplot  ={}  
    mt_vbf_PTH_GE_200_2017_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2017_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2017_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2017_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2017_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2017_sb = reBin(rb,mt_0jet_PTH_0_10_2017_subplot,"mt_0jet_PTH_0_10_2017_subplot")       
    mt_0jet_PTH_GE10_2017_sb = reBin(rb,mt_0jet_PTH_GE10_2017_subplot,"mt_0jet_PTH_GE10_2017_subplot")
    mt_boosted_1J_2017_sb = reBin(rb,mt_boosted_1J_2017_subplot,"mt_boosted_1J_2017_subplot") 
    mt_boosted_GE2J_2017_sb = reBin(rb,mt_boosted_GE2J_2017_subplot,"mt_boosted_GE2J_2017_subplot")           
    mt_vbf_PTH_0_200_2017_sb = reBin(rb,mt_vbf_PTH_0_200_2017_subplot,"mt_vbf_PTH_0_200_2017_subplot")
    mt_vbf_PTH_GE_200_2017_sb = reBin(rb,mt_vbf_PTH_GE_200_2017_subplot,"mt_vbf_PTH_GE_200_2017_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(mt_0jet_PTH_GE10_2017[histo])         
        masterDictionary[histo].Add(mt_boosted_1J_2017[histo])   
        masterDictionary[histo].Add(mt_boosted_GE2J_2017[histo])  
        masterDictionary[histo].Add(mt_vbf_PTH_0_200_2017[histo]) 
        masterDictionary[histo].Add(mt_vbf_PTH_GE_200_2017[histo])
        masterDictionary_sb[histo].Add(mt_0jet_PTH_GE10_2017_subplot[histo])         
        masterDictionary_sb[histo].Add(mt_boosted_1J_2017_subplot[histo])   
        masterDictionary_sb[histo].Add(mt_boosted_GE2J_2017_subplot[histo])  
        masterDictionary_sb[histo].Add(mt_vbf_PTH_0_200_2017_subplot[histo]) 
        masterDictionary_sb[histo].Add(mt_vbf_PTH_GE_200_2017_subplot[histo])


    mt_0jet_PTH_0_10_2018_prefit  ={}                                                                             
    mt_0jet_PTH_GE10_2018_prefit  ={}  
    mt_boosted_1J_2018_prefit     ={}  
    mt_boosted_GE2J_2018_prefit   ={}  
    mt_vbf_PTH_0_200_2018_prefit  ={}  
    mt_vbf_PTH_GE_200_2018_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2018_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2018_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2018_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2018_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2018  = reBin(rb,mt_0jet_PTH_0_10_2018_prefit,"mt_0jet_PTH_0_10_2018_prefit")       
    mt_0jet_PTH_GE10_2018  = reBin(rb,mt_0jet_PTH_GE10_2018_prefit,"mt_0jet_PTH_GE10_2018_prefit")
    mt_boosted_1J_2018     = reBin(rb,mt_boosted_1J_2018_prefit,"mt_boosted_1J_2018_prefit") 
    mt_boosted_GE2J_2018   = reBin(rb,mt_boosted_GE2J_2018_prefit,"mt_boosted_GE2J_2018_prefit")           
    mt_vbf_PTH_0_200_2018  = reBin(rb,mt_vbf_PTH_0_200_2018_prefit,"mt_vbf_PTH_0_200_2018_prefit")
    mt_vbf_PTH_GE_200_2018 = reBin(rb,mt_vbf_PTH_GE_200_2018_prefit,"mt_vbf_PTH_GE_200_2018_prefit")                                                     

    mt_0jet_PTH_0_10_2018_subplot  ={}                                                                             
    mt_0jet_PTH_GE10_2018_subplot  ={}  
    mt_boosted_1J_2018_subplot     ={}  
    mt_boosted_GE2J_2018_subplot   ={}  
    mt_vbf_PTH_0_200_2018_subplot  ={}  
    mt_vbf_PTH_GE_200_2018_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_0_10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_0jet_PTH_GE10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_1J_2018_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_boosted_GE2J_2018_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_0_200_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    mt_vbf_PTH_GE_200_2018_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"mt_vbf_PTH_GE_200_2018_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    mt_0jet_PTH_0_10_2018_sb = reBin(rb,mt_0jet_PTH_0_10_2018_subplot,"mt_0jet_PTH_0_10_2018_subplot")       
    mt_0jet_PTH_GE10_2018_sb = reBin(rb,mt_0jet_PTH_GE10_2018_subplot,"mt_0jet_PTH_GE10_2018_subplot")
    mt_boosted_1J_2018_sb = reBin(rb,mt_boosted_1J_2018_subplot,"mt_boosted_1J_2018_subplot") 
    mt_boosted_GE2J_2018_sb = reBin(rb,mt_boosted_GE2J_2018_subplot,"mt_boosted_GE2J_2018_subplot")           
    mt_vbf_PTH_0_200_2018_sb = reBin(rb,mt_vbf_PTH_0_200_2018_subplot,"mt_vbf_PTH_0_200_2018_subplot")
    mt_vbf_PTH_GE_200_2018_sb = reBin(rb,mt_vbf_PTH_GE_200_2018_subplot,"mt_vbf_PTH_GE_200_2018_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(mt_0jet_PTH_GE10_2018[histo])         
        masterDictionary[histo].Add(mt_boosted_1J_2018[histo])   
        masterDictionary[histo].Add(mt_boosted_GE2J_2018[histo])  
        masterDictionary[histo].Add(mt_vbf_PTH_0_200_2018[histo]) 
        masterDictionary[histo].Add(mt_vbf_PTH_GE_200_2018[histo])
        masterDictionary_sb[histo].Add(mt_0jet_PTH_GE10_2018_subplot[histo])         
        masterDictionary_sb[histo].Add(mt_boosted_1J_2018_subplot[histo])   
        masterDictionary_sb[histo].Add(mt_boosted_GE2J_2018_subplot[histo])  
        masterDictionary_sb[histo].Add(mt_vbf_PTH_0_200_2018_subplot[histo]) 
        masterDictionary_sb[histo].Add(mt_vbf_PTH_GE_200_2018_subplot[histo])
        
   
    et_0jet_PTH_0_10_2016_prefit  ={}                                                                             
    et_0jet_PTH_GE10_2016_prefit  ={}  
    et_boosted_1J_2016_prefit     ={}  
    et_boosted_GE2J_2016_prefit   ={}  
    et_vbf_PTH_0_200_2016_prefit  ={}  
    et_vbf_PTH_GE_200_2016_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2016_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2016_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2016_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2016_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2016  = reBin(rb,et_0jet_PTH_0_10_2016_prefit,"et_0jet_PTH_0_10_2016_prefit")       
    et_0jet_PTH_GE10_2016  = reBin(rb,et_0jet_PTH_GE10_2016_prefit,"et_0jet_PTH_GE10_2016_prefit")
    et_boosted_1J_2016     = reBin(rb,et_boosted_1J_2016_prefit,"et_boosted_1J_2016_prefit") 
    et_boosted_GE2J_2016   = reBin(rb,et_boosted_GE2J_2016_prefit,"et_boosted_GE2J_2016_prefit")           
    et_vbf_PTH_0_200_2016  = reBin(rb,et_vbf_PTH_0_200_2016_prefit,"et_vbf_PTH_0_200_2016_prefit")
    et_vbf_PTH_GE_200_2016 = reBin(rb,et_vbf_PTH_GE_200_2016_prefit,"et_vbf_PTH_GE_200_2016_prefit")                                                     

    et_0jet_PTH_0_10_2016_subplot  ={}                                                                             
    et_0jet_PTH_GE10_2016_subplot  ={}  
    et_boosted_1J_2016_subplot     ={}  
    et_boosted_GE2J_2016_subplot   ={}  
    et_vbf_PTH_0_200_2016_subplot  ={}  
    et_vbf_PTH_GE_200_2016_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2016_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2016_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2016_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2016_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2016_sb = reBin(rb,et_0jet_PTH_0_10_2016_subplot,"et_0jet_PTH_0_10_2016_subplot")       
    et_0jet_PTH_GE10_2016_sb = reBin(rb,et_0jet_PTH_GE10_2016_subplot,"et_0jet_PTH_GE10_2016_subplot")
    et_boosted_1J_2016_sb = reBin(rb,et_boosted_1J_2016_subplot,"et_boosted_1J_2016_subplot") 
    et_boosted_GE2J_2016_sb = reBin(rb,et_boosted_GE2J_2016_subplot,"et_boosted_GE2J_2016_subplot")           
    et_vbf_PTH_0_200_2016_sb = reBin(rb,et_vbf_PTH_0_200_2016_subplot,"et_vbf_PTH_0_200_2016_subplot")
    et_vbf_PTH_GE_200_2016_sb = reBin(rb,et_vbf_PTH_GE_200_2016_subplot,"et_vbf_PTH_GE_200_2016_subplot")                                                     
    #Merge the categories
    print "merging the categories"
    masterDictionary=et_0jet_PTH_0_10_2016
    masterDictionary_sb=et_0jet_PTH_0_10_2016_sb

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(et_0jet_PTH_GE10_2016[histo])         
        masterDictionary[histo].Add(et_boosted_1J_2016[histo])   
        masterDictionary[histo].Add(et_boosted_GE2J_2016[histo])  
        masterDictionary[histo].Add(et_vbf_PTH_0_200_2016[histo]) 
        masterDictionary[histo].Add(et_vbf_PTH_GE_200_2016[histo])
        masterDictionary_sb[histo].Add(et_0jet_PTH_GE10_2016_subplot[histo])         
        masterDictionary_sb[histo].Add(et_boosted_1J_2016_subplot[histo])   
        masterDictionary_sb[histo].Add(et_boosted_GE2J_2016_subplot[histo])  
        masterDictionary_sb[histo].Add(et_vbf_PTH_0_200_2016_subplot[histo]) 
        masterDictionary_sb[histo].Add(et_vbf_PTH_GE_200_2016_subplot[histo])


    et_0jet_PTH_0_10_2017_prefit  ={}                                                                             
    et_0jet_PTH_GE10_2017_prefit  ={}  
    et_boosted_1J_2017_prefit     ={}  
    et_boosted_GE2J_2017_prefit   ={}  
    et_vbf_PTH_0_200_2017_prefit  ={}  
    et_vbf_PTH_GE_200_2017_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2017_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2017_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2017_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2017_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2017  = reBin(rb,et_0jet_PTH_0_10_2017_prefit,"et_0jet_PTH_0_10_2017_prefit")       
    et_0jet_PTH_GE10_2017  = reBin(rb,et_0jet_PTH_GE10_2017_prefit,"et_0jet_PTH_GE10_2017_prefit")
    et_boosted_1J_2017     = reBin(rb,et_boosted_1J_2017_prefit,"et_boosted_1J_2017_prefit") 
    et_boosted_GE2J_2017   = reBin(rb,et_boosted_GE2J_2017_prefit,"et_boosted_GE2J_2017_prefit")           
    et_vbf_PTH_0_200_2017  = reBin(rb,et_vbf_PTH_0_200_2017_prefit,"et_vbf_PTH_0_200_2017_prefit")
    et_vbf_PTH_GE_200_2017 = reBin(rb,et_vbf_PTH_GE_200_2017_prefit,"et_vbf_PTH_GE_200_2017_prefit")                                                     

    et_0jet_PTH_0_10_2017_subplot  ={}                                                                             
    et_0jet_PTH_GE10_2017_subplot  ={}  
    et_boosted_1J_2017_subplot     ={}  
    et_boosted_GE2J_2017_subplot   ={}  
    et_vbf_PTH_0_200_2017_subplot  ={}  
    et_vbf_PTH_GE_200_2017_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2017_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2017_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2017_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2017_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2017_sb = reBin(rb,et_0jet_PTH_0_10_2017_subplot,"et_0jet_PTH_0_10_2017_subplot")       
    et_0jet_PTH_GE10_2017_sb = reBin(rb,et_0jet_PTH_GE10_2017_subplot,"et_0jet_PTH_GE10_2017_subplot")
    et_boosted_1J_2017_sb = reBin(rb,et_boosted_1J_2017_subplot,"et_boosted_1J_2017_subplot") 
    et_boosted_GE2J_2017_sb = reBin(rb,et_boosted_GE2J_2017_subplot,"et_boosted_GE2J_2017_subplot")           
    et_vbf_PTH_0_200_2017_sb = reBin(rb,et_vbf_PTH_0_200_2017_subplot,"et_vbf_PTH_0_200_2017_subplot")
    et_vbf_PTH_GE_200_2017_sb = reBin(rb,et_vbf_PTH_GE_200_2017_subplot,"et_vbf_PTH_GE_200_2017_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(et_0jet_PTH_GE10_2017[histo])         
        masterDictionary[histo].Add(et_boosted_1J_2017[histo])   
        masterDictionary[histo].Add(et_boosted_GE2J_2017[histo])  
        masterDictionary[histo].Add(et_vbf_PTH_0_200_2017[histo]) 
        masterDictionary[histo].Add(et_vbf_PTH_GE_200_2017[histo])
        masterDictionary_sb[histo].Add(et_0jet_PTH_GE10_2017_subplot[histo])         
        masterDictionary_sb[histo].Add(et_boosted_1J_2017_subplot[histo])   
        masterDictionary_sb[histo].Add(et_boosted_GE2J_2017_subplot[histo])  
        masterDictionary_sb[histo].Add(et_vbf_PTH_0_200_2017_subplot[histo]) 
        masterDictionary_sb[histo].Add(et_vbf_PTH_GE_200_2017_subplot[histo])


    et_0jet_PTH_0_10_2018_prefit  ={}                                                                             
    et_0jet_PTH_GE10_2018_prefit  ={}  
    et_boosted_1J_2018_prefit     ={}  
    et_boosted_GE2J_2018_prefit   ={}  
    et_vbf_PTH_0_200_2018_prefit  ={}  
    et_vbf_PTH_GE_200_2018_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2018_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2018_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2018_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2018_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2018  = reBin(rb,et_0jet_PTH_0_10_2018_prefit,"et_0jet_PTH_0_10_2018_prefit")       
    et_0jet_PTH_GE10_2018  = reBin(rb,et_0jet_PTH_GE10_2018_prefit,"et_0jet_PTH_GE10_2018_prefit")
    et_boosted_1J_2018     = reBin(rb,et_boosted_1J_2018_prefit,"et_boosted_1J_2018_prefit") 
    et_boosted_GE2J_2018   = reBin(rb,et_boosted_GE2J_2018_prefit,"et_boosted_GE2J_2018_prefit")           
    et_vbf_PTH_0_200_2018  = reBin(rb,et_vbf_PTH_0_200_2018_prefit,"et_vbf_PTH_0_200_2018_prefit")
    et_vbf_PTH_GE_200_2018 = reBin(rb,et_vbf_PTH_GE_200_2018_prefit,"et_vbf_PTH_GE_200_2018_prefit")                                                     

    et_0jet_PTH_0_10_2018_subplot  ={}                                                                             
    et_0jet_PTH_GE10_2018_subplot  ={}  
    et_boosted_1J_2018_subplot     ={}  
    et_boosted_GE2J_2018_subplot   ={}  
    et_vbf_PTH_0_200_2018_subplot  ={}  
    et_vbf_PTH_GE_200_2018_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_0_10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_0jet_PTH_GE10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_1J_2018_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_boosted_GE2J_2018_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_0_200_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    et_vbf_PTH_GE_200_2018_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"et_vbf_PTH_GE_200_2018_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    et_0jet_PTH_0_10_2018_sb = reBin(rb,et_0jet_PTH_0_10_2018_subplot,"et_0jet_PTH_0_10_2018_subplot")       
    et_0jet_PTH_GE10_2018_sb = reBin(rb,et_0jet_PTH_GE10_2018_subplot,"et_0jet_PTH_GE10_2018_subplot")
    et_boosted_1J_2018_sb = reBin(rb,et_boosted_1J_2018_subplot,"et_boosted_1J_2018_subplot") 
    et_boosted_GE2J_2018_sb = reBin(rb,et_boosted_GE2J_2018_subplot,"et_boosted_GE2J_2018_subplot")           
    et_vbf_PTH_0_200_2018_sb = reBin(rb,et_vbf_PTH_0_200_2018_subplot,"et_vbf_PTH_0_200_2018_subplot")
    et_vbf_PTH_GE_200_2018_sb = reBin(rb,et_vbf_PTH_GE_200_2018_subplot,"et_vbf_PTH_GE_200_2018_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(et_0jet_PTH_GE10_2018[histo])         
        masterDictionary[histo].Add(et_boosted_1J_2018[histo])   
        masterDictionary[histo].Add(et_boosted_GE2J_2018[histo])  
        masterDictionary[histo].Add(et_vbf_PTH_0_200_2018[histo]) 
        masterDictionary[histo].Add(et_vbf_PTH_GE_200_2018[histo])
        masterDictionary_sb[histo].Add(et_0jet_PTH_GE10_2018_subplot[histo])         
        masterDictionary_sb[histo].Add(et_boosted_1J_2018_subplot[histo])   
        masterDictionary_sb[histo].Add(et_boosted_GE2J_2018_subplot[histo])  
        masterDictionary_sb[histo].Add(et_vbf_PTH_0_200_2018_subplot[histo]) 
        masterDictionary_sb[histo].Add(et_vbf_PTH_GE_200_2018_subplot[histo])


    tt_0jet_PTH_0_10_2016_prefit  ={}                                                                             
    tt_0jet_PTH_GE10_2016_prefit  ={}  
    tt_boosted_1J_2016_prefit     ={}  
    tt_boosted_GE2J_2016_prefit   ={}  
    tt_vbf_PTH_0_200_2016_prefit  ={}  
    tt_vbf_PTH_GE_200_2016_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2016_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2016_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2016_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2016_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2016_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2016  = reBin(rb,tt_0jet_PTH_0_10_2016_prefit,"tt_0jet_PTH_0_10_2016_prefit")       
    tt_0jet_PTH_GE10_2016  = reBin(rb,tt_0jet_PTH_GE10_2016_prefit,"tt_0jet_PTH_GE10_2016_prefit")
    tt_boosted_1J_2016     = reBin(rb,tt_boosted_1J_2016_prefit,"tt_boosted_1J_2016_prefit") 
    tt_boosted_GE2J_2016   = reBin(rb,tt_boosted_GE2J_2016_prefit,"tt_boosted_GE2J_2016_prefit")           
    tt_vbf_PTH_0_200_2016  = reBin(rb,tt_vbf_PTH_0_200_2016_prefit,"tt_vbf_PTH_0_200_2016_prefit")
    tt_vbf_PTH_GE_200_2016 = reBin(rb,tt_vbf_PTH_GE_200_2016_prefit,"tt_vbf_PTH_GE_200_2016_prefit")                                                     

    tt_0jet_PTH_0_10_2016_subplot  ={}                                                                             
    tt_0jet_PTH_GE10_2016_subplot  ={}  
    tt_boosted_1J_2016_subplot     ={}  
    tt_boosted_GE2J_2016_subplot   ={}  
    tt_vbf_PTH_0_200_2016_subplot  ={}  
    tt_vbf_PTH_GE_200_2016_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2016_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2016_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2016_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2016_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2016_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2016_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2016_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2016_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2016_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2016_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2016_sb = reBin(rb,tt_0jet_PTH_0_10_2016_subplot,"tt_0jet_PTH_0_10_2016_subplot")       
    tt_0jet_PTH_GE10_2016_sb = reBin(rb,tt_0jet_PTH_GE10_2016_subplot,"tt_0jet_PTH_GE10_2016_subplot")
    tt_boosted_1J_2016_sb = reBin(rb,tt_boosted_1J_2016_subplot,"tt_boosted_1J_2016_subplot") 
    tt_boosted_GE2J_2016_sb = reBin(rb,tt_boosted_GE2J_2016_subplot,"tt_boosted_GE2J_2016_subplot")           
    tt_vbf_PTH_0_200_2016_sb = reBin(rb,tt_vbf_PTH_0_200_2016_subplot,"tt_vbf_PTH_0_200_2016_subplot")
    tt_vbf_PTH_GE_200_2016_sb = reBin(rb,tt_vbf_PTH_GE_200_2016_subplot,"tt_vbf_PTH_GE_200_2016_subplot")                                                     
    #Merge the categories
    print "merging the categories"
    masterDictionary=tt_0jet_PTH_0_10_2016
    masterDictionary_sb=tt_0jet_PTH_0_10_2016_sb

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(tt_0jet_PTH_GE10_2016[histo])         
        masterDictionary[histo].Add(tt_boosted_1J_2016[histo])   
        masterDictionary[histo].Add(tt_boosted_GE2J_2016[histo])  
        masterDictionary[histo].Add(tt_vbf_PTH_0_200_2016[histo]) 
        masterDictionary[histo].Add(tt_vbf_PTH_GE_200_2016[histo])
        masterDictionary_sb[histo].Add(tt_0jet_PTH_GE10_2016_subplot[histo])         
        masterDictionary_sb[histo].Add(tt_boosted_1J_2016_subplot[histo])   
        masterDictionary_sb[histo].Add(tt_boosted_GE2J_2016_subplot[histo])  
        masterDictionary_sb[histo].Add(tt_vbf_PTH_0_200_2016_subplot[histo]) 
        masterDictionary_sb[histo].Add(tt_vbf_PTH_GE_200_2016_subplot[histo])


    tt_0jet_PTH_0_10_2017_prefit  ={}                                                                             
    tt_0jet_PTH_GE10_2017_prefit  ={}  
    tt_boosted_1J_2017_prefit     ={}  
    tt_boosted_GE2J_2017_prefit   ={}  
    tt_vbf_PTH_0_200_2017_prefit  ={}  
    tt_vbf_PTH_GE_200_2017_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2017_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2017_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2017_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2017_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2017_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2017  = reBin(rb,tt_0jet_PTH_0_10_2017_prefit,"tt_0jet_PTH_0_10_2017_prefit")       
    tt_0jet_PTH_GE10_2017  = reBin(rb,tt_0jet_PTH_GE10_2017_prefit,"tt_0jet_PTH_GE10_2017_prefit")
    tt_boosted_1J_2017     = reBin(rb,tt_boosted_1J_2017_prefit,"tt_boosted_1J_2017_prefit") 
    tt_boosted_GE2J_2017   = reBin(rb,tt_boosted_GE2J_2017_prefit,"tt_boosted_GE2J_2017_prefit")           
    tt_vbf_PTH_0_200_2017  = reBin(rb,tt_vbf_PTH_0_200_2017_prefit,"tt_vbf_PTH_0_200_2017_prefit")
    tt_vbf_PTH_GE_200_2017 = reBin(rb,tt_vbf_PTH_GE_200_2017_prefit,"tt_vbf_PTH_GE_200_2017_prefit")                                                     

    tt_0jet_PTH_0_10_2017_subplot  ={}                                                                             
    tt_0jet_PTH_GE10_2017_subplot  ={}  
    tt_boosted_1J_2017_subplot     ={}  
    tt_boosted_GE2J_2017_subplot   ={}  
    tt_vbf_PTH_0_200_2017_subplot  ={}  
    tt_vbf_PTH_GE_200_2017_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2017_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2017_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2017_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2017_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2017_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2017_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2017_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2017_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2017_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2017_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2017_sb = reBin(rb,tt_0jet_PTH_0_10_2017_subplot,"tt_0jet_PTH_0_10_2017_subplot")       
    tt_0jet_PTH_GE10_2017_sb = reBin(rb,tt_0jet_PTH_GE10_2017_subplot,"tt_0jet_PTH_GE10_2017_subplot")
    tt_boosted_1J_2017_sb = reBin(rb,tt_boosted_1J_2017_subplot,"tt_boosted_1J_2017_subplot") 
    tt_boosted_GE2J_2017_sb = reBin(rb,tt_boosted_GE2J_2017_subplot,"tt_boosted_GE2J_2017_subplot")           
    tt_vbf_PTH_0_200_2017_sb = reBin(rb,tt_vbf_PTH_0_200_2017_subplot,"tt_vbf_PTH_0_200_2017_subplot")
    tt_vbf_PTH_GE_200_2017_sb = reBin(rb,tt_vbf_PTH_GE_200_2017_subplot,"tt_vbf_PTH_GE_200_2017_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(tt_0jet_PTH_GE10_2017[histo])         
        masterDictionary[histo].Add(tt_boosted_1J_2017[histo])   
        masterDictionary[histo].Add(tt_boosted_GE2J_2017[histo])  
        masterDictionary[histo].Add(tt_vbf_PTH_0_200_2017[histo]) 
        masterDictionary[histo].Add(tt_vbf_PTH_GE_200_2017[histo])
        masterDictionary_sb[histo].Add(tt_0jet_PTH_GE10_2017_subplot[histo])         
        masterDictionary_sb[histo].Add(tt_boosted_1J_2017_subplot[histo])   
        masterDictionary_sb[histo].Add(tt_boosted_GE2J_2017_subplot[histo])  
        masterDictionary_sb[histo].Add(tt_vbf_PTH_0_200_2017_subplot[histo]) 
        masterDictionary_sb[histo].Add(tt_vbf_PTH_GE_200_2017_subplot[histo])


    tt_0jet_PTH_0_10_2018_prefit  ={}                                                                             
    tt_0jet_PTH_GE10_2018_prefit  ={}  
    tt_boosted_1J_2018_prefit     ={}  
    tt_boosted_GE2J_2018_prefit   ={}  
    tt_vbf_PTH_0_200_2018_prefit  ={}  
    tt_vbf_PTH_GE_200_2018_prefit ={}                                     

    #rebin
    rb=1

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2018_prefit     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2018_prefit   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2018_prefit  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2018_prefit = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2018_prefit")                                                   

    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2018  = reBin(rb,tt_0jet_PTH_0_10_2018_prefit,"tt_0jet_PTH_0_10_2018_prefit")       
    tt_0jet_PTH_GE10_2018  = reBin(rb,tt_0jet_PTH_GE10_2018_prefit,"tt_0jet_PTH_GE10_2018_prefit")
    tt_boosted_1J_2018     = reBin(rb,tt_boosted_1J_2018_prefit,"tt_boosted_1J_2018_prefit") 
    tt_boosted_GE2J_2018   = reBin(rb,tt_boosted_GE2J_2018_prefit,"tt_boosted_GE2J_2018_prefit")           
    tt_vbf_PTH_0_200_2018  = reBin(rb,tt_vbf_PTH_0_200_2018_prefit,"tt_vbf_PTH_0_200_2018_prefit")
    tt_vbf_PTH_GE_200_2018 = reBin(rb,tt_vbf_PTH_GE_200_2018_prefit,"tt_vbf_PTH_GE_200_2018_prefit")                                                     

    tt_0jet_PTH_0_10_2018_subplot  ={}                                                                             
    tt_0jet_PTH_GE10_2018_subplot  ={}  
    tt_boosted_1J_2018_subplot     ={}  
    tt_boosted_GE2J_2018_subplot   ={}  
    tt_vbf_PTH_0_200_2018_subplot  ={}  
    tt_vbf_PTH_GE_200_2018_subplot ={}                                     

    #rebin
    rb=0

    #gather the dictionaries for the histograms 
    rollingBins = [30.0,40.0,50.0,10000.0]
    #recoBins=[50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_0_10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_0_10_2018_prefit")                                                             

    rollingBins = [30.0,40.0,50.0,60.0,70.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_0jet_PTH_GE10_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_0jet_PTH_GE10_2018_prefit")

    rollingBins = [0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_1J_2018_subplot     = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_1J_2018_prefit") 

    rollingBins=[0.0,60.0,120.0,200.0,250.0,300.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_boosted_GE2J_2018_subplot   = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_boosted_GE2J_2018_prefit")                                                                           

    rollingBins=[350.0,700.0,1000.0,1500.0,1800.0,10000.0]
    #recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_0_200_2018_subplot  = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_0_200_2018_prefit")

    rollingBins = [350.0,700.0,1200.0,10000.0]
    #recoBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
    recoBins=[50.0,70.0,90.,110.,130.,150.0,170.0,210.0,250.0,300.0]
    recobw = [20.0,20.0,20.0,20.0,20.0,20.0,40.0,40.0,8750.0,10000.0]
    tt_vbf_PTH_GE_200_2018_subplot = makePlots(fhisto,rerollfile,recoBins,rollingBins,recobw,rb,"tt_vbf_PTH_GE_200_2018_prefit")                                                   
    #Rebin the histograms 
    print "combining bins"
    tt_0jet_PTH_0_10_2018_sb = reBin(rb,tt_0jet_PTH_0_10_2018_subplot,"tt_0jet_PTH_0_10_2018_subplot")       
    tt_0jet_PTH_GE10_2018_sb = reBin(rb,tt_0jet_PTH_GE10_2018_subplot,"tt_0jet_PTH_GE10_2018_subplot")
    tt_boosted_1J_2018_sb = reBin(rb,tt_boosted_1J_2018_subplot,"tt_boosted_1J_2018_subplot") 
    tt_boosted_GE2J_2018_sb = reBin(rb,tt_boosted_GE2J_2018_subplot,"tt_boosted_GE2J_2018_subplot")           
    tt_vbf_PTH_0_200_2018_sb = reBin(rb,tt_vbf_PTH_0_200_2018_subplot,"tt_vbf_PTH_0_200_2018_subplot")
    tt_vbf_PTH_GE_200_2018_sb = reBin(rb,tt_vbf_PTH_GE_200_2018_subplot,"tt_vbf_PTH_GE_200_2018_subplot")                                                     

    for histo in masterDictionary.keys():
        print "Working on merging ",histo
        masterDictionary[histo].Add(tt_0jet_PTH_GE10_2018[histo])         
        masterDictionary[histo].Add(tt_boosted_1J_2018[histo])   
        masterDictionary[histo].Add(tt_boosted_GE2J_2018[histo])  
        masterDictionary[histo].Add(tt_vbf_PTH_0_200_2018[histo]) 
        masterDictionary[histo].Add(tt_vbf_PTH_GE_200_2018[histo])
        masterDictionary_sb[histo].Add(tt_0jet_PTH_GE10_2018_subplot[histo])         
        masterDictionary_sb[histo].Add(tt_boosted_1J_2018_subplot[histo])   
        masterDictionary_sb[histo].Add(tt_boosted_GE2J_2018_subplot[histo])  
        masterDictionary_sb[histo].Add(tt_vbf_PTH_0_200_2018_subplot[histo]) 
        masterDictionary_sb[histo].Add(tt_vbf_PTH_GE_200_2018_subplot[histo])

 

    #Final Plots
    c = ROOT.TCanvas("c1","c1",50,50,600,600)
    #leg = ROOT.TLegend(0.1,0.45,0.28,0.84)
    leg = ROOT.TLegend(0.59,0.7,0.83,0.88)
    leg2 = ROOT.TLegend(0.59,0.55,0.83,0.88)
    pad1 = ROOT.TPad("pad1","The pad",0.0016,0.0,1.0,1.0)
    pad2 = ROOT.TPad("pad2","The upper right pad",0.45,0.15,0.9,0.68)

    c.cd()
    #c.SetTitle("Weighted Fitted Mass")
    #c.SetLogy()
   
    setTDRStyle()
    sigstack2 = ROOT.THStack()
    bkgstack2 = ROOT.THStack()
    dataclone2 = ROOT.TH1F()
    bkg = ROOT.TH1F()
    #print rerolledDict

    masterDictionary["data_obs"].SetMarkerStyle(20)
    masterDictionary["data_obs"].SetMarkerSize(1)
    masterDictionary["data_obs"].SetLineWidth(2)
    masterDictionary["data_obs"].SetLineColor(ROOT.kBlack)
    dataclone2 = masterDictionary["data_obs"].Clone()
    leg.AddEntry(masterDictionary["data_obs"])


    leg.AddEntry(masterDictionary["ggH_htt125"],"signal","l")

    #masterDictionary["qqH_htt125"].SetFillStyle(0)
    #masterDictionary["qqH_htt125"].SetFillColor(ROOT.kRed)
    #leg.AddEntry(masterDictionary["qqH_htt125"])
    #sigstack2.Add(masterDictionary["qqH_htt125"])

    masterDictionary["jetFakes"].SetFillStyle(1001)
    #masterDictionary["jetFakes"].SetFillColor(ROOT.kSpring+6)
    masterDictionary["jetFakes"].SetFillColor(ROOT.TColor.GetColor("#ffccff"))
    leg.AddEntry(masterDictionary["jetFakes"],"Jets mis-ID","f")
    bkgstack2.Add(masterDictionary["jetFakes"])
    bkg = masterDictionary["jetFakes"].Clone()

    masterDictionary["ZL"].SetFillStyle(1001)
    #masterDictionary["ZL"].SetFillColor(ROOT.kAzure-9)
    masterDictionary["ZL"].SetFillColor(ROOT.TColor.GetColor("#4496c8"))
    leg.AddEntry(masterDictionary["ZL"],"Z#rightarrow ee/#mu#mu","f")
    bkgstack2.Add(masterDictionary["ZL"])
    bkg.Add(masterDictionary["ZL"])

    masterDictionary["TTT"].SetFillStyle(1001)
    masterDictionary["TTT"].SetFillColor(ROOT.kBlue-8)

    masterDictionary["TTL"].SetFillStyle(1001)
    masterDictionary["TTL"].SetFillColor(ROOT.TColor.GetColor("#9999cc"))
    masterDictionary["TTL"].Add(masterDictionary["TTT"])

    masterDictionary["STL"].SetFillStyle(1001)
    masterDictionary["STL"].SetFillColor(ROOT.kBlue)
    #leg.AddEntry(masterDictionary["STL"])
    #bkgstack2.Add(masterDictionary["STL"])

    masterDictionary["STT"].SetFillStyle(1001)
    #masterDictionary["STT"].SetFillColor(ROOT.kBlue)
    #masterDictionary["STT"].SetFillColor(ROOT.TColor.GetColor("#12cadd"))
    masterDictionary["STT"].SetFillColor(ROOT.TColor.GetColor("#9999cc"))
    masterDictionary["STT"].Add(masterDictionary["STL"])
    masterDictionary["STT"].Add(masterDictionary["TTL"])
    masterDictionary["STT"].Add(masterDictionary["TTT"])
    leg.AddEntry(masterDictionary["STT"],"t#bar{t} + Jets","f")
    bkgstack2.Add(masterDictionary["STT"])
    bkg.Add(masterDictionary["STT"])

    masterDictionary["VVL"].SetFillStyle(1001)
    masterDictionary["VVL"].SetFillColor(ROOT.kRed-6)
    #kleg.AddEntry(masterDictionary["VVL"])
    #kbkgstack2.Add(masterDictionary["VVL"])

    masterDictionary["VVT"].SetFillStyle(1001)
    #masterDictionary["VVT"].SetFillColor(ROOT.kRed-6)
    #masterDictionary["VVT"].SetFillColor(ROOT.TColor.GetColor("#de5a6a"))
    masterDictionary["VVT"].SetFillColor(ROOT.TColor.GetColor("#12cadd"))
    masterDictionary["VVT"].Add(masterDictionary["VVL"])
    leg.AddEntry(masterDictionary["VVT"],"Others","f")
    bkgstack2.Add(masterDictionary["VVT"])
    bkg.Add(masterDictionary["VVT"])

    masterDictionary["embedded"].SetFillStyle(1001)
    #masterDictionary["embedded"].SetFillColor(ROOT.kOrange-4)
    masterDictionary["embedded"].SetFillColor(ROOT.TColor.GetColor("#ffcc66"))
    leg.AddEntry(masterDictionary["embedded"],"DY#rightarrow#tau#tau","f")
    bkgstack2.Add(masterDictionary["embedded"])
    bkg.Add(masterDictionary["embedded"])

    masterDictionary["ggH_htt125"].SetFillStyle(0)
    #masterDictionary["ggH_htt125"].SetFillColor(ROOT.kBlue+2)
    masterDictionary["ggH_htt125"].SetFillColor(ROOT.kRed)
    masterDictionary["ggH_htt125"].SetLineColor(ROOT.kRed)
    masterDictionary["ggH_htt125"].GetXaxis().SetTitle("m_{#tau#tau} (GeV)")
    #masterDictionary["ggH_htt125"].GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")
    masterDictionary["ggH_htt125"].GetYaxis().SetTitle("S/(S+B) weighted events / GeV")
    masterDictionary["ggH_htt125"].SetMinimum(0.01)
    masterDictionary["ggH_htt125"].SetTitle("")
    masterDictionary["ggH_htt125"].Add(masterDictionary["qqH_htt125"])
    sigstack2.Add(masterDictionary["ggH_htt125"])
    bkgstack2.Add(masterDictionary["ggH_htt125"])


    sigstack2_sb = ROOT.THStack()
    bkgstack2_sb = ROOT.THStack()
    dataclone2_sb = ROOT.TH1F()
    bkg_sb = ROOT.TH1F()
    #print rerolledDict

    masterDictionary_sb["data_obs"].SetMarkerStyle(20)
    masterDictionary_sb["data_obs"].SetMarkerSize(1)
    masterDictionary_sb["data_obs"].SetLineWidth(2)
    masterDictionary_sb["data_obs"].SetLineColor(ROOT.kBlack)
    dataclone2_sb = masterDictionary_sb["data_obs"].Clone()

    #Blinding
    for bn in range(0,dataclone2.GetNbinsX()):
        if dataclone2.GetBinContent(bn)>0.6:
            dataclone2.SetBinContent(bn,-999.)
    for bn in range(0,dataclone2_sb.GetNbinsX()):
        if (bn==2 or bn==3):
            dataclone2_sb.SetBinContent(bn,-999.)


    #masterDictionary_sb["qqH_htt125"].SetFillStyle(0)
    #masterDictionary_sb["qqH_htt125"].SetFillColor(ROOT.kRed)
    #leg.AddEntry(masterDictionary_sb["qqH_htt125"])
    #sigstack2_sb.Add(masterDictionary_sb["qqH_htt125"])

    masterDictionary_sb["jetFakes"].SetFillStyle(1001)
    #masterDictionary_sb["jetFakes"].SetFillColor(ROOT.kSpring+6)
    masterDictionary_sb["jetFakes"].SetFillColor(ROOT.TColor.GetColor("#ffccff"))
    bkgstack2_sb.Add(masterDictionary_sb["jetFakes"])
    bkg_sb = masterDictionary_sb["jetFakes"].Clone()

    masterDictionary_sb["ZL"].SetFillStyle(1001)
    masterDictionary_sb["ZL"].SetFillColor(ROOT.TColor.GetColor("#4496c8"))
    bkgstack2_sb.Add(masterDictionary_sb["ZL"])
    bkg_sb.Add(masterDictionary_sb["ZL"])

    masterDictionary_sb["TTT"].SetFillStyle(1001)
    masterDictionary_sb["TTT"].SetFillColor(ROOT.kBlue-8)

    masterDictionary_sb["TTL"].SetFillStyle(1001)
    #masterDictionary_sb["TTL"].SetFillColor(ROOT.kBlue-8)
    masterDictionary_sb["TTL"].SetFillColor(ROOT.TColor.GetColor("#9999cc"))
    masterDictionary_sb["TTL"].Add(masterDictionary_sb["TTT"])
    bkgstack2_sb.Add(masterDictionary_sb["TTL"])
    bkg_sb.Add(masterDictionary_sb["TTL"])

    masterDictionary_sb["STL"].SetFillStyle(1001)
    masterDictionary_sb["STL"].SetFillColor(ROOT.kBlue)

    masterDictionary_sb["STT"].SetFillStyle(1001)
    masterDictionary_sb["STT"].SetFillColor(ROOT.TColor.GetColor("#12cadd"))
    masterDictionary_sb["STT"].Add(masterDictionary_sb["STL"])
    bkgstack2_sb.Add(masterDictionary_sb["STT"])
    bkg_sb.Add(masterDictionary_sb["STT"])

    masterDictionary_sb["VVL"].SetFillStyle(1001)
    masterDictionary_sb["VVL"].SetFillColor(ROOT.kRed-6)

    masterDictionary_sb["VVT"].SetFillStyle(1001)
    masterDictionary_sb["VVT"].SetFillColor(ROOT.TColor.GetColor("#de5a6a"))
    masterDictionary_sb["VVT"].Add(masterDictionary_sb["VVL"])
    bkgstack2_sb.Add(masterDictionary_sb["VVT"])
    bkg_sb.Add(masterDictionary_sb["VVT"])

    masterDictionary_sb["embedded"].SetFillStyle(1001)
    #masterDictionary_sb["embedded"].SetFillColor(ROOT.kOrange-4)
    masterDictionary_sb["embedded"].SetFillColor(ROOT.TColor.GetColor("#ffcc66"))
    bkgstack2_sb.Add(masterDictionary_sb["embedded"])
    bkg_sb.Add(masterDictionary_sb["embedded"])

    masterDictionary_sb["ggH_htt125"].SetFillStyle(0)
    #masterDictionary_sb["ggH_htt125"].SetFillColor(ROOT.kBlue+2)
    masterDictionary_sb["ggH_htt125"].SetFillColor(ROOT.kRed)
    masterDictionary_sb["ggH_htt125"].SetLineColor(ROOT.kRed)
    masterDictionary_sb["ggH_htt125"].GetXaxis().SetTitle("m_{#tau#tau} (GeV)")
    #masterDictionary_sb["ggH_htt125"].GetYaxis().SetTitle("(Events/(bin width))  #cross S/(S+B)")
    masterDictionary_sb["ggH_htt125"].GetYaxis().SetTitle("S/(S+B) weighted events / GeV")
    masterDictionary_sb["ggH_htt125"].SetMinimum(0.01)
    masterDictionary_sb["ggH_htt125"].SetTitle("")
    masterDictionary_sb["ggH_htt125"].Add(masterDictionary_sb["qqH_htt125"])
    sigstack2_sb.Add(masterDictionary_sb["ggH_htt125"])
    bkgstack2_sb.Add(masterDictionary_sb["ggH_htt125"])




    #Plotting!
    bkgstack2.Print()
    sigstack2.Print()
    c.cd()

    bkgstack2.Draw("hist")  
    #sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")
    c.cd()
    c.Draw()
    pad1.Draw()

    #bkgstack2.SetTitle("Weighted Fitted Mass S/(S+B)")  
    bkgstack2.GetXaxis().SetTitle("m_{#tau#tau} (GeV)")  
    bkgstack2.GetYaxis().SetTitle("S/(S+B) weighted events / GeV")  
    bkgstack2.GetYaxis().SetTitleSize(0.05)  
    bkgstack2.GetYaxis().SetTitleOffset(1.0)  
    bkgstack2.SetMaximum(float(bkgstack2.GetMaximum())*(1.12))
    #dataclone2.GetYaxis().SetRange(0.01,(float(bkgstack2.GetMaximum())*(1.3)))  
    bkgstack2.GetYaxis().SetLabelSize(0.035)  
    #bkgstack2.GetYaxis().SetMaxDigits(2)  
    ROOT.TGaxis.SetMaxDigits(3)  
    #pad1.SetTitle("Weighted Fitted Mass")
    #c.SetTitle("Weighted Fitted Mass")
    cmsText="CMS"
    preText="Preliminary"
    #lumi="137 pb^{-1} #mu#tau 2018 (13TeV) Run II"
    lumi="137 fb^{-1} (13TeV) Run II"
    latex1 = ROOT.TLatex(.15,0.88,cmsText)
    latex2 = ROOT.TLatex(.28,0.88,preText)
    latex1.SetNDC()
    latex2.SetNDC()
    latex1.SetTextFont(61)
    latex1.SetTextAlign(13)
    latex1.Draw("same")
    latex2.SetTextFont(52)
    latex2.SetTextAlign(13)
    latex2.Draw("same")
    r=pad1.GetRightMargin()
    t=pad1.GetTopMargin()
    lumiTextOffset=0.07
    latex3 = ROOT.TLatex(1-r,1-t+lumiTextOffset*t,lumi)
    latex3.SetTextSize(0.4*t)
    latex3.SetNDC()
    latex3.SetTextAngle(0)
    latex3.SetTextColor(ROOT.kBlack)
    latex3.SetTextFont(42)
    latex3.SetTextAlign(31)
    latex3.Draw("same")



    pad2.Draw()
    pad1.cd()
    #pad1.SetGrid(15,15)
    ROOT.gStyle.SetOptStat(0)
    bkgstack2.Draw("hist")  
    #sigstack2.Draw("hist,same")  
    dataclone2.Draw("same")

    ROOT.gStyle.SetOptStat(0)

    leg.SetBorderSize(0)
    leg.Draw("F")

    #inner sub plot! 

    #c.cd()
    pad2.cd()
    #pad2.SetGrid(15,15)
    #pad2.SetGrid(0,0)
    #pad2.Draw()
    dataclone3 = dataclone2_sb.Clone()
    dataclone3.Add(bkg_sb,-1)
    bkg_sb.Add(bkg_sb,-1)

    bkg_sb.SetTitle("")
    bkg_sb.SetFillColor(ROOT.kGray)
    dataclone3.SetTitle("")
    dataclone3.GetYaxis().SetTitle()
    dataclone3.GetXaxis().SetTitle("m_{#tau#tau} (GeV)")
    #bkg.GetXaxis().SetTitle("m_{#tau#tau} (GeV)")
    #bkg.GetXaxis().SetTitleSize(0.06)
    bkg_sb.GetYaxis().SetLabelSize(0.06)
    bkg_sb.GetXaxis().SetLabelSize(0.06)
    bkg_sb.Draw("E2")
    dataclone3.Draw("ep,same")
    
    sigstack2_sb.Draw("hist,same")  

    leg2.SetBorderSize(0)
    leg2.AddEntry(dataclone3,"Obs. - Bkg.")
    leg2.AddEntry(masterDictionary_sb["ggH_htt125"],"H#rightarrow#tau#tau","l")
    leg2.AddEntry(bkg_sb,"Bkg. Unc.","f")
    leg2.Draw("F")

    c.SaveAs("master_sb.png")
    c.SaveAs("master_sb.root")
    c.SaveAs("master_sb.pdf")
        

if __name__ == "__main__":
    main()
