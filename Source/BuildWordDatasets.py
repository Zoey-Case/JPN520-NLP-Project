from GlobalMethods import Methods
from copy import deepcopy
import csv

CSVdir = "DATA"

P4words = []
P5words = []
P4wordsByP = []
P5wordsByP = []


# Read data in...
P4words = Methods.ReadCSV("DATA/Persona4Words.csv")

P5words = Methods.ReadCSV("DATA/Persona5Words.csv")
P5words.pop(-1)

# P4wordsByP = Methods.ReadCSV("DATA/Persona4Words.csv")
P4wordsByP = Methods.CopyArray(P4words)
P4wordsByP = Methods.ConvertToPercentages(P4wordsByP)

# P5wordsByP = Methods.ReadCSV("DATA/Persona5Words.csv")
# P5wordsByP.pop(-1)
P5wordsByP = Methods.CopyArray(P5words)
P5wordsByP = Methods.ConvertToPercentages(P5wordsByP)


# Compare word occurrences by count || Persona 4 base.
print("Compiling Word Comparisons by COUNT, with Persona 4 Base.")

for P4entry in P4words:
    wordFound = False
    
    for P5entry in P5words:
        if (str(P4entry[0]) == str(P5entry[0])):
            P4entry += [P5entry[-1]]
            wordFound = True
            P5words.remove(P5entry)
    
    if(not wordFound):
        P4entry += [0]

for P5entry in P5words:
    P4words.append([P5entry[0]] + [P5entry[1]] + [P5entry[2]] + [0] + [P5entry[3]])

with open(CSVdir+"/Persona4WordCountComparison.csv", "w") as CSV:
    P4wordsOutput = csv.writer(CSV)
    P4wordsOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"])
    P4wordsOutput.writerows(P4words)

print("Completed compiling Word Comparisons by COUNT, with Persona 4 Base.")


# Compare word occurrences by percentage || Persona 4 base.
print("Compiling Word Comparisons by PERCENTAGE, with Persona 4 Base.")

for P4entry in P4wordsByP:
    wordFound = False
    
    for P5entry in P5wordsByP:
        if (str(P4entry[0]) == str(P5entry[0])):
            P4entry += [P5entry[-1]]
            wordFound = True
            P5wordsByP.remove(P5entry)
    
    if(not wordFound):
        P4entry += [0]

for P5entry in P5wordsByP:
    P4wordsByP.append([P5entry[0]] + [P5entry[1]] + [P5entry[2]] + [0] + [P5entry[3]])

with open(CSVdir+"/Persona4WordPercentageComparison.csv", "w") as CSV:
    P4wordsByPOutput = csv.writer(CSV)
    P4wordsByPOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"])
    P4wordsByPOutput.writerows(P4wordsByP)

print("Completed compiling Word Comparisons by PERCENTAGE, with Persona 4 Base.")

# Compare word occurrences by count || Persona 5 base.
print("Now compiling Word Comparisons by COUNT, with Persona 5 Base.")

P5words = Methods.BubbleSort(P4words)

with open(CSVdir+"/Persona5WordCountComparison.csv", "w") as CSV:
    P5wordsOutput = csv.writer(CSV)
    P5wordsOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"])
    P5wordsOutput.writerows(P5words)

print("Completed compiling Word Comparisons by COUNT, with Persona 5 Base.")

# Compare word occurrences by count || Persona 5 base.
print("Now compiling Word Comparisons by PERCENTAGE, with Persona 5 Base.")

P5wordsByP = Methods.BubbleSort(P4wordsByP)

with open(CSVdir+"/Persona5WordPercentageComparison.csv", "w") as CSV:
    P5wordsByPOutput = csv.writer(CSV)
    P5wordsByPOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"])
    P5wordsByPOutput.writerows(P5wordsByP)

print("Completed compiling Word Comparisons by PERCENTAGE, with Persona 5 Base.")

input("Press ENTER to continue.")