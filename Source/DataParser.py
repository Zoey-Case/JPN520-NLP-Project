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
totalsHeader = ["SET"]
initialTotals = ["ALL"]

for index in range(Methods.GetNumScripts()):
    name = Methods.GetScriptName(index)
    script = open("Script Files/" + str(name) + ".txt", "r").read()
    words = ParseScript(script)

    for entry in words:
        if(entry[1] == None):
            entry[1] = entry[0]

    words = Methods.FindOccurrences(words)
    Methods.BubbleSort(words, -1)
    total = Methods.CountEntries(words, -1)
    Methods.WriteToCSV(outputHeader, words, "Script" + str(index + 1) + "Parsed", Methods.GetDirectoryMainCSV())
    
    totalsHeader += ("Script " + str(index + 1))
    initialTotals += [total]


totals = Methods.InitializeTotalsSet(initialTotals)
Methods.WriteToCSV(totalsHeader, totals, "Totals", Methods.GetDirectoryMainCSV())