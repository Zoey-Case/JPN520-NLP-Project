from MethodLibrary import Methods

countOutputHeader = ["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"]
percentOutputHeader = ["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"]

script1 = Methods.ReadFromCSV("Script1Parsed", Methods.GetDirectoryMainCSV())
script1 = Methods.RemoveSymbols(script1)
S1lemma = Methods.GetLemmaAndPOS(script1)
Methods.BubbleSort(S1lemma, -1)
S1total = Methods.CountEntries(S1lemma, -1)

script2 = Methods.ReadFromCSV("Script2Parsed", Methods.GetDirectoryMainCSV())
script2.pop(-1)
script2 = Methods.RemoveSymbols(script2)
S2lemma = Methods.GetLemmaAndPOS(script2)
Methods.BubbleSort(S2lemma, -1)
S2total = Methods.CountEntries(S2lemma, -1)

S1lemmaByP = Methods.Copy(S1lemma)
Methods.ConvertToPercentages(S1lemmaByP, S1total, -1)
S2lemmaByP = Methods.Copy(S2lemma)
Methods.ConvertToPercentages(S2lemmaByP, S2total, -1)

for S1entry in S1lemma:
    wordFound = False
    
    for S2entry in S2lemma:
        if (S1entry[0] == S2entry[0]):
            S1entry += [S2entry[-1]]
            wordFound = True
            S2lemma.remove(S2entry)

    if(not wordFound):
        S1entry += [0]

for S2entry in S2lemma:
    S1lemma.append([S2entry[0]] + [S2entry[1]] + [0] + [S2entry[2]])

Methods.WriteToCSV(countOutputHeader, S1lemma, "Script1LemmaCountCompare", Methods.GetDirectoryDefaultCSV())

for S1entry in S1lemmaByP:
    wordFound = False
    
    for S2entry in S2lemmaByP:
        if (str(S1entry[0]) == str(S2entry[0])):
            S1entry += [S2entry[-1]]
            wordFound = True
            S2lemmaByP.remove(S2entry)

    if(not wordFound):
        S1entry += [0]

for S2entry in S2lemmaByP:
    S1lemmaByP.append([S2entry[0]] + [S2entry[1]] + [0] + [S2entry[2]])

Methods.WriteToCSV(countOutputHeader, S1lemmaByP, "Script1LemmaPercentCompare", Methods.GetDirectoryDefaultCSV())

S2lemma = Methods.BubbleSort(S1lemma, -1)
Methods.WriteToCSV(countOutputHeader, S2lemma, "Script2LemmaCountCompare", Methods.GetDirectoryDefaultCSV())

S2lemmaByP = Methods.BubbleSort(S1lemmaByP, -1)
Methods.WriteToCSV(countOutputHeader, S2lemmaByP, "Script2LemmaPercentCompare", Methods.GetDirectoryDefaultCSV())

totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("Totals", Methods.GetDirectoryMainCSV())
totals[2] = ["LEMMA", S2total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "Totals", Methods.GetDirectoryMainCSV())