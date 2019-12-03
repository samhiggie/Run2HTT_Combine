import ROOT

pasStyle = ROOT.TStyle('pasStyle','Style for PAS plots')

def pasGrid(gridOn):
    pasStyle.SetPadGridX(gridOn)
    pasStyle.SetPadGridY(gridOn)

def fixOverlay():
    ROOT>gPad.RedrawAxis()

def setPASStyle():
    #Canvas Settings
    pasStyle.SetCanvasBorderMode(0)
    pasStyle.SetCanvasDefH(600)
    pasStyle.SetCanvasDefW(600)
    pasStyle.SetCanvasDefX(0)
    pasStyle.SetCanvasDefY(0)

    #Pad Settings
    pasStyle.SetPadBorderMode(0)
    
    pasStyle.SetPadColor(ROOT.kWhite)
    pasStyle.SetPadGridX(False)
    pasStyle.SetPadGridY(False)
    pasStyle.SetGridColor(0)
    pasStyle.SetGridStyle(3)
    pasStyle.SetGridWidth(1)

    #Frame Settings
    pasStyle.SetFrameBorderMode(0)
    pasStyle.SetFrameBorderSize(1)
    pasStyle.SetFrameFillColor(0)
    pasStyle.SetFrameFillStyle(0)
    pasStyle.SetFrameLineColor(1)
    pasStyle.SetFrameLineStyle(1)
    pasStyle.SetFrameLineWidth(1)

    #Histogram Settings
    pasStyle.SetHistLineColor(ROOT.kBlack)
    pasStyle.SetHistLineStyle(0)
    pasStyle.SetHistLineWidth(1)

    pasStyle.SetEndErrorSize(2)

    pasStyle.SetMarkerStyle(20)

    #fix data error line colors
    #pasStyle.SetLineColor(ROOT.kBlack)

    #Fit Settings
    pasStyle.SetOptFit(1)
    pasStyle.SetFitFormat("5.4g")
    pasStyle.SetFuncColor(2)
    pasStyle.SetFuncStyle(1)
    pasStyle.SetFuncWidth(1)

    #For the date:
    pasStyle.SetOptDate(0)

    #For the statistics box:
    pasStyle.SetOptFile(0)
    pasStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
    pasStyle.SetStatColor(ROOT.kWhite)
    pasStyle.SetStatFont(42)
    pasStyle.SetStatFontSize(0.025)
    pasStyle.SetStatTextColor(1)
    pasStyle.SetStatFormat("6.4g")
    pasStyle.SetStatBorderSize(1)
    pasStyle.SetStatH(0.1)
    pasStyle.SetStatW(0.15)

    # Margins:
    pasStyle.SetPadTopMargin(0.05)
    pasStyle.SetPadBottomMargin(0.13)
    pasStyle.SetPadLeftMargin(0.16)
    pasStyle.SetPadRightMargin(0.02)

    # For the Global title:
    pasStyle.SetOptTitle(0)
    pasStyle.SetTitleFont(42)
    pasStyle.SetTitleColor(1)
    pasStyle.SetTitleTextColor(1)
    pasStyle.SetTitleFillColor(10)
    pasStyle.SetTitleFontSize(0.05)
    # pasStyle.SetTitleH(0) # Set the height of the title box
    # pasStyle.SetTitleW(0) # Set the width of the title box
    # pasStyle.SetTitleX(0) # Set the position of the title box
    # pasStyle.SetTitleY(0.985) # Set the position of the title box
    # pasStyle.SetTitleStyle(Style_t style = 1001)
    # pasStyle.SetTitleBorderSize(2)

    # For the axis titles:
    
    pasStyle.SetTitleColor(1, "XYZ")
    pasStyle.SetTitleFont(42, "XYZ")
    pasStyle.SetTitleSize(0.06, "XYZ")
    # pasStyle.SetTitleXSize(Float_t size = 0.02) # Another way to set the size?
    # pasStyle.SetTitleYSize(Float_t size = 0.02)
    pasStyle.SetTitleXOffset(0.9)
    pasStyle.SetTitleYOffset(1.25)
    # pasStyle.SetTitleOffset(1.1, "Y") # Another way to set the Offset
    
    # For the axis labels:
    
    pasStyle.SetLabelColor(1, "XYZ")
    pasStyle.SetLabelFont(42, "XYZ")
    pasStyle.SetLabelOffset(0.007, "XYZ")
    pasStyle.SetLabelSize(0.05, "XYZ")
    
    # For the axis:
    
    pasStyle.SetAxisColor(1, "XYZ")
    pasStyle.SetStripDecimals(True)
    pasStyle.SetTickLength(0.03, "XYZ")
    pasStyle.SetNdivisions(510, "XYZ")
    pasStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
    pasStyle.SetPadTickY(1)
    
    # Change for log plots:
    pasStyle.SetOptLogx(0)
    pasStyle.SetOptLogy(0)
    pasStyle.SetOptLogz(0)
    
    # Postscript options:
    pasStyle.SetPaperSize(20.,20.)
