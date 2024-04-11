from GlobalMethods import Methods
import csv

CSVdir = "DATA"

P4words = []
P5words = []

# Read data in...
P4words = Methods.ReadCSV("DATA/Persona4Words.csv")
P5words = Methods.ReadCSV("DATA/Persona5Words.csv")
P5words.pop(-1)

print("Compiling Word Comparisons, Persona 4 Base.")

# Compare word occurrences || Persona 4 base.
for index1 in P4words:
    wordFound = False
    
    for index2 in P5words:
        if (str(index1[0]) == str(index2[0])):
            index1 += [index2[-1]]
            wordFound = True
            P5words.remove(index2)
    
    if(not wordFound):
        index1 += [0]

for entry in P5words:
    P4words.append([entry[0]] + [entry[1]] + [entry[2]] + [0] + [entry[3]])

with open(CSVdir+"/Persona4WordsComparison.csv", "w") as CSV:
    P4wordsOutput = csv.writer(CSV)
    P4wordsOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrences", "P5 Occurrences"])
    P4wordsOutput.writerows(P4words)

print("Completed compiling Word Comparisons, Persona 4 Base.")
print("Now compiling Word Comparisons, Persona 5 Base.")

# Compare word occurrences || Persona 5 base.
P5words = Methods.BubbleSort(P4words)

with open(CSVdir+"/Persona5WordsComparison.csv", "w") as CSV:
    P5wordsOutput = csv.writer(CSV)
    P5wordsOutput.writerow(["Word", "Lemma", "POS", "P4 Occurrences", "P5 Occurrences"])
    P5wordsOutput.writerows(P5words)

print("Completed compiling Word Comparisons, Persona 5 Base.")