from GlobalMethods import Methods
import csv

CSVdir = "DATA"

##############################
##      GLOBAL METHODS      ##
##############################

def FindPOS(data):
    parts = [["Auxiliary Symbol", 0], ["Particle", 0], ["Auxiliary Verb", 0], ["Verb", 0], ["Adverb", 0], ["Prefix", 0], ["Pronoun", 0], ["Conjunction", 0], ["Noun", 0], ["い-Adjective", 0], ["Suffix", 0], ["Adnominal", 0], ["Interjection", 0], ["Code", 0], ["な-Adjective", 0], ["TOTAL", 0]]

    for index1 in data:
        print("SHECKING: ", index1)
        for index2 in parts:
            if(index1[2] == index2[0]):
                index2[1] += int(index1[3])
                parts[15][1] += int(index1[3])

    return parts


###################################
##      Processing The Data      ##
###################################

print("Processing Persona 4 POS Counts.")

P4lemmaList = Methods.ReadCSV(CSVdir+"/Persona4Words.csv")
P4parts = FindPOS(P4lemmaList)
P4partsTotal = P4parts.pop(-1)
P4partsSorted = Methods.BubbleSort(P4parts)

P4partsByPSorted = []
for entry in P4partsSorted:
    P4partsByPSorted.append([entry[0], (entry[1] / P4partsTotal[1] * 100)])

with open(CSVdir+"/Persona4POS.csv", "w") as CSV:
    P4partsOutput = csv.writer(CSV)
    P4partsOutput.writerow(["POS", "# Occurrences", "Percent Occurrences"])
    P4partsOutput.writerows(P4partsSorted)

with open(CSVdir+"/Persona4POSByP.csv", "w") as CSV:
    P4partsByPOutput = csv.writer(CSV)
    P4partsByPOutput.writerow(["POS", "# Occurrences"])
    P4partsByPOutput.writerows(P4partsByPSorted)

print("Compelted processing Persona 4 POS.")


print("Now processing Persona 5 POS.")

P5lemmaList = Methods.ReadCSV(CSVdir+"/Persona5Words.csv")
P5lemmaList.pop(-1)
P5parts = FindPOS(P5lemmaList)
P5partsTotal = P5parts.pop(-1)
P5partsSorted = Methods.BubbleSort(P5parts)

P5partsByPSorted = []
for entry in P5partsSorted:
    P5partsByPSorted.append([entry[0], (entry[1] / P5partsTotal[1]) * 100])

with open(CSVdir+"/Persona5POS.csv", "w") as CSV:
    P5partsOutput = csv.writer(CSV)
    P5partsOutput.writerow(["POS", "# Occurrences"])
    P5partsOutput.writerows(P5partsSorted)

with open(CSVdir+"/Persona5POSByP.csv", "w") as CSV:
    P5partsByPOutput = csv.writer(CSV)
    P5partsByPOutput.writerow(["POS", "# Occurrences"])
    P5partsByPOutput.writerows(P5partsByPSorted)

print("Compelted processing Persona 5 POS.\n\n")


##################################
##    COMPARING The Datasets    ##
##################################


# Compare POS occurrence COUNT || Persona 4 base.

print("Now compiling POS Comparisons by COUNT, with Persona 4 Base.")

P4partsComp = P4partsSorted.copy()
for P4entry in P4partsComp:
    wordFound = False
    
    for P5entry in P5partsSorted:
        if (str(P4entry[0]) == str(P5entry[0])):
            P4entry += [P5entry[-1]]
            wordFound = True
            P5partsSorted.remove(P5entry)

    if(not wordFound):
        P4entry += [0]

for P5entry in P5partsSorted:
    P4partsComp.append([P5entry[0]] + [P5entry[1]] + [0] + [P5entry[2]])

with open(CSVdir+"/Persona4POSComparison.csv", "w") as CSV:
    P4partsCompOutput = csv.writer(CSV)
    P4partsCompOutput.writerow(["POS", "P4 Occurrence Count", "P5 Occurrence Count"])
    P4partsCompOutput.writerows(P4partsComp)

print("Completed compiling POS Comparisons by count, with Persona 4 Base.")


# Compare POS occurrence percentage || Persona 4 base.

print("Now compiling POS Comparisons by PERCENTAGE, with Persona 4 Base.")

P4partsByPComp = P4partsByPSorted.copy()
for P4entry in P4partsByPComp:
    wordFound = False
    
    for P5entry in P5partsByPSorted:
        if (str(P4entry[0]) == str(P5entry[0])):
            P4entry += [P5entry[-1]]
            wordFound = True
            P5partsByPSorted.remove(P5entry)

    if(not wordFound):
        P4entry += [0]

for P5entry in P5partsByPSorted:
    P4partsByPComp.append([P5entry[0]] + [P5entry[1]] + [0] + [P5entry[2]])

with open(CSVdir+"/Persona4POSByPComparison.csv", "w") as CSV:
    P4partsByPCompOutput = csv.writer(CSV)
    P4partsByPCompOutput.writerow(["POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"])
    P4partsByPCompOutput.writerows(P4partsByPComp)

print("Completed compiling POS Comparisons by PERCENTAGE, with Persona 4 Base.")


# Compare POS occurrence count || Persona 5 base.

print("Now compiling POS Comparisons by COUNT, with Persona 5 Base.")

P5partsComp = Methods.BubbleSort(P4partsComp)

with open(CSVdir+"/Persona5POSComparison.csv", "w") as CSV:
    P5partsCompOutput = csv.writer(CSV)
    P5partsCompOutput.writerow(["POS", "P4 Occurrences", "P5 Occurrences"])
    P5partsCompOutput.writerows(P5partsComp)

print("Completed compiling POS Comparisons by COUNT, with Persona 5 Base.")


# Compare POS occurrence percentage || Persona 5 base.

print("Now compiling POS Comparisons by percentage, with Persona 5 Base.")

P5partsByPComp = Methods.BubbleSort(P4partsByPComp)

with open(CSVdir+"/Persona5POSByPComparison.csv", "w") as CSV:
    P5partsByPCompOutput = csv.writer(CSV)
    P5partsByPCompOutput.writerow(["POS", "P4 Occurrences", "P5 Occurrences"])
    P5partsByPCompOutput.writerows(P5partsByPComp)

print("Completed compiling POS Comparisons by percentage, with Persona 5 Base.")