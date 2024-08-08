from fugashi import Tagger
from GlobalMethods import Methods
import csv


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
        
        part = Methods.TranslatePOS(POS)
        text.append([word]+[word.feature.lemma]+[part])
    
    return text


print("PARSING PERSONA 4 SCRIPT.")

P4script = open("Text Files/Persona4.txt", "r").read()
P4text = ParseScript(P4script)
P4textTrans = Methods.TranslatePOS(P4text)
P4words = Methods.FindOccurrences(P4textTrans)

P4wordsSorted = Methods.BubbleSort(P4words)
with open(CSVdir+"/Persona4Words.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["WORD", "LEMMA", "POS", "OCCURRENCE COUNT"])
    P4output.writerows(P4wordsSorted)


print("COMPLETE.")

print("PARSING PERSONA 5 SCRIPT.")

P5script = open("Text Files/Persona5.txt", "r").read()
P5text = ParseScript(P5script)
P5textTrans = Methods.TranslatePOS(P5text)
P5words = Methods.FindOccurrences(P5textTrans)

P5wordsSorted = Methods.BubbleSort(P5words)
with open(CSVdir+"/Persona5Words.csv", "w") as CSV:
    P5output = csv.writer(CSV)
    P5output.writerow(["WORD", "LEMMA", "POS", "OCCURRENCE COUNT"])
    P5output.writerows(P5wordsSorted)
    
print("COMPLETE.")