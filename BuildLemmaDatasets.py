from GlobalMethods import Methods
import csv

CSVdir = "DATA"

# Read data in...
P4lemma = Methods.ReadCSV(CSVdir+"/Persona4Lemma.csv")
P5lemma = Methods.ReadCSV(CSVdir+"/Persona5Lemma.csv")

# P4lemmaByP = P4lemma.copy()
# P5lemmaByP = P5lemma.copy()

print("Compiling Lemma Comparisons by count, with Persona 4 Base.")

# Compare lemma occurrences by count || Persona 4 base.
for P4entry in P4lemma:
    wordFound = False
    
    for P5entry in P5lemma:
        if (str(P4entry[0]) == str(P5entry[0])):
            P4entry += [P5entry[-1]]
            wordFound = True
            P5lemma.remove(P5entry)

    if(not wordFound):
        P4entry += [0]

for P5entry in P5lemma:
    P4lemma.append([P5entry[0]] + [P5entry[1]] + [0] + [P5entry[2]])

with open(CSVdir+"/Persona4LemmaCountComparison.csv", "w") as CSV:
    P4lemmaOutput = csv.writer(CSV)
    P4lemmaOutput.writerow(["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"])
    P4lemmaOutput.writerows(P4lemma)
    
print("Completed compiling Lemma Comparisons by count, with Persona 4 Base.")

# print("Compiling Lemma Comparisons by percentage, with Persona 4 Base.")

# # Compare lemma occurrences by percentage || Persona 4 base.
# for P4entry in P4lemmaByP:
#     wordFound = False
    
#     for P5entry in P5lemmaByP:
#         if (str(P4entry[0]) == str(P5entry[0])):
#             P4entry += [P5entry[-1]]
#             wordFound = True
#             P5lemmaByP.remove(P5entry)

#     if(not wordFound):
#         P4entry += [0]

# for P5entry in P5lemmaByP:
#     P4lemmaByP.append([P5entry[0]] + [P5entry[1]] + [0] + [P5entry[2]])

# with open(CSVdir+"/Persona4LemmaPercentageComparison.csv", "w") as CSV:
#     P4lemmaByPOutput = csv.writer(CSV)
#     P4lemmaByPOutput.writerow(["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"])
#     P4lemmaByPOutput.writerows(P4lemmaByP)
    
# print("Completed compiling Lemma Comparisons by percentage, with Persona 4 Base.")

print("Now compiling Lemma Comparisons by count, with Persona 5 Base.")

# Compare lemma occurrences by count || Persona 5 base.
P5lemma = Methods.BubbleSort(P4lemma)

with open(CSVdir+"/Persona5LemmaCountComparison.csv", "w") as CSV:
    P5lemmaCompOutput = csv.writer(CSV)
    P5lemmaCompOutput.writerow(["Lemma", "POS", "P4 Occurrence Count", "P5 Occurrence Count"])
    P5lemmaCompOutput.writerows(P5lemma)

print("Completed compiling Lemma Comparisons by count, with Persona 5 Base.")

# print("Now compiling Lemma Comparisons by percentage, with Persona 5 Base.")

# # Compare lemma occurrences by percentage || Persona 5 base.
# P5lemmaByP = Methods.BubbleSort(P4lemmaByP)

# with open(CSVdir+"/Persona5LemmaPercentageComparison.csv", "w") as CSV:
#     P5lemmaByPCompOutput = csv.writer(CSV)
#     P5lemmaByPCompOutput.writerow(["Lemma", "POS", "P4 Occurrence Percentage", "P5 Occurrence Percentage"])
#     P5lemmaByPCompOutput.writerows(P5lemma)

# print("Completed compiling Lemma Comparisons by percentage, with Persona 5 Base.")