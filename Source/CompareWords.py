from MethodLibrary import Methods


countOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 COUNT", "SCRIPT 2 COUNT"]
percentOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 PERCENT", "SCRIPT 2 PERCENT"]


print("Reading in data.")
script1 = Methods.ReadFromCSV("Script1Parsed")
S1words = Methods.RemoveSymbols(script1)
S1total = Methods.CountEntries(S1words)
S1wordsByP = Methods.CopyArray(S1words)
Methods.ConvertToPercentages(S1wordsByP, S1total)

script2 = Methods.ReadFromCSV("Script2Parsed")
script2.pop(-1)
S2words = Methods.RemoveSymbols(script2)
S2total = Methods.CountEntries(S2words)
S2wordsByP = Methods.CopyArray(S2words)
Methods.ConvertToPercentages(S2wordsByP, S2total)



print("Compiling Word Comparisons by COUNT, using the first script as the base.")
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

# S2words.clear()
Methods.WriteToCSV(countOutputHeader, S1words, "CountCompareScript1Words")


print("Compiling Word Comparisons by PERCENTAGE, using the first script as the base.")
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

# S2wordsByP.clear()
Methods.WriteToCSV(percentOutputHeader, S1wordsByP, "PercentCompareScript1Words")


print("Compiling Word Comparisons by COUNT, using the second script as the base.")
S2words = Methods.CopyArray(S1words)
Methods.BubbleSort(S2words)
Methods.WriteToCSV(countOutputHeader, S2words, "CountCompareScript2Words")


print("Compiling Word Comparisons by PERCENTAGE, using the second script as the base.")
S2wordsByP = Methods.CopyArray(S1wordsByP)
Methods.BubbleSort(S2wordsByP)
Methods.WriteToCSV(percentOutputHeader, S2wordsByP, "PercentCompareScript2Words")

print("Appending TOTALS dataset")
totalsHeader = ["SET", "Script 1", "Script 2"]
totals = Methods.ReadFromCSV("_Totals")
totals[1] = ["WORDS", S1total, S2total]
Methods.WriteToCSV(totalsHeader, totals, "_Totals")

Methods.PromptComplete()
Methods.PromptContinue()