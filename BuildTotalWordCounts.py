from GlobalMethods import Methods
import csv

CSVdir = "DATA"

P4POSdata = Methods.ReadCSV(CSVdir+"/Persona4POS.csv")
P5POSdata = Methods.ReadCSV(CSVdir+"/Persona5POS.csv")

P4wordCount = [0,0]
P5wordCount = [0,0]

print("Calculating total word counts, including Particles.")

for entry in P4POSdata:
    if(entry[0] == "Auxiliary Symbol"):
        continue
    else:
        P4wordCount[0] += int(entry[-1])

for entry in P5POSdata:
    if(entry[0] == "Auxiliary Symbol"):
        continue
    else:
        P5wordCount[0] += int(entry[-1])


print("Now calculating total word counts, not including particles.")

for entry in P4POSdata:
    if(entry[0] == "Auxiliary Symbol" or entry[0] == "Particle"):
        continue
    else:
        P4wordCount[1] += int(entry[-1])

for entry in P5POSdata:
    if(entry[0] == "Auxiliary Symbol" or entry[0] == "Particle"):
        continue
    else:
        P5wordCount[1] += int(entry[-1])

with open(CSVdir+"/WordCount.csv", "w") as CSV:
    wordCountOutput = csv.writer(CSV)
    wordCountOutput.writerow(["Parameter","Persona 4","Persona 5"])
    wordCountOutput.writerow(["With Particles",P4wordCount[0],P5wordCount[0]])
    wordCountOutput.writerow(["Without Particles",P4wordCount[1],P5wordCount[1]])