from fugashi import Tagger
import csv

tagger = Tagger('-Owakati')

##############################
##      GLOBAL METHODS      ##
##############################

# BubbleSort algorithm (GREATEST to LEAST).
def BubbleSort(list):
    length = len(list)
    
    for outerIndex in range(length - 1):
        swapped = False
        
        for innerIndex in range(0, length - outerIndex - 1):
            if list[innerIndex + 1][-1] > list[innerIndex][-1]:
                swapped = True
                list[innerIndex + 1], list[innerIndex] = list[innerIndex], list[innerIndex + 1]

        if not swapped:
            return list
    
    return list


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
        index = 0
        
        for index in range(len(word.pos)):
            if(word.pos[index] == ","):
                break
            else:
                POS += word.pos[index]
        
        text.append([word]+[word.feature.lemma]+[POS])
    
    return text


def DetermineOccurrences(text):
    list = []

    for word in text:
        location = 0
        wordAdd = True
        firstTerm = str(word[0])
        
        for term in list:
            secondTerm = str(term[0])
            
            if(firstTerm == secondTerm):
                print("P4, Match Found at: ", location)
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

# Initialize the tagger.
POStypes = ["補助記号", "助詞", "助動詞", "動詞", "副詞", "接頭辞", "代名詞", "接続詞", "名詞", "形容詞", "接尾辞"]
POStranslations = ["Auxiliary Symbol", "Particle", "Auxiliary Verb", "Verb", "Adverb", "Prefix", "Pronoun", "Conjunction", "Noun", "い-Adjective", "Suffix"]


P4script = open("Persona4.txt", "r").read()
P4text = ParseScript(P4script)
P4list = DetermineOccurrences(P4text)
P4parts = GetLemmaAndPOS(P4text)
P4listSorted = BubbleSort(P4list)
P4partsSorted = BubbleSort(P4parts)


# P5script = open("Persona5.txt", "r").read()
# P5text = ParseScript(P5script)
# P5list = DetermineOccurrences(P5text)
# P5parts = GetLemmaAndPOS(P5text)
# P5listSorted = BubbleSort(P5list)
# P5partsSorted = BubbleSort(P5parts)


# Save sorted Persona 4 lists to spreadsheets.
with open("Persona4.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["Word", "Lemma", "POS", "# Occurrences"])
    P4output.writerows(P4listSorted)

with open("Persona4Parts.csv", "w") as CSV:
    P4partsOutput = csv.writer(CSV)
    P4partsOutput.writerow(["Lemma", "POS", "# Occurrences"])
    P4partsOutput.writerows(P4partsSorted)


# Save sorted Persona 5 lists to spreadsheets.
# with open("Persona5.csv", "w") as CSV:
#     P5output = csv.writer(CSV)
#     P5output.writerow(["Word", "Lemma", "POS", "# Occurrences"])
#     P5output.writerows(P5listSorted)

# with open("Persona5Parts.csv", "w") as CSV:
#     P5partsOutput = csv.writer(CSV)
#     P5partsOutput.writerow(["Lemma", "POS", "# of Occurrences"])
#     P5partsOutput.writerows(P5partsSorted)