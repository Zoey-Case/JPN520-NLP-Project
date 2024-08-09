from MethodLibrary import Methods


countOutputHeader = ["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"]
percentOutputHeader = ["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"]


script1 = Methods.ReadFromCSV("Script1Parsed")
script1 = Methods.RemoveSymbols(script1)
S1parts = Methods.GetPOS(script1)
Methods.BubbleSort(S1parts)
S1total = Methods.CountEntries(S1parts)

script2 = Methods.ReadFromCSV("Script2Parsed")
script2.pop(-1)
script2 = Methods.RemoveSymbols(script2)
S2parts = Methods.GetPOS(script2)
Methods.BubbleSort(S2parts)
S2total = Methods.CountEntries(S2parts)

S1partsByP = Methods.CopyArray(S1parts)
Methods.ConvertToPercentages(S1partsByP, S1total)
S2partsByP = Methods.CopyArray(S2parts)
Methods.ConvertToPercentages(S2partsByP, S2total)


for S1entry in S1parts:
    found = False
    
    for S2entry in S2parts:
        if (S1entry[0] == S2entry[0]):
            S1entry += [S2entry[-1]]
            found = True
            S2parts.remove(S2entry)

    if(not found):
        S1entry += [0]

for S2entry in S2parts:
    S1parts.append([S2entry[0]] + [0] + [S2entry[1]])

Methods.WriteToCSV(countOutputHeader, S1parts, "CountCompareS1POS")


for S1entry in S1partsByP:
    found = False
    
    for S2entry in S2partsByP:
        if (S1entry[0] == S2entry[0]):
            S1entry += [S2entry[-1]]
            found = True
            S2partsByP.remove(S2entry)

    if(not found):
        S1entry += [0]

for S2entry in S2partsByP:
    S1partsByP.append([S2entry[0]] + [0] + [S2entry[1]])

Methods.WriteToCSV(percentOutputHeader, S1partsByP, "PercentCompareS1POS")


S2parts = Methods.CopyArray(S1parts)
Methods.BubbleSort(S2parts)
Methods.WriteToCSV(countOutputHeader, S2parts, "CountCompareS2POS")

S2partsByP = Methods.CopyArray(S1partsByP)
Methods.BubbleSort(S2partsByP)
Methods.WriteToCSV(countOutputHeader, S2partsByP, "PercentCompareS2POS")

totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("_Totals")
totals[3] = ["POS", S1total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "_Totals")

Methods.PromptComplete()
Methods.PromptContinue()