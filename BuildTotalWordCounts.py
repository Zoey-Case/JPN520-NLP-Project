from GlobalMethods import Methods
import csv

CSVdir = "DATA"

P4POSdata = Methods.ReadCSV(CSVdir+"/Persona4POS.csv")
P5POSdata = Methods.ReadCSV(CSVdir+"/Persona5POS.csv")

P4wordCount = 0
P5wordCount = 0

print("Calculating total word counts.")

for entry in P4POSdata:
    if(entry[0] == "Auxiliary Symbol"):
        continue
    else:
        P4wordCount += int(entry[-1])

for entry in P5POSdata:
    if(entry[0] == "Auxiliary Symbol"):
        continue
    else:
        P5wordCount += int(entry[-1])

with open(CSVdir+"/WordCount.csv", "w") as CSV:
    wordCountOutput = csv.writer(CSV)
    wordCountOutput.writerow(["Persona 4","Persona 5"])
    wordCountOutput.writerow([P4wordCount,P5wordCount])