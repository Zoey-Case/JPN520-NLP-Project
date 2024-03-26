from fugashi import Tagger
import csv

tagger = Tagger('-Owakati')
P4script = open("Persona4.txt", "r").read()

tagger.parse(P4script)
P4words = []

for word in tagger(P4script):
    P4words.append([word, word.feature.lemma])

with open("Persona4.csv", "w") as CSV:
    P4output = csv.writer(CSV)
    P4output.writerow(["Word", "Dictionary Form"])
    P4output.writerows(P4words)