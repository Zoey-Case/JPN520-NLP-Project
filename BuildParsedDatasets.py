from fugashi import Tagger
from GlobalMethods import Methods
import time
import csv


CSVdir = "DATA"
tagger = Tagger('-Owakati')

##############################
##      GLOBAL METHODS      ##
##############################

def TranslatePOS(POS):
    POStypes = ["補助記号", "助詞", "助動詞", "動詞", "副詞", "接頭辞", "代名詞", "接続詞", "名詞", "形容詞", "接尾辞", "連体詞", "感動詞", "記号", "形状詞"]
    POStranslations = ["Auxiliary Symbol", "Particle", "Auxiliary Verb", "Verb", "Adverb", "Prefix", "Pronoun", "Conjunction", "Noun", "い-Adjective", "Suffix", "Adnominal", "Interjection", "Code", "な-Adjective"]
    
    for index in range(len(POStypes)):
        if (POS == POStypes[index]):
            POS = POStranslations[index]
    
    return POS


def GetLemmaAndPOS(list):
    length = len(list)
    terms = []
    
    for index in range(length - 1):
        incremented = False
        
        for term in terms:
            if(list[index][1] == term[0]):
                term[2] += 1
                incremented = True
                break
            
        if(incremented == False):
            # TODO: Setup so only first POS entry gets added.
            terms.append([list[index][1]]+[list[index][2]]+[1])
    
    return terms


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
        
        part = TranslatePOS(POS)
        text.append([word]+[word.feature.lemma]+[part])
    
    return text


def FindOccurrences(text):
    list = []

    for word in text:
        location = 0
        wordAdd = True
        firstTerm = str(word[0])
        
        for term in list:
            secondTerm = str(term[0])
            
            if(firstTerm == secondTerm):
                list[location][3] += 1
                wordAdd = False
                break
            else:
                location += 1
        
        if wordAdd:
            list.append(word+[1])
    
    return list


###################################
##      Processing The Data      ##
###################################

print("Processing Persona 4 Script.")

# Persona 4 Data...
P4script = open("Text Files/Persona4.txt", "r").read()
P4text = ParseScript(P4script)
P4textTrans = TranslatePOS(P4text)
P4list = FindOccurrences(P4textTrans)
P4lemma = GetLemmaAndPOS(P4textTrans)

P4listSorted = Methods.BubbleSort(P4list)
with open(CSVdir+"/Persona4Words.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["Word", "Lemma", "POS", "# Occurrences"])
    P4output.writerows(P4listSorted)

P4lemmaSorted = Methods.BubbleSort(P4lemma)
with open(CSVdir+"/Persona4Lemma.csv", "w") as CSV:
    P4lemmaOutput = csv.writer(CSV)
    P4lemmaOutput.writerow(["Lemma", "POS", "# Occurrences"])
    P4lemmaOutput.writerows(P4lemmaSorted)
    
print("Completed processing Persona 4 Script.")
print("Now processing Persona 5 Script.")

# Persona 5 Data...
P5script = open("Text Files/Persona5.txt", "r").read()
P5text = ParseScript(P5script)
P5textTrans = TranslatePOS(P5text)
P5list = FindOccurrences(P5textTrans)
P5lemma = GetLemmaAndPOS(P5textTrans)

P5listSorted = Methods.BubbleSort(P5list)
with open(CSVdir+"/Persona5Words.csv", "w") as CSV:
    P5output = csv.writer(CSV)
    P5output.writerow(["Word", "Lemma", "POS", "# Occurrences"])
    P5output.writerows(P5listSorted)

P5lemmaSorted = Methods.BubbleSort(P5lemma)
with open(CSVdir+"/Persona5Lemma.csv", "w") as CSV:
    P5lemmaOutput = csv.writer(CSV)
    P5lemmaOutput.writerow(["Lemma", "POS", "# of Occurrences"])
    P5lemmaOutput.writerows(P5lemmaSorted)
    
print("Completed processing Persona 4 Script.")