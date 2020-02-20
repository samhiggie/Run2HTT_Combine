#!/usr/bin/env python
import argparse
import re

def LaTeXifyCategory(category):    
    category=category[:len(category)-4]
    if category == "r":        
        return "$\\mu$"
    if category == "r_ggH":
        return "$\\mu_{ggH}$"
    if category == "r_qqH":
        return "$\\mu_{qqH}$"
    if category == "r_WH":
        return "$\\mu_{WH}$"
    if category == "r_ZH":
        return "$\\mu_{ZH}$"
    if category == "r_ggH_FWDH_htt125":
        return "\\multicolumn{3}{c|}{$ggH$, Forward Higgs}"
    if category == "r_ggH_PTH_0_200_0J_PTH_0_10_htt125":
        return "$p_{t}^{H} [0,200]$ & 0 Jets & $0 \\leq p_{t}^{H} < 10 $"
    if category == "r_ggH_PTH_0_200_0J_PTH_10_200_htt125":
        return "$p_{t}^{H} [0,200]$ & 0 Jets & $10 \\leq p_{t}^{H} < 200 $"
    if category == "r_ggH_PTH_0_200_1J_PTH_60_120_htt125":
        return "$p_{t}^{H} [0,200]$ & 1 Jet & $60 \\leq p_{t}^{H} < 120 $"        
    if category == "r_ggH_PTH_0_200_1J_PTH_0_60_htt125":        
        return "$p_{t}^{H} [0,200]$ & 1 Jet & $0 \\leq p_{t}^{H} < 60 $"
    if category == "r_ggH_PTH_0_200_1J_PTH_120_200_htt125":
        return "$p_{t}^{H} [0,200]$ & 1 Jet & $120 \\leq p_{t}^{H} < 200 $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets, $m_{jj} [0,350]$ & $60 \\leq p_{t}^{H} < 120 $"        
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets, $m_{jj} [0,350]$ & $0 \\leq p_{t}^{H} < 60 $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets, $m_{jj} [0,350]$ & $120 \leq p_{t}^{H} < 200 $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets $m_{jj} [350,700]$ & $0 \\leq p_{t}^{H_{jj}} < 25 $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets $m_{jj} [350,700]$ & $25 \\leq p_{t}^{H_{jj}} < \\infty $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets $m_{jj} [700,\\infty]$ & $0 \\leq p_{t}^{H_{jj}} < 25 $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125":
        return "$p_{t}^{H} [0,200]$ & 2 Jets $m_{jj} [700,\infty]$ & $25 \leq p_{t}^{H_{jj}} < \infty $"
    if category == "r_ggH_PTH_0_200_GE2J_MJJ_GE350":
        return "merged: $p_{t}^{H} [0,200]$ & \\multicolumn{2}{c|}{2 Jets $m_{jj} \ge 350$}"
    if category == "r_ggH_PTH_200_300_htt125":
        return "\\multicolumn{3}{c|}{$p_{t}^{H}[200,300]$} "
    if category == "r_ggH_PTH_300_450_htt125":
        return "\\multicolumn{3}{c|}{$p_{t}^{H}[300,450]$} "
    if category == "r_ggH_PTH_450_650_htt125":
        return "\\multicolumn{3}{c|}{$p_{t}^{H}[450,650]$} "
    if category == "r_ggH_PTH_GE650_htt125":
        return "\\multicolumn{3}{c|}{$p_{t}^{H}\\ge 650$} "
    if category == "r_ggH_PTH_GE300":
        return "merged: \\multicolumn{3}{c|}{$p_{t}^{H}[300,\\infty]$} "
    if category == "r_qqH_FWDH_htt125":
        return "\\multicolumn{3}{c|}{$qqH$, Forward Higgs}"
    if category == "r_qqH_0J_htt125":
        return "\\multicolumn{3}{c|}{0 Jets}"
    if category == "r_qqH_1J_htt125":
        return "\\multicolumn{3}{c|}{1 Jet}"
    if category == "r_qqH_LT2J":
        return "merged: \\multicolumn{3}{c|}{$<$ 2 Jets}"
    if category == "r_qqH_GE2J_MJJ_0_60_htt125":
        return "2 Jets & $m_{jj} [0,350]$ & $0 \\leq m_{jj} < 60 $"
    if category == "r_qqH_GE2J_MJJ_60_120_htt125":
        return "2 Jets & $m_{jj} [0,350]$ & $60 \\leq m_{jj} < 120 $"
    if category == "r_qqH_GE2J_MJJ_120_350_htt125":
        return "2 Jets & $m_{jj} [0,350]$ & $120 \\leq m_{jj} < 350 $"
    if category == "r_qqH_GE2J_MJJ_0_350":
        return "merged: 2 Jets & \\multicolumn{2}{c|}{m_{jj}[0,350]}"
    if category == "r_qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125":
        return "2 Jets & $m_{jj} [350,\\infty]$ & $p_{t}^{H}[0,200],m_{jj}[350,700],p_{t}^{H_{jj}}[0,25]$"
    if category == "r_qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125":
        return "2 Jets & $m_{jj} [350,\\infty]$ & $p_{t}^{H}[0,200],m_{jj}[350,700],p_{t}^{H_{jj}}[25,\\infty]$"
    if category == "r_qqH_GE2J_MJJ_350_700_PTH_0_200":
        return "merged: 2 Jets & $m_{jj} [350,\infty]$ & $p_{t}^{H}[0,200],m_{jj}[350,700] $ "
    if category == "r_qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125":
        return "2 Jets & $m_{jj} [350,\\infty]$ & $p_{t}^{H}[0,200],m_{jj}[700,\\infty],p_{t}^{H_{jj}}[0,25]$"
    if category == "r_qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125":
        return "2 Jets & $m_{jj} [350,\\infty]$ & $p_{t}^{H}[0,200],m_{jj}[700,\\infty],p_{t}^{H_{jj}}[25,\\infty]$"
    if category == "r_qqH_GE2J_MJJ_GE700_PTH_0_200":
        return "merged: 2 Jets & $m_{jj} [350,\\infty]$ & $p_{t}^{H}[0,200],m_{jj}[700,\\infty]$"
    if category == "r_qqH_GE2J_MJJ_GE350_PTH_GE200_htt125":
        return "2 Jets & $m_{jj} [350,\infty]$ & $p_{t}^{H}[200,\infty]$"
    return "" 
parser = argparse.ArgumentParser()
parser.add_argument("input_2016",help="2016 Sorting STXS output to turn into a LaTeX table")
parser.add_argument("input_2017",help="2017 Sorting STXS output to turn into a LaTeX table")
parser.add_argument("input_2018",help="2018 Sorting STXS output to turn into a LaTeX table")
parser.add_argument("Run2input",help="Run 2 Sorting STXS output to turn into a LaTeX table")

args = parser.parse_args()

File_2016 = open(args.input_2016,"r")
File_2017 = open(args.input_2017,"r")
File_2018 = open(args.input_2018,"r")
Run2File = open(args.Run2input,"r")

Lines_2016 = File_2016.readlines()
Lines_2017 = File_2017.readlines()
Lines_2018 = File_2018.readlines()
Run2Lines = Run2File.readlines()

for i in range(len(Lines_2016)):
    resultLine_2016 = re.findall("((\+|-)[0-9]+\.[0-9]+)|N/A",Lines_2016[i])
    resultLine_2017 = re.findall("((\+|-)[0-9]+\.[0-9]+)|N/A",Lines_2017[i])
    resultLine_2018 = re.findall("((\+|-)[0-9]+\.[0-9]+)|N/A",Lines_2018[i])
    Run2resultLine = re.findall("((\+|-)[0-9]+\.[0-9]+)|N/A",Run2Lines[i])        
    if resultLine_2016:        
        #print(Lines_2016[i])
        #print(Lines_2017[i])
        #print(Lines_2018[i])
        #print(Run2Lines[i])
        #print ''
        #print(resultLine_2016)
        #print(resultLine_2017)
        #print(resultLine_2018)
        #print(Run2resultLine)
        if "N/A" in Lines_2016[i]:
            upUncert_2016 = 24.000
            downUncert_2016 = -26.000
        else:
            upUncert_2016 = float(resultLine_2016[1][0])
            downUncert_2016 = float(resultLine_2016[0][0])                        
        if "N/A" in Lines_2017[i]:
            upUncert_2017 = 24.000
            downUncert_2017 = -26.000
        else:
            upUncert_2017 = float(resultLine_2017[1][0])
            downUncert_2017 = float(resultLine_2017[0][0])                        
        if "N/A" in Lines_2018[i]:
            upUncert_2018 = 24.000
            downUncert_2018 = -26.000
        else:
            upUncert_2018 = float(resultLine_2018[1][0])
            downUncert_2018 = float(resultLine_2018[0][0])                        
        if "N/A" in Run2Lines[i]:
            Run2upUncert = 24.000
            Run2downUncert = -26.000
        else:
            Run2upUncert = float(Run2resultLine[1][0])
            Run2downUncert = float(Run2resultLine[0][0])                        
        category = re.search("r\S*",Lines_2016[i])        
        category = LaTeXifyCategory(category.group(0))
        if ("Forward Higgs" in category):
            print ''
        tableLine = category 
        #Let's make the up and down contribution strings before hand
        #2016
        if upUncert_2016 >= 24.0:
            upUncertString_2016 = "\\geq 25.000"
        else:
            upUncertString_2016 = "%.3f"%upUncert_2016
        if downUncert_2016 <= -26.0:
            downUncertString_2016 = "\\leq -25.000"
        else:
            downUncertString_2016 = "%.3f"%downUncert_2016
        #2017
        if upUncert_2017 >= 24.0:
            upUncertString_2017 = "\\geq 25.000"
        else:
            upUncertString_2017 = "%.3f"%upUncert_2017
        if downUncert_2017 <= -26.0:
            downUncertString_2017 = "\\leq -25.000"
        else:
            downUncertString_2017 = "%.3f"%downUncert_2017
        #2018
        if upUncert_2018 >= 24.0:
            upUncertString_2018 = "\\geq 25.000"
        else:
            upUncertString_2018 = "%.3f"%upUncert_2018
        if downUncert_2018 <= -26.0:
            downUncertString_2018 = "\\leq -25.000"
        else:
            downUncertString_2018 = "%.3f"%downUncert_2018
        #Run 2
        if Run2upUncert >= 24.0:
            upUncertString_Run2 = "\\geq 25.000"
        else:
            upUncertString_Run2 = "%.3f"%Run2upUncert
        if Run2downUncert <= -26.0:
            downUncertString_Run2 = "\\leq -25.000"
        else:
            downUncertString_Run2 = "%.3f"%Run2downUncert
        #construct the string
        tableLine += " & "+" $1.0^{"+upUncertString_2016+"}_{"+downUncertString_2016+"}$"
        tableLine += " & "+" $1.0^{"+upUncertString_2017+"}_{"+downUncertString_2017+"}$"
        tableLine += " & "+" $1.0^{"+upUncertString_2018+"}_{"+downUncertString_2018+"}$"
        tableLine += " & "+" $1.0^{"+upUncertString_Run2+"}_{"+downUncertString_Run2+"}$"        
        tableLine += "\\\\"
        print(tableLine)
