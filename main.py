from fugashi import Tagger
import csv

##############################
##      GLOBAL METHODS      ##
##############################

# BubbleSort algorithm (GREATEST to LEAST).
def BubbleSort(list):
    length = len(list)
    
    for outerIndex in range(length - 1):
        swapped = False
        
        for innerIndex in range(0, length - outerIndex - 1):
            if list[innerIndex + 1][1] > list[innerIndex][1]:
                swapped = True
                list[innerIndex + 1], list[innerIndex] = list[innerIndex], list[innerIndex + 1]

        if not swapped:
            return list
    
    return list

# Cleanup data to indicate individual variations of words and remove extraneous parts of speech.
def TextFixup(list):
    newList = []
    parts = [0, 0, 0] # Sentences, Phrases, Quotes
    teForm = ["て", "テ", "で", "デ"]
    joiners = ["っ", "ッ", "ん", "ン"]
    existenceVerbs = ["いる", "イル", "います", "ある", "アル", "あります"]
    genericVerbs = ["ます", "する", "します", ""]
    singleCharacters = ["し", "シ", "て", "テ", "た", "タ", "る", "ル", "れ", "レ", "え", "エ", "け", "ケ", "げ", "ゲ", "せ", "セ", "ぜ", "ゼ", "め", "メ", "てる", "ます"]
    potential = ["え", "エ", "け", "ケ", "て", "で", "ね", "", "め", "", "へ", "", "れ", "", "せ", ""]
    punctuation = ["!", "！", "？", "。"]
    quotations = ["『", "』", "“", "”"]
    special = ["(", "[", ")", "]", ")]", "_", "/", "<", ">", "＠", "％", "＆", "＊", "（", "）", "ー", "’", "：", "＞", "＜", "…"]
    operation = 0
    
    for index in range(len(list)):
        if len(newList) == 0:
            operation = 1
        elif (list[index][-1] in joiners and list[index + 1][0] in teForm):
            operation = 2
        elif list[index][0] in singleCharacters or list[index][0] in genericVerbs:
            operation = 3
        elif list[index][0] in existenceVerbs and newList[len(newList) - 1][-1] in teForm:
            operation = 3
        elif list[index][0] in teForm and (newList[len(newList) - 1][-1] in potential or newList[len(newList) - 1][-1] in joiners):
            operation = 3
        elif list[index] == "・" or list[index][0] == "の":
            operation = 4
        elif list[index][0] == "マス" and newList[len(newList) - 1][-1] == "リ":
            operation = 4
        elif list[index][0] in quotations:
            operation = 0
            parts[2] += 1
        elif list[index][0] in punctuation:
            operation = 0
            parts[0] += 1
            parts[1] += 1
        elif list[index][0] == "、":
            operation = 0
            parts[1] += 1
        elif list[index][0] in special:
            operation = 0
        else:
            operation = 1
        
        match operation:
            case 1:
                newList.append(list[index][0])
                print("Adding", list[index][0], "to list.")
            case 2:
                newList.append(list[index][0] + list[index + 1][0])
                print("Combining", list[index][0], "and", list[index + 1][0], ",and adding to list.")
                index += 1
            case 3:
                print("Attaching", list[index][0], "to", newList[len(newList) - 1], "at end of list.")
                newList[len(newList) - 1] += list[index][0]
            case 4:
                print("Attaching", list[index][0], "to", newList[len(newList) - 1], "at end of list.")
                newList[len(newList) - 1] += (list[index][0] + list[index + 1][0])
                index += 1
            case _:
                continue
    
    parts[2] /= 2
    
    return newList, parts


###################################
##      Processing The Data      ##
###################################

tagger = Tagger('-Owakati')

P4script = open("Persona4.txt", "r").read()
# P5script = open("Persona5.txt", "r").read()

# Separates individual words and inserts them into character array variables, using Fugashi's word tagger class.
# tagger.parse(P4script)
# P4text = [word.surface for word in tagger(P4script)]
# P5text = [word.surface for word in tagger(P5script)]

# P4textFixed, P4parts = TextFixup(P4text)
# P5textFixed, P5parts = TextFixup(P5text)

# Set up 2D arrays to store individual words and their number of occurrences.
P4words = []
# P5words = []
P4wordsFixed = []
# P5wordsFixed = []

tagger.parse(P4script)
P4text = []

for word in tagger(P4script):
    P4text.append([word, word.feature.lemma])

P4textFixed, P4parts = TextFixup(P4text)

# Creating Persona 4 Occurence List
for word in P4textFixed:
    location = 0
    wordAdd = True
    
    for term in P4wordsFixed:
        if(word == term[0]):
            P4wordsFixed[location][1] += 1
            wordAdd = False
            break
        else:
            location += 1
    
    if wordAdd:
        P4wordsFixed.append([word, 1])

# Creating Persona 5 Occurence List
# for word in P5textFixed:
#     location = 0
#     wordAdd = True
    
#     for term in P5wordsFixed:
#         if(word == term[0]):
#             P5wordsFixed[location][1] += 1
#             wordAdd = False
#             break
#         else:
#             location += 1
    
#     if wordAdd:
#         P5wordsFixed.append([word, 1])

# Creating Persona 4 Occurence List
for word in P4text:
    location = 0
    wordAdd = True
    
    for term in P4words:
        if(word == term[0]):
            P4words[location][1] += 1
            wordAdd = False
            break
        else:
            location += 1
    
    if wordAdd:
        P4words.append([word, 1])

# Creating Persona 5 Occurence List
# for word in P5text:
#     location = 0
#     wordAdd = True
    
#     for term in P5words:
#         if(word == term[0]):
#             P5words[location][1] += 1
#             wordAdd = False
#             break
#         else:
#             location += 1
    
#     if wordAdd:
#         P5words.append([word, 1])


P4fixedSorted = BubbleSort(P4wordsFixed)
# P5fixedSorted = BubbleSort(P5wordsFixed)
P4sorted = BubbleSort(P4words)
# P5sorted = BubbleSort(P5words)

# Save sorted Persona 4 list to spreadsheets.
with open("Persona4.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["Words", "Dictionary Form", "#"])
    P4output.writerows(P4sorted)

# Save sorted Persona 5 list to spreadsheets.
# with open("Persona5.csv", "w") as CSV:
#     P5output = csv.writer(CSV)
#     P5output.writerow(["Words", "Dictionary Form", "#"])
#     P5output.writerows(P5sorted)

# Save sorted Persona 4 Fixup list to spreadsheets.
with open("Persona4edited.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["Words", "#"])
    P4output.writerows(P4fixedSorted)
    P4output.writerow([" ", " ", " "])
    P4output.writerow(["Sentences", "Phrases", "Quotes"])
    P4output.writerow(P4parts)

# Save sorted Persona 5 Fixup list to spreadsheets.
# with open("Persona5edited.csv", "w") as CSV:
#     P5output = csv.writer(CSV)
#     P5output.writerow(["Words", "#"])
#     P5output.writerows(P5fixedSorted)
#     P5output.writerow([" ", " ", " "])
#     P5output.writerow(["Sentences", "Phrases", "Quotes"])
#     P5output.writerow(P5parts)