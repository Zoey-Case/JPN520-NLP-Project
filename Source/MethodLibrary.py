import csv
import os
import tkinter as tk
from tkinter import ttk
from threading import Thread
from functools import partial

class Methods:
    # BubbleSort algorithm (GREATEST to LEAST).
    def BubbleSort(self, data, valueIndex): 
        length = len(data)
        for outerIndex in range(length - 1):
            swapped = False
            for innerIndex in range(0, length - outerIndex - 1):
                if (float(data[innerIndex + 1][valueIndex]) > float(data[innerIndex][valueIndex])):
                    swapped = True
                    data[innerIndex + 1], data[innerIndex] = data[innerIndex], data[innerIndex + 1]
            if not swapped:
                return data
    
    
    def ConvertToPercentages(self, text, total, valueIndex):
        for word in text:
            word[valueIndex] = (float(word[valueIndex]) / float(total)) * 100
    
    
    def Copy(self, dataToCopy):
        copy = []
        for item in dataToCopy:
            copy.append(item[:])
        return copy

    
    def CountEntries(self, data, valueIndex):
        total = 0
        for word in data:
            total += int(word[valueIndex])
        return total
    
    
    def DeleteCSVfile(self, fileName, CSVdir):
        if os.path.exists(CSVdir + fileName + ".csv"):
            os.remove(CSVdir + fileName + ".csv")
    
    
    def Extract(self, POS, type):
        script1 = self.ReadFromCSV("Script1Parsed", self.GetDirectoryMainCSV())
        script2 = self.ReadFromCSV("Script2Parsed", self.GetDirectoryMainCSV())
        script2.pop(-1)
        
        newList = []
        
        if(type == "LEMMA"):
            dataset1 = Methods.GetLemmaAndPOS(script1)
            dataset2 = Methods.GetLemmaAndPOS(script2)
            for scriptItem in dataset1:
                if scriptItem[1] == POS:
                    newList.append(scriptItem + [0])

            for scriptItem in dataset2:
                if scriptItem[1] == POS:
                    newWord = True
                    for item in newList:
                        if item[0] == scriptItem[0]:
                            item[3] = scriptItem[2]
                            newWord = False
                            break
                    if (newWord):
                        newList.append([scriptItem[0], scriptItem[1], 0, scriptItem[2]])
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
    
    
    def GetDirectoryDefaultCSV(self):
        return self.defaultCSVdir
    
    def GetDirectoryCustomCSV(self):
        return self.customCSVdir
    
    def GetDirectoryMainCSV(self):
        return self.mainCSVdir
    
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


    def GetNumScripts(self):
        return self.numScripts
    
    
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

    
    def GetScriptName(self, index):
        return self.scriptNames[index]
    
    
    def HandleDataTracker(self, operation):
        if operation == "open":
            tracker = self.SetUpDataTracker()
            trackerHeader = tracker.pop(0)
        elif operation == "close":
            self.WriteToCSV(trackerHeader, tracker, "_OperationTracker", self.mainCSVdir)
    
    
    def InitializeTotalsSet(self, initialTotals):
        totals = [
            [initialTotals[0], initialTotals[1], initialTotals[2]],
            ["WORDS", 0, 0],
            ["LEMMA", 0, 0],
            ["POS", 0, 0]]
        return totals
    
    
    def ReadFromCSV(self, fileName, CSVdir):
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
    
    
    def RunModule(self, module):
        os.system("Python3 Source/" + module + ".py")
    
    
    def SetUpDataTracker(self):
        dataTracker = []
        if os.path.exists(self.mainCSVdir + "_OperationTracker.csv"):
            dataTracker = self.ReadFromCSV("_OperationTracker", self.GetDirectoryMainCSV())
        else:
            dataTracker = [["Parsed Datasets Built", "NO"],
                           ["Word Comparison Dataset Built", "NO"],
                           ["Lemma Comparison Dataset Built", "NO"],
                           ["POS Datasets Built", "NO"],
                           ["Custom Datasets Built", 0]]
        dataTracker.insert(0, ["Operation", "Completed?"])
        return dataTracker
    
    
    def TranslatePOS(self, POS):
        POStypes = ["補助記号", "助詞", "助動詞", "動詞", "副詞", "接頭辞", "代名詞", "接続詞", "名詞", "形容詞", "接尾辞", "連体詞", "感動詞", "記号", "形状詞"]
        POStranslations = ["Auxiliary Symbol", "Particle", "Auxiliary Verb", "Verb", "Adverb", "Prefix", "Pronoun", "Conjunction", "Noun", "い-Adjective", "Postfix", "Adnominal", "Interjection", "Coda", "な-Adjective"]
        for index in range(len(POStypes)):
            if (POS == POStypes[index]):
                POS = POStranslations[index]
        return POS


    def WriteToCSV(self, header, inData, fileName, CSVdir):
        if not os.path.exists(CSVdir):
            os.makedirs(CSVdir)
        with open(CSVdir + fileName + ".csv", "w") as CSV:
            Output = csv.writer(CSV)
            Output.writerow(header)
            Output.writerows(inData)

    customCSVdir = "Data/Custom Comparisons/"
    defaultCSVdir = "Data/Default Comparisons/"
    mainCSVdir = "Data/"
    
    numScripts = 2
    scriptNames = ["Script1", "Script2"]

Methods = Methods()


class MenuMethods:
    
    def __init__(self):
        self.tracker = Methods.SetUpDataTracker()
        self.trackerHeader = self.tracker.pop(0)
    
        
    ################### 
    # Public Methods #
    ###################
    
    
    def CloseApp(self, root):
        Methods.WriteToCSV(self.trackerHeader, self.tracker, "_OperationTracker", Methods.GetDirectoryMainCSV())
        root.destroy()
    
    
    def CustomComparisonMenu(self, root, STR):
        compWindow = tk.Toplevel(root)
        compWindow.minsize(480,810)
        compWindow.title(STR.CUST_TITLE)
        
        width = 480
        height = 810
        screenWidth = compWindow.winfo_screenwidth()
        screenHeight = compWindow.winfo_screenheight()
        xLoc = (screenWidth/2) - (width/2)
        yLoc = (screenHeight/2) - (height/2)
        compWindow.geometry('%dx%d+%d+%d' % (width, height, xLoc, yLoc))
        
        compLabel = tk.Label(master = compWindow, text = STR.CUST_LABEL, font = ("Ariel", 20))
        adjCompAll = tk.Button(master = compWindow, text = STR.CUST_OPTION_0, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "All Adjectives"))
        adjCompI = tk.Button(master = compWindow, text = STR.CUST_OPTION_1, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "い-Adjective"))
        adjCompNa = tk.Button(master = compWindow, text = STR.CUST_OPTION_2, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "な-Adjective"))
        adnomComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_3, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Adnominal"))
        advComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_4, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Adverb"))
        auxVerbComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_5, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Auxiliary Verb"))
        codaComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_6, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Coda"))
        conComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_7, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Conjunction"))
        interComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_8, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Interjection"))
        nounComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_9, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Noun"))
        partComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_10, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Particle"))
        preComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_11, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Postfix"))
        postComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_12, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Prefix"))
        proComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_13, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Pronoun"))
        verbComp = tk.Button(master = compWindow, text = STR.CUST_OPTION_14, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__AddCustomOption, "Verb"))
        lemmaBuild = tk.Button(master = compWindow, text = STR.LEMMA_BUILD, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__RunCustomProcess, root, "LEMMA", STR))
        wordBuild = tk.Button(master = compWindow, text = STR.WORD_BUILD, bg = "gray", fg = "black", state = "disabled",
                                command = partial(self.__RunCustomProcess, root, "WORD", STR))
        goBack = tk.Button(master = compWindow, text = STR.RETURN, bg = "gray", fg = "black", command = compWindow.destroy)
        
        if(self.tracker[0][1] == "YES"):
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
            lemmaBuild["state"] = "normal"
            wordBuild["state"] = "normal"
            
            self.customOptions = self.__SetupCustomOptionTracker()
        else:
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
        lemmaBuild.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        wordBuild.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        goBack.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        compWindow.mainloop()
    
    def DefaultComparisonMenu(self, root, STR):
        compWindow = tk.Toplevel(root)
        compWindow.minsize(480,270)
        compWindow.title(STR.COMP_TITLE)
        
        width = 480
        height = 270
        screenWidth = compWindow.winfo_screenwidth()
        screenHeight = compWindow.winfo_screenheight()
        xLoc = (screenWidth/2) - (width/2)
        yLoc = (screenHeight/2) - (height/2)
        compWindow.geometry('%dx%d+%d+%d' % (width, height, xLoc, yLoc))
        
        compLabel = tk.Label(master = compWindow, text = STR.COMP_LABEL, font = ("Ariel", 20))
        wordComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_0, bg = "gray", fg = "black", state = "disabled",
                             command = partial(self.__ModuleProcessWindow, "CompareWords", root, self.tracker[1], STR.WORD_TITLE, STR.WORD_LABEL, STR.RETURN))
        lemmaComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_1, bg = "gray", fg = "black", state = "disabled",
                             command = lambda: self.__ModuleProcessWindow("CompareLemma", root, self.tracker[2], STR.LEMMA_TITLE, STR.LEMMA_LABEL, STR.RETURN))
        posComp = tk.Button(master = compWindow, text = STR.COMP_OPTION_2, bg = "gray", fg = "black", state = "disabled",
                             command = lambda: self.__ModuleProcessWindow("ComparePOS", root, self.tracker[3], STR.POS_TITLE, STR.POS_LABEL, STR.RETURN))
        goBack = tk.Button(master = compWindow, text = STR.RETURN, bg = "gray", fg = "black", command = compWindow.destroy)
        
        if(self.tracker[0][1] == "YES"):
            wordComp["state"] = "normal"
            lemmaComp["state"] = "normal"
            posComp["state"] = "normal"
        else:
            compLabel["text"] = STR.ERROR_PARSED
            
        compLabel.pack(padx = 15, pady = 5, fill = tk.BOTH, expand = False)
        wordComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        lemmaComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        posComp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        goBack.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        compWindow.mainloop()
    
    def ParseText(self, root, STR):
        self.__ModuleProcessWindow("DataParser", root, self.tracker[0], STR.PARSE_TITLE, STR.PARSE_LABEL, STR.RETURN)
    
    def ResetApp(self):
        # Delete CORE data files
        Methods.DeleteCSVfile("_OperationTracker", Methods.GetDirectoryMainCSV())
        Methods.DeleteCSVfile("Totals", Methods.GetDirectoryMainCSV())
        Methods.DeleteCSVfile("Script1Parsed", Methods.GetDirectoryMainCSV())
        Methods.DeleteCSVfile("Script2Parsed", Methods.GetDirectoryMainCSV())
        
        # Delete SCRIPT data files
        for index in range(Methods.GetNumScripts() + 1):
            Methods.DeleteCSVfile("Script" + str(index) + "LemmaCountCompare", Methods.GetDirectoryDefaultCSV())
            Methods.DeleteCSVfile("Script" + str(index) + "POSCountCompare", Methods.GetDirectoryDefaultCSV())
            Methods.DeleteCSVfile("Script" + str(index) + "WordsCountCompare", Methods.GetDirectoryDefaultCSV())
            Methods.DeleteCSVfile("Script" + str(index) + "LemmaPercentCompare", Methods.GetDirectoryDefaultCSV())
            Methods.DeleteCSVfile("Script" + str(index) + "POSPercentCompare", Methods.GetDirectoryDefaultCSV())
            Methods.DeleteCSVfile("Script" + str(index) + "WordsPercentCompare", Methods.GetDirectoryDefaultCSV())
            
            for index in range(int(self.tracker[-1][1]) + 1):
                Methods.DeleteCSVfile("Script" + str(index) + "CustomCountCompare-" + str(index), Methods.GetDirectoryCustomCSV())
                Methods.DeleteCSVfile("Script" + str(index) + "CustomPercentCompare-" + str(index), Methods.GetDirectoryCustomCSV())
        
        for index in range(len(self.tracker) - 1):
            self.tracker[index][1] = "NO"
        self.tracker[-1][1] = 0
    
    ###################
    # Private Methods #
    ###################
    
    
    def __AddCustomOption(self, option):
        if(option == "All Adjectives"):
            self.customOptions[0][1] = 1
            self.customOptions[1][1] = 1
        else:
            for entry in self.customOptions:
                if (entry[0] == option):
                    entry[1] = 1
    
    
    def __HandleModule(self, module, progressBar, button, processLabel):
        Methods.RunModule(module)
        progressBar.stop()
        button["state"] = "normal"
        processLabel["text"] = "PROCESS COMPLETE"
    
    
    def __ModuleProcessWindow(self, module, root, trackerData, STRtitle, STRlabel, STRreturn):
        processWindow = tk.Toplevel(root)
        processWindow.minsize(480,270)
        processWindow.title(STRtitle)
        
        width = 480
        height = 270
        screenWidth = processWindow.winfo_screenwidth()
        screenHeight = processWindow.winfo_screenheight()
        xLoc = (screenWidth/2) - (width/2)
        yLoc = (screenHeight/2) - (height/2)
        processWindow.geometry('%dx%d+%d+%d' % (width, height, xLoc, yLoc))
        
        processLabel = tk.Label(master = processWindow, text = STRlabel, font = ("Ariel", 20))
        processLabel.pack(padx = 15, pady = 5, fill = tk.BOTH, expand = False)
        
        progressBar = ttk.Progressbar(master = processWindow, mode = "indeterminate")
        progressBar.pack(fill = tk.BOTH, padx = 15, pady = 10, expand = False)
        
        continueButton = tk.Button(master = processWindow, text = STRreturn, bg = "gray", fg = "black", state = "disabled", command = processWindow.destroy)
        continueButton.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
        
        if(module == "CompareCustom"):
            progressBar.start()
            thread1 = Thread(target = self.__HandleModule, args = (module, progressBar, continueButton, processLabel))
            processWindow.after_idle(thread1.start)
        else:
            if(trackerData[1] == "YES"):
                processLabel["text"] = "PROCESS ALREADY COMPLETED"
                continueButton["state"] = "normal"
            else:
                progressBar.start()
                
                for index in range(len(self.tracker)):
                    if(self.tracker[index][0] == trackerData[0]):
                        self.tracker[index][1] = "YES"
                        break
                
                thread1 = Thread(target = self.__HandleModule, args = (module, progressBar, continueButton, processLabel))
                processWindow.after_idle(thread1.start)
        
        processWindow.mainloop()
        
    
    def __RunCustomProcess(self, root, type, STR):
        breakOut = True
        
        for entry in self.customOptions:
            if(entry[-1] == 1):
                breakOut = False
                break
        
        if(breakOut):
            return
                
        self.customOptions[-1][1] = int(self.customOptions[-1][1]) + 1
        self.tracker[-1][1] = self.customOptions[-1][1]
        self.customOptions[-2][1] = type
        
        Methods.WriteToCSV(["OPERATIONS"], self.customOptions, "_CustomOptions", Methods.GetDirectoryMainCSV())
        
        for index in range(13):
            if(self.customOptions[index][1] == 1):
                self.customOptions[index][1] = 0
        
        self.__ModuleProcessWindow("CompareCustom", root, [], STR.LEMMA_TITLE, STR.LEMMA_LABEL, STR.RETURN)
    
    def __SetupCustomOptionTracker(self):
        return  [["い-Adjective", 0],
                 ["な-Adjective", 0],
                 ["Adnominal", 0],
                 ["Adverb", 0],
                 ["Auxiliary Verb", 0],
                 ["Coda", 0],
                 ["Conjunction", 0],
                 ["Interjection", 0],
                 ["Noun", 0],
                 ["Particle", 0],
                 ["Prefix", 0],
                 ["Pronoun", 0],
                 ["Postfix", 0],
                 ["Verb", 0],
                 ["Type", ""],
                 ["FileNum", self.tracker[4][1]]]
    
    
    #####################
    # PRIVATE VARIABLES #
    #####################
    
    
    customOptions = []
    tracker = []
    trackerHeader = []


MenuMethods = MenuMethods()