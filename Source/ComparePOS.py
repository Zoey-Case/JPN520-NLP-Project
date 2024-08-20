from MethodLibrary import Methods


countOutputHeader = ["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"]
percentOutputHeader = ["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"]


script1 = Methods.ReadFromCSV("Script1Parsed", Methods.GetDirectoryMainCSV())
script1 = Methods.RemoveSymbols(script1)
S1parts = Methods.GetPOS(script1)
Methods.BubbleSort(S1parts, -1)
S1total = Methods.CountEntries(S1parts, -1)

script2 = Methods.ReadFromCSV("Script2Parsed", Methods.GetDirectoryMainCSV())
script2.pop(-1)
script2 = Methods.RemoveSymbols(script2)
S2parts = Methods.GetPOS(script2)
Methods.BubbleSort(S2parts, -1)
S2total = Methods.CountEntries(S2parts, -1)

S1partsByP = Methods.Copy(S1parts)
Methods.ConvertToPercentages(S1partsByP, S1total, -1)
S2partsByP = Methods.Copy(S2parts)
Methods.ConvertToPercentages(S2partsByP, S2total, -1)


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

Methods.WriteToCSV(countOutputHeader, S1parts, "Script1POSCountCompare", Methods.GetDirectoryDefaultCSV())


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

Methods.WriteToCSV(percentOutputHeader, S1partsByP, "Script1POSPercentCompare", Methods.GetDirectoryDefaultCSV())


S2parts = Methods.Copy(S1parts)
Methods.BubbleSort(S2parts, -1)
Methods.WriteToCSV(countOutputHeader, S2parts, "Script2POSCountCompare", Methods.GetDirectoryDefaultCSV())

S2partsByP = Methods.Copy(S1partsByP)
Methods.BubbleSort(S2partsByP, -1)
Methods.WriteToCSV(countOutputHeader, S2partsByP, "Script2POSPercentCompare", Methods.GetDirectoryDefaultCSV())

totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("Totals", Methods.GetDirectoryMainCSV())
totals[3] = ["POS", S1total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "Totals", Methods.GetDirectoryMainCSV())