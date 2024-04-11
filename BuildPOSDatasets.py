from GlobalMethods import Methods
import csv

CSVdir = "DATA"

##############################
##      GLOBAL METHODS      ##
##############################

def FindPOS(data):
    parts = [["Auxiliary Symbol", 0], ["Particle", 0], ["Auxiliary Verb", 0], ["Verb", 0], ["Adverb", 0], ["Prefix", 0], ["Pronoun", 0], ["Conjunction", 0], ["Noun", 0], ["い-Adjective", 0], ["Suffix", 0], ["Adnominal", 0], ["Interjection", 0], ["Code", 0], ["な-Adjective", 0]]

    for index1 in data:
        for index2 in parts:
            if(index1[1] == index2[0]):
                index2[1] += int(index1[2])
    
    return parts
    

###################################
##      Processing The Data      ##
###################################

print("Processing Persona 4 POS.")

P4lemmaList = Methods.ReadCSV(CSVdir+"/Persona4Lemma.csv")
P4parts = FindPOS(P4lemmaList)
P4partsSorted = Methods.BubbleSort(P4parts)

with open(CSVdir+"/Persona4POS.csv", "w") as CSV:
    P4partsOutput = csv.writer(CSV)
    P4partsOutput.writerow(["POS", "# Occurrences"])
    P4partsOutput.writerows(P4partsSorted)

print("Compelted processing Persona 4 POS.")
print("Now processing Persona 5 POS.")

P5lemmaList = Methods.ReadCSV(CSVdir+"/Persona5Lemma.csv")
P5parts = FindPOS(P5lemmaList)
P5partsSorted = Methods.BubbleSort(P5parts)

with open(CSVdir+"/Persona5POS.csv", "w") as CSV:
    P5partsOutput = csv.writer(CSV)
    P5partsOutput.writerow(["POS", "# Occurrences"])
    P5partsOutput.writerows(P5partsSorted)

print("Compelted processing Persona 5 POS.\n\n")

print("Now compiling POS Comparisons, Persona 4 Base.")

# Compare POS occurrences || Persona 4 base.
P4partsComp = P4partsSorted.copy()
for index1 in P4partsComp:
    wordFound = False
    
    for index2 in P5partsSorted:
        if (str(index1[0]) == str(index2[0])):
            index1 += [index2[-1]]
            wordFound = True
            P5partsSorted.remove(index2)

    if(not wordFound):
        index1 += [0]

for index in P5partsSorted:
    P4partsComp.append([index[0]] + [index[1]] + [0] + [index[2]])

with open(CSVdir+"/Persona4POSComparison.csv", "w") as CSV:
    P4partsCompOutput = csv.writer(CSV)
    P4partsCompOutput.writerow(["POS", "P4 Occurrences", "P5 Occurrences"])
    P4partsCompOutput.writerows(P4partsComp)

print("Completed compiling POS Comparisons, Persona 4 Base.")
print("Now compiling POS Comparisons, Persona 5 Base.")

# Compare POS occurrences || Persona 5 base.
P5partsComp = Methods.BubbleSort(P4partsComp)
with open(CSVdir+"/Persona5POSComparison.csv", "w") as CSV:
    P5partsCompOutput = csv.writer(CSV)
    P5partsCompOutput.writerow(["POS", "P4 Occurrences", "P5 Occurrences"])
    P5partsCompOutput.writerows(P5partsComp)

print("Completed compiling POS Comparisons, Persona 5 Base.")