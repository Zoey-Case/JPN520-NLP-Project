from fugashi import Tagger
from MethodLibrary import Methods

CSVdir = "DATA"
tagger = Tagger('-Owakati')

def ParseScript(script):
    text = []
    
    tagger.parse(script)

    for word in tagger(script):
        POS = ""
        
        for index in range(len(word.pos)):
            if(word.pos[index] == ","):
                break
            else:
                POS += word.pos[index]
        
        POS = Methods.TranslatePOS(POS)
        text.append([word]+[word.feature.lemma]+[POS])
    
    return text

outputHeader = ["WORD", "LEMMA", "POS", "OCCURRENCE COUNT"]

name = "Persona4"
print("PARSING SCRIPT 1.")
script1 = open("Script Files/" + name + ".txt", "r").read()
S1words = ParseScript(script1)
S1words = Methods.FindOccurrences(S1words)
Methods.BubbleSort(S1words)
S1total = Methods.CountEntries(S1words)
Methods.WriteToCSV(outputHeader, S1words, "Script1Parsed")
Methods.PromptComplete()

name = "Persona5"
print("PARSING SCRIPT 2.")
script2 = open("Script Files/" + name + ".txt", "r").read()
S2words = ParseScript(script2)
S2words = Methods.FindOccurrences(S2words)
Methods.BubbleSort(S2words)
S2total = Methods.CountEntries(S2words)
Methods.WriteToCSV(outputHeader, S2words, "Script2Parsed")
Methods.PromptComplete()

print("Creating TOTALS dataset")
totalsHeader = ["SET", "Script 1", "Script 2"]
initialTotals = ["ALL", S1total, S2total]
totals = Methods.InitializeTotalsSet(initialTotals)
Methods.WriteToCSV(totalsHeader, totals, "_Totals")
Methods.PromptComplete()