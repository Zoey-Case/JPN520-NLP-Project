from MethodLibrary import Methods

countOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 COUNT", "SCRIPT 2 COUNT"]
percentOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 PERCENT", "SCRIPT 2 PERCENT"]
dataset = []

customOptions = Methods.ReadFromCSV("_CustomOptions", Methods.GetDirectoryMainCSV())
fileNum = customOptions.pop(-1)
fileNum = int(fileNum.pop(-1))
type = customOptions.pop(-1)
type = str(type.pop(-1))

for entry in customOptions:
    if entry[1] == "1":
        dataset += Methods.Extract(entry[0], type)
        
S1dataset = Methods.Copy(dataset)
Methods.BubbleSort(S1dataset, -2)
S1total = Methods.CountEntries(S1dataset, -2)

S2dataset = Methods.Copy(S1dataset)
Methods.BubbleSort(S2dataset, -1)
S2total = Methods.CountEntries(S2dataset, -1)

S1datasetByP = Methods.Copy(S1dataset)
Methods.ConvertToPercentages(S1datasetByP, S1total, -1)
Methods.ConvertToPercentages(S1datasetByP, S2total, -2)
S2datasetByP = Methods.Copy(S2dataset)
Methods.ConvertToPercentages(S2datasetByP, S1total, -1)
Methods.ConvertToPercentages(S2datasetByP, S2total, -2)

Methods.WriteToCSV(countOutputHeader, S1dataset, "Script1CustomCountCompare-" + str(fileNum), Methods.GetDirectoryCustomCSV())
Methods.WriteToCSV(countOutputHeader, S2dataset, "Script2CustomCountCompare-" + str(fileNum), Methods.GetDirectoryCustomCSV())
Methods.WriteToCSV(countOutputHeader, S1datasetByP, "Script1CustomPercentCompare-" + str(fileNum), Methods.GetDirectoryCustomCSV())
Methods.WriteToCSV(countOutputHeader, S2datasetByP, "Script2CustomPercentCompare-" + str(fileNum), Methods.GetDirectoryCustomCSV())

Methods.DeleteCSVfile("_CustomOptions", Methods.GetDirectoryMainCSV())

