import csv
import os
import tkinter as tk
from tkinter import ttk
from threading import Thread

CSVdir = "DATA/"

class Methods:
    # BubbleSort algorithm (GREATEST to LEAST).
    def BubbleSort(self, data): 
        length = len(data)
        for outerIndex in range(length - 1):
            swapped = False
            for innerIndex in range(0, length - outerIndex - 1):
                if (float(data[innerIndex + 1][-1]) > float(data[innerIndex][-1])):
                    swapped = True
                    data[innerIndex + 1], data[innerIndex] = data[innerIndex], data[innerIndex + 1]
            if not swapped:
                return data
    
    def BubbleSortAlt(self, data): 
        length = len(data)
        for outerIndex in range(length - 1):
            swapped = False
            for innerIndex in range(0, length - outerIndex - 1):
                if (float(data[innerIndex + 1][-2]) > float(data[innerIndex][-2])):
                    swapped = True
                    data[innerIndex + 1], data[innerIndex] = data[innerIndex], data[innerIndex + 1]
            if not swapped:
                return data
    
    
    def ClearScreen(self):
        os.system("clear")
    
    
    def ConvertToPercentages(self, text, total):
        for word in text:
            word[-1] = (float(word[-1]) / float(total)) * 100
    
    def ConvertToPercentagesAlt(self, text, total):
        for word in text:
            word[-2] = (float(word[-2]) / float(total)) * 100
    
    
    def CopyArray(self, arrayToCopy):
        copy = []
        for item in arrayToCopy:
            copy.append(item[:])
        return copy

    
    def CountEntries(self, data):
        total = 0
        for word in data:
            total += int(word[-1])
        return total
    
    
    def CountEntriesAlt(self, data):
        total = 0
        for word in data:
            total += int(word[-2])
        return total
    
    
    def Extract(self, POS):
        script1 = self.ReadFromCSV("Script1Parsed")
        script1.pop(-1)
        script2 = self.ReadFromCSV("Script2Parsed")
        script2.pop(-1)
        newList = []
        if(POS == "Adjective"):
            for scriptItem in script1:
                if scriptItem[2] == "い-Adjective" or scriptItem[2] == "な-Adjective":
                    newList.append(scriptItem + [0])
            for scriptItem in script2:
                if scriptItem[2] == "い-Adjective" or scriptItem[2] == "な-Adjective":
                    newWord = True
                    for item in newList:
                        if item[0] == scriptItem[0]:
                            item[4] = scriptItem[3]
                            newWord = False
                            break
                    if (newWord):
                        newList.append([scriptItem[0], scriptItem[1], scriptItem[2], 0, scriptItem[3]])
        else:
            for scriptItem in script1:
                if scriptItem[2] == POS:
                    newList.append(scriptItem + [0])

            for scriptItem in script2:
                if scriptItem[2] == POS:
                    newWord = True
                    for item in newList:
                        if item[0] == scriptItem[0]:
                            item[4] = scriptItem[3]
                            newWord = False
                            break
                    if (newWord):
                        newList.append([scriptItem[0], scriptItem[1], scriptItem[2], 0, scriptItem[3]])
        return newList
    
    
    def FindOccurrences(self, text):
        data = []
        for word in text:
            location = 0
            wordAdd = True
            firstTerm = str(word[0])
            for term in data:
                secondTerm = str(term[0])
                if(firstTerm == secondTerm):
                    data[location][3] += 1
                    wordAdd = False
                    break
                else:
                    location += 1
            if wordAdd:
                data.append(word+[1])
        return data
    
    
    def GetLemmaAndPOS(self, data):
        terms = []
        for item in data:
            incremented = False
            for term in terms:
                if(term[0] == item[1]):
                    term[2] += int(item[3])
                    incremented = True
                    break
            if(incremented == False):
                terms.append([item[1], item[2], int(item[3])])
        return terms

    
    def GetPOS(self, data):
        POS = []
        for item in data:
            incremented = False
            for term in POS:
                if(term[0] == item[2]):
                    term[1] += int(item[3])
                    incremented = True
                    break
            if(incremented == False):
                POS.append([item[2], int(item[3])])
        return POS
    
    
    def HandleDataTracker(self, operation):
        if operation == "open":
            tracker = self.SetUpDataTracker()
            trackerHeader = tracker.pop(0)
        elif operation == "close":
            self.WriteToCSV(trackerHeader, tracker, "_OperationTracker")
    
    
    def InitializeTotalsSet(self, initialTotals):
        totals = [
            [initialTotals[0], initialTotals[1], initialTotals[2]],
            ["WORDS", 0, 0],
            ["LEMMA", 0, 0],
            ["POS", 0, 0]]
        return totals
    
    
    def PromptComplete(self):
        print("OPERATION COMPELTE.\n")
    
    
    def PromptContinue(self):
        input("Press 'ENTER' to continue.")
    
    
    def PromptInvalid(self):
        print("INVALID INPUT\n")
    
    
    def PromptReturn(self):
        print("Returning to MAIN options.\n")
    
    
    def ReadFromCSV(self, fileName):
        data = []
        with open(CSVdir + fileName + ".CSV", newline = '') as CSV:
            data += csv.reader(CSV, delimiter = ',', lineterminator = '\r', quotechar = '|')
        data.pop(0)
        return data

    
    def RemoveSymbols(self, data):
        newList = []
        for entry in data:
            if(entry[2] != "Auxiliary Symbol"):
                newList.append(entry)
        return newList
    
    
    def ResetApp(self, trackerArray):
        self.ClearScreen()
        for item in trackerArray:
            item[1] = "NO"
        # Delete Core data files
        if os.path.exists(CSVdir + "_OperationTracker.csv"):
            os.remove(CSVdir + "_OperationTracker.csv")
        if os.path.exists(CSVdir + "_Totals.csv"):
            os.remove(CSVdir + "_Totals.csv")
        if os.path.exists(CSVdir + "Script1Parsed.csv"):
            os.remove(CSVdir + "Script1Parsed.csv")
        if os.path.exists(CSVdir + "Script2Parsed.csv"):
            os.remove(CSVdir + "Script2Parsed.csv")
        # Delete Script 1 data files
        if os.path.exists(CSVdir + "CountCompareScript1Lemma.csv"):
            os.remove(CSVdir + "CountCompareScript1Lemma.csv")
        if os.path.exists(CSVdir + "CountCompareScript1POS.csv"):
            os.remove(CSVdir + "CountCompareScript1POS.csv")
        if os.path.exists(CSVdir + "CountCompareScript1Words.csv"):
            os.remove(CSVdir + "CountCompareScript1Words.csv")
        if os.path.exists(CSVdir + "PercentCompareScript1Lemma.csv"):
            os.remove(CSVdir + "PercentCompareScript1Lemma.csv")
        if os.path.exists(CSVdir + "PercentCompareScript1POS.csv"):
            os.remove(CSVdir + "PercentCompareScript1POS.csv")
        if os.path.exists(CSVdir + "PercentCompareScript1Words.csv"):
            os.remove(CSVdir + "PercentCompareScript1Words.csv")
        # Delete Script 2 data files
        if os.path.exists(CSVdir + "CountCompareScript2Lemma.csv"):
            os.remove(CSVdir + "CountCompareScript2Lemma.csv")
        if os.path.exists(CSVdir + "CountCompareScript2POS.csv"):
            os.remove(CSVdir + "CountCompareScript2POS.csv")
        if os.path.exists(CSVdir + "CountCompareScript2Words.csv"):
            os.remove(CSVdir + "CountCompareScript2Words.csv")
        if os.path.exists(CSVdir + "PercentCompareScript2Lemma.csv"):
            os.remove(CSVdir + "PercentCompareScript2Lemma.csv")
        if os.path.exists(CSVdir + "PercentCompareScript2POS.csv"):
            os.remove(CSVdir + "PercentCompareScript2POS.csv")
        if os.path.exists(CSVdir + "PercentCompareScript2Words.csv"):
            os.remove(CSVdir + "PercentCompareScript2Words.csv")
        print("APPLICATION RESET.\n")
    
    
    def RunModule(self, module):
        self.ClearScreen()
        os.system("Python3 Source/" + module + ".py")
    
    
    def SetUpDataTracker(self):
        dataTracker = []
        if os.path.exists(CSVdir + "_OperationTracker.csv"):
            dataTracker = self.ReadFromCSV("_OperationTracker")
        else:
            dataTracker = [["Parsed Datasets Built", "NO"],
                           ["Word Comparison Dataset Built", "NO"],
                           ["Lemma Comparison Dataset Built", "NO"],
                           ["POS Datasets Built", "NO"],
                           ["NarrowNum", 0]]
        dataTracker.insert(0, ["Operation", "Completed?"])
        return dataTracker
    
    
    def TranslatePOS(self, POS):
        POStypes = ["補助記号", "助詞", "助動詞", "動詞", "副詞", "接頭辞", "代名詞", "接続詞", "名詞", "形容詞", "接尾辞", "連体詞", "感動詞", "記号", "形状詞"]
        POStranslations = ["Auxiliary Symbol", "Particle", "Auxiliary Verb", "Verb", "Adverb", "Prefix", "Pronoun", "Conjunction", "Noun", "い-Adjective", "Postfix", "Adnominal", "Interjection", "Coda", "な-Adjective"]
        for index in range(len(POStypes)):
            if (POS == POStypes[index]):
                POS = POStranslations[index]
        return POS


    def WriteToCSV(self, header, inData, fileName):
        with open(CSVdir + fileName + ".csv", "w") as CSV:
            Output = csv.writer(CSV)
            Output.writerow(header)
            Output.writerows(inData)

    customOutputFileNum = 0

Methods = Methods()






class MenuMethods:        
    def HandleModule(self, module, progressBar, button):
        Methods.ClearScreen()
        print(module)
        print(type(module))
        Methods.RunModule(module)
        progressBar.stop()
        button["state"] = "normal"
        
    
    def ParseText(self, root, tracker, STR):
        parseWindow = tk.Toplevel(root)
        parseWindow.minsize(320, 180)
        parseWindow.title(STR.PARSE_TITLE)
        parseLabel = tk.Label(master = parseWindow, text = STR.PARSE_LABEL, font = ("Ariel", 20))
        parseLabel.pack(padx = 15, pady = 5, fill = tk.BOTH, expand = False)
        
        parseBar = ttk.Progressbar(master = parseWindow, mode = "indeterminate")
        parseBar.pack(fill = tk.BOTH, padx = 15, pady = 10, expand = False)
        
        continueButton = tk.Button(master = parseWindow, text = STR.RETURN, bg = "gray", fg = "black", state = "disabled", command = parseWindow.destroy)
        continueButton.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        tracker[0][1] = "YES"
        parseBar.start()
        thread1 = Thread(target = self.HandleModule, args = ("DataParser", parseBar, continueButton))
        
        parseWindow.after_idle(thread1.start())
        parseWindow.mainloop()
        
        
    def GoToComparisonMenu(self, root, tracker, STR):
        compWindow = tk.Toplevel(root)
        compWindow.minsize(250, 250)
        compWindow.title(STR.COMP_TITLE)
        
        compLabel = tk.Label(master = compWindow, text = STR.COMP_LABEL, font = ("Ariel", 20))
        wordComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        lemmaComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_1, bg = "gray", fg = "black", state = "disabled")
        posComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_2, bg = "gray", fg = "black", state = "disabled")
        goBack = tk.Button(master = compWindow, text = STR.RETURN, bg = "gray", fg = "black", command = compWindow.destroy)
        
        if(tracker[0][1] == "YES"):
            wordComp["state"] = "normal"
            lemmaComp["state"] = "normal"
            posComp["state"] = "normal"
        else:
            Methods.ClearScreen()
            print("Must build parsed datasets before building comparison datasets.")
            compLabel["text"] = STR.ERROR_PARSED
            
        compLabel.pack(padx = 15, pady = 5, fill = tk.BOTH, expand = False)
        wordComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        lemmaComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        posComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        goBack.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        compWindow.mainloop()
    
    def GoToCustomMenu(self, root, tracker, STR):
        print(" 1: Extract ADJECTIVES (ALL) for dataset.\n",
          "2: Extract ADJECTIVES (い) for dataset.\n",
          "3: Extract ADJECTIVES (な) for dataset.\n",
          "4: Extract ADNOMINALS for dataset.\n",
          "5: Extract ADVERBS for dataset.\n",
          "6: Extract AUXILIARY VERBS for dataset.\n",
          "7: Extract CODA for dataset.\n",
          "8: Extract CONJUNCTIONS for dataset.\n",
          "9: Extract INTERJECTIONS for dataset.\n",
          "10: Extract NOUNS for dataset.\n",
          "11: Extract PARTICLES for dataset.\n",
          "12: Extract PREFIXES for dataset.\n",
          "13: Extract PRONOUNS for dataset.\n",
          "14: Extract SUFFIXES for dataset.\n",
          "15: Extract VERBS for dataset.\n",
          "\n")
        
        compWindow = tk.Toplevel(root)
        compWindow.minsize(250, 250)
        compWindow.title(STR.CUST_TITLE)
        
        compLabel = tk.Label(master = compWindow, text = STR.CUST_LABEL, font = ("Ariel", 20))
        adjCompAll = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        adjCompI = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        adjCompNa = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        adnomComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        advComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        auxVerbComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        codaComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        conComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        interComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        nounComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        partComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        preComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        postComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        proComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        verbComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled")
        goBack = tk.Button(master = compWindow, text = STR.BUILD, bg = "gray", fg = "black", command = compWindow.destroy)
        
        if(tracker[0][1] == "YES"):
            adjCompAll["state"] = "normal"
            adjCompI["state"] = "normal"
            adjCompNa["state"] = "normal"
            adnomComp["state"] = "normal"
            advComp["state"] = "normal"
            auxVerbComp["state"] = "normal"
            codaComp["state"] = "normal"
            conComp["state"] = "normal"
            interComp["state"] = "normal"
            nounComp["state"] = "normal"
            partComp["state"] = "normal"
            preComp["state"] = "normal"
            postComp["state"] = "normal"
            proComp["state"] = "normal"
            verbComp["state"] = "normal"
        else:
            Methods.ClearScreen()
            print("Must build parsed datasets before building comparison datasets.")
            compLabel["text"] = STR.ERROR_PARSED
            
        compLabel.pack(padx = 15, pady = 5, fill = tk.BOTH, expand = False)
        adjCompAll.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        adjCompI.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        adjCompNa.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        adnomComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        advComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        auxVerbComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        codaComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        conComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        interComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        nounComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        partComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        preComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        postComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        proComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        verbComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        goBack.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        compWindow.mainloop()
        
        

MenuMethods = MenuMethods()