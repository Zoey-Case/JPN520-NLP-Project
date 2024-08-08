import csv
import os

class GlobalMethods:
    # BubbleSort algorithm (GREATEST to LEAST).
    def BubbleSort(self, list): 
        length = len(list)
        
        for outerIndex in range(length - 1):
            swapped = False
            
            for innerIndex in range(0, length - outerIndex - 1):
                if (int(list[innerIndex + 1][-1]) > int(list[innerIndex][-1])):
                    swapped = True
                    list[innerIndex + 1], list[innerIndex] = list[innerIndex], list[innerIndex + 1]

            if not swapped:
                return list
        
        return list


    def ReadCSV(self, fileName):
        data = []
        
        with open(fileName, newline='') as CSV:
            data += csv.reader(CSV, delimiter=',', lineterminator='\r', quotechar='|')
        
        data.pop(0)
        return data
    
    
    def ConvertToPercentages(self, text):
        totalWords = 0
        list = []
        
        for word in text:
            totalWords += int(word[-1])
        
        for word in text:
            newEntry = word
            newEntry[-1] = (int(newEntry[-1]) / totalWords) * 100
            list.append(newEntry)
        
        return list
    
    
    def TranslatePOS(self, POS):
        POStypes = ["補助記号", "助詞", "助動詞", "動詞", "副詞", "接頭辞", "代名詞", "接続詞", "名詞", "形容詞", "接尾辞", "連体詞", "感動詞", "記号", "形状詞"]
        POStranslations = ["Auxiliary Symbol", "Particle", "Auxiliary Verb", "Verb", "Adverb", "Prefix", "Pronoun", "Conjunction", "Noun", "い-Adjective", "Suffix", "Adnominal", "Interjection", "Code", "な-Adjective"]
        
        for index in range(len(POStypes)):
            if (POS == POStypes[index]):
                POS = POStranslations[index]
        
        return POS


    def FindOccurrences(self, text):
        list = []

        for word in text:
            location = 0
            wordAdd = True
            firstTerm = str(word[0])
            
            for term in list:
                secondTerm = str(term[0])
                
                if(firstTerm == secondTerm):
                    list[location][3] += 1
                    wordAdd = False
                    break
                else:
                    location += 1
            
            if wordAdd:
                list.append(word+[1])
        
        return list
    
    
    def SetUpDataTracker(self):
        dataTracker = []
        
        if os.path.exists("Source/OperationTracker.csv"):
            dataTracker = self.ReadCSV("Source/OperationTracker.csv")
        else:
            dataTracker = [["Parsed Datasets Built", "NO"],
                           ["Word Comparison Dataset Built", "NO"],
                           ["Lemma Comparison Dataset Built", "NO"],
                           ["POS Datasets Built", "NO"],
                           ["Word Counts Built", "NO"]]
        
        return dataTracker


    def CopyArray(self, arrayToCopy):
        copy = []
        
        for item in arrayToCopy:
            copy.append(item[:])
        
        return copy


    def ResetApp(self, trackerArray, CSVdir):
        os.system("clear")
        
        for item in trackerArray:
            item[1] = "NO"
        
        # Delete Persona 4 files

        if os.path.exists(CSVdir+"/Persona4Lemma.csv"):
            os.remove(CSVdir+"/Persona4Lemma.csv")
        if os.path.exists(CSVdir+"/Persona4LemmaCountComparison.csv"):
            os.remove(CSVdir+"/Persona4LemmaCountComparison.csv")
        if os.path.exists(CSVdir+"/Persona4LemmaPercentageComparison.csv"):
            os.remove(CSVdir+"/Persona4LemmaPercentageComparison.csv")
        if os.path.exists(CSVdir+"/Persona4POS.csv"):
            os.remove(CSVdir+"/Persona4POS.csv")
        if os.path.exists(CSVdir+"/Persona4POSComparison.csv"):
            os.remove(CSVdir+"/Persona4POSComparison.csv")
        if os.path.exists(CSVdir+"/Persona4Words.csv"):
            os.remove(CSVdir+"/Persona4Words.csv")
        if os.path.exists(CSVdir+"/Persona4WordsByP.csv"):
            os.remove(CSVdir+"/Persona4WordsByP.csv")
        if os.path.exists(CSVdir+"/Persona4WordCountComparison.csv"):
            os.remove(CSVdir+"/Persona4WordCountComparison.csv")
        if os.path.exists(CSVdir+"/Persona4WordPercentageComparison.csv"):
            os.remove(CSVdir+"/Persona4WordPercentageComparison.csv")


        # Delete Persona 5 files

        if os.path.exists(CSVdir+"/Persona5Lemma.csv"):
            os.remove(CSVdir+"/Persona5Lemma.csv")
        if os.path.exists(CSVdir+"/Persona5LemmaCountComparison.csv"):
            os.remove(CSVdir+"/Persona5LemmaCountComparison.csv")
        if os.path.exists(CSVdir+"/Persona5LemmaPercentageComparison.csv"):
            os.remove(CSVdir+"/Persona5LemmaPercentageComparison.csv")
        if os.path.exists(CSVdir+"/Persona5POS.csv"):
            os.remove(CSVdir+"/Persona5POS.csv")
        if os.path.exists(CSVdir+"/Persona5POSComparison.csv"):
            os.remove(CSVdir+"/Persona5POSComparison.csv")
        if os.path.exists(CSVdir+"/Persona5Words.csv"):
            os.remove(CSVdir+"/Persona5Words.csv")
        if os.path.exists(CSVdir+"/Persona5WordsByP.csv"):
            os.remove(CSVdir+"/Persona5WordsByP.csv")
        if os.path.exists(CSVdir+"/Persona5WordCountComparison.csv"):
            os.remove(CSVdir+"/Persona5WordCountComparison.csv")
        if os.path.exists(CSVdir+"/Persona5WordPercentageComparison.csv"):
            os.remove(CSVdir+"/Persona5WordPercentageComparison.csv")
        
        print("APPLICATION RESET.\n")

Methods = GlobalMethods()