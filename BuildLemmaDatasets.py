from GlobalMethods import Methods
import csv

CSVdir = "DATA"

# Read data in...
P4lemma = Methods.ReadCSV(CSVdir+"/Persona4Lemma.csv")
P5lemma = Methods.ReadCSV(CSVdir+"/Persona5Lemma.csv")

print("Compiling Lemma Comparisons, Persona 4 Base.")

# Compare lemma occurrences || Persona 4 base.
for index1 in P4lemma:
    wordFound = False
    
    for index2 in P5lemma:
        if (str(index1[0]) == str(index2[0])):
            index1 += [index2[-1]]
            wordFound = True
            P5lemma.remove(index2)

    if(not wordFound):
        index1 += [0]

for index in P5lemma:
    P4lemma.append([index[0]] + [index[1]] + [0] + [index[2]])

with open(CSVdir+"/Persona4LemmaComparison.csv", "w") as CSV:
    P4lemmaOutput = csv.writer(CSV)
    P4lemmaOutput.writerow(["Lemma", "POS", "P4 Occurrences", "P5 Occurrences"])
    P4lemmaOutput.writerows(P4lemma)
    
print("Completed compiling Lemma Comparisons, Persona 4 Base.")
print("Now compiling Lemma Comparisons, Persona 5 Base.")

# Compare lemma occurrences || Persona 5 base.
P5lemma = Methods.BubbleSort(P4lemma)

with open(CSVdir+"/Persona5LemmaComparison.csv", "w") as CSV:
    P5lemmaCompOutput = csv.writer(CSV)
    P5lemmaCompOutput.writerow(["Lemma", "POS", "P4 Occurrences", "P5 Occurrences"])
    P5lemmaCompOutput.writerows(P5lemma)

print("Completed compiling Lemma Comparisons, Persona 5 Base.")