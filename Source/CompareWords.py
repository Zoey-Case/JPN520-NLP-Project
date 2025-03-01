from MethodLibrary import Methods

countOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 COUNT", "SCRIPT 2 COUNT"]
percentOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 PERCENT", "SCRIPT 2 PERCENT"]

script1 = Methods.ReadFromCSV("Script1Parsed", Methods.GetDirectoryMainCSV())
S1words = Methods.RemoveSymbols(script1)
S1total = Methods.CountEntries(S1words, -1)
S1wordsByP = Methods.Copy(S1words)
Methods.ConvertToPercentages(S1wordsByP, S1total, -1)

script2 = Methods.ReadFromCSV("Script2Parsed", Methods.GetDirectoryMainCSV())
script2.pop(-1)
S2words = Methods.RemoveSymbols(script2)
S2total = Methods.CountEntries(S2words, -1)
S2wordsByP = Methods.Copy(S2words)
Methods.ConvertToPercentages(S2wordsByP, S2total, -1)

for S1entry in S1words:
    wordFound = False
    
    for S2entry in S2words:
        if (str(S1entry[0]) == str(S2entry[0])):
            S1entry += [S2entry[-1]]
            wordFound = True
            S2words.remove(S2entry)
    
    if(not wordFound):
        S1entry += [0]

for S2entry in S2words:
    S1words.append([S2entry[0]] + [S2entry[1]] + [S2entry[2]] + [0] + [S2entry[3]])

Methods.WriteToCSV(countOutputHeader, S1words, "Script1WordsCountCompare", Methods.GetDirectoryDefaultCSV())

for S1entry in S1wordsByP:
    wordFound = False
    
    for S2entry in S2wordsByP:
        if (str(S1entry[0]) == str(S2entry[0])):
            S1entry += [S2entry[-1]]
            wordFound = True
            S2wordsByP.remove(S2entry)
    
    if(not wordFound):
        S1entry += [0]

for S2entry in S2wordsByP:
    S1wordsByP.append([S2entry[0]] + [S2entry[1]] + [S2entry[2]] + [0] + [S2entry[3]])

Methods.WriteToCSV(percentOutputHeader, S1wordsByP, "Script1WordsPercentCompare", Methods.GetDirectoryDefaultCSV())

S2words = Methods.Copy(S1words)
Methods.BubbleSort(S2words, -1)
Methods.WriteToCSV(countOutputHeader, S2words, "Script2WordsCountCompare", Methods.GetDirectoryDefaultCSV())

S2wordsByP = Methods.Copy(S1wordsByP)
Methods.BubbleSort(S2wordsByP, -1)
Methods.WriteToCSV(percentOutputHeader, S2wordsByP, "Script2WordsPercentCompare", Methods.GetDirectoryDefaultCSV())

totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("Totals", Methods.GetDirectoryMainCSV())
totals[1] = ["WORDS", S1total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "Totals", Methods.GetDirectoryMainCSV())