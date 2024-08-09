from MethodLibrary import Methods


countOutputHeader = ["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"]
percentOutputHeader = ["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"]

print("Reading in data.")
script1 = Methods.ReadFromCSV("Script1Parsed")
script1 = Methods.RemoveSymbols(script1)
S1lemma = Methods.GetLemmaAndPOS(script1)
Methods.BubbleSort(S1lemma)
S1total = Methods.CountEntries(S1lemma)

script2 = Methods.ReadFromCSV("Script2Parsed")
script2.pop(-1)
script2 = Methods.RemoveSymbols(script2)
S2lemma = Methods.GetLemmaAndPOS(script2)
Methods.BubbleSort(S2lemma)
S2total = Methods.CountEntries(S2lemma)

S1lemmaByP = Methods.CopyArray(S1lemma)
Methods.ConvertToPercentages(S1lemmaByP, S1total)
S2lemmaByP = Methods.CopyArray(S2lemma)
Methods.ConvertToPercentages(S2lemmaByP, S2total)


print("Compiling Lemma Comparisons by COUNT, with Script 1 Base.")
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

Methods.WriteToCSV(countOutputHeader, S1lemma, "CountCompareS1Lemma")


print("Compiling Lemma Comparisons by PERCENTAGE, with Script 1 Base.")
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

Methods.WriteToCSV(countOutputHeader, S1lemmaByP, "PercentCompareS1Lemma")


print("Now compiling Lemma Comparisons by COUNT, with Script 2 Base.")
S2lemma = Methods.BubbleSort(S1lemma)
Methods.WriteToCSV(countOutputHeader, S2lemma, "CountCompareS2Lemma")


print("Now compiling Lemma Comparisons by PERCENTAGE, with Script 2 Base.")
S2lemmaByP = Methods.BubbleSort(S1lemmaByP)
Methods.WriteToCSV(countOutputHeader, S2lemmaByP, "PercentCompareS2Lemma")


print("Appending TOTALS dataset")
totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("_Totals")
totals[2] = ["LEMMA", S2total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "_Totals")


Methods.PromptComplete()
Methods.PromptContinue()