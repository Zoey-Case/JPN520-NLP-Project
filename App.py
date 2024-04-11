from GlobalMethods import Methods
import time
import csv
import os

CSVdir = "DATA"

if os.path.exists("OperationTracker.csv"):
    newTracker = False
    tracker = Methods.ReadCSV("OperationTracker.csv")
else:
    newTracker = True
    tracker = [
                ["Parsed Datasets Built",0],
                ["Word Comparison Dataset Built",0],
                ["Lemma Comparison Dataset Built",0],
                ["POS Datasets Built",0]
                ["Word Counts Built", 0]
            ]

while(True):
    os.system('clear')
    
    if(not newTracker):
        for item in tracker:
            if(item[1] == 1):
                print(item[0])
    
    print(" 1: Build parsed datasets.\n",
          "2: Build comparison datasets.\n",
          "3: Build POS dataset.\n",
          "4: Build Total Word Counts.\n",
          "5: Reset Application.\n")
    
    print("Enter the number corresponding to your choice.\n")
    userInput = str(input("Enter \"exit\" or \"quit\" to exit the application.\n"))
    
    userInput.lower()
    
    if(userInput == "1" or userInput == "one"):
        tracker[0][1] = 1
        os.system('clear')
        os.system("Python3 BuildParsedDatasets.py")
    
    elif(userInput == "2" or userInput == "two"):
        if(tracker[0][1] == 0):
            os.system('clear')
            print("Must build parsed datasets before building comparison datasets.")
            input("Press 'ENTER' to continue.")
        else:
            while(True):
                os.system('clear')
                print(" 1: Build Word Comparison Dataset\n",
                    "2: Build Lemma Comparison Dataset\n",
                    "3: Return to previous options.")
                
                userInput = str(input("Enter the number corresponding to your choice.\n"))
                
                if(userInput == "1" or userInput == "one"):
                    tracker[1][1] = 1
                    os.system('clear')
                    os.system("Python3 BuildWordDatasets.py")
                elif(userInput == "2" or userInput == "two"):
                    tracker[2][1] = 1
                    os.system('clear')
                    os.system("Python3 BuildLemmaDatasets.py")
                elif(userInput == "3" or userInput == "three"):
                    os.system('clear')
                    print("Returning to previous menu.\n")
                    break
                
                print("\n")
                
    elif(userInput == "3" or userInput == "three"):
        if(tracker[2][1] == 0):
            print("Must build LEMMA comparison datasets before building POS datasets.")
            input("Press 'ENTER' to continue.")
        else:
            tracker[3][1] = 1
            os.system('clear')
            os.system("Python3 BuildPOSDatasets.py")
    
    elif(userInput == "4" or userInput == "four"):
        if(tracker[3][1] == 0):
            print("Must build POS comparison datasets before building POS datasets.")
            input("Press 'ENTER' to continue.")
        else:
            tracker[4][1] = 1
            os.system('clear')
            os.system("Python3 BuildTotalWordCounts.py")
    
    elif(userInput == "5" or userInput == "five"):
        for item in tracker:
            item[0] = 0
        
        if os.path.exists(CSVdir+"/Persona4Lemma.csv"):
            os.remove(CSVdir+"/Persona4Lemma.csv")
        if os.path.exists(CSVdir+"/Persona4LemmaComparison.csv"):
            os.remove(CSVdir+"/Persona4LemmaComparison.csv")
        if os.path.exists(CSVdir+"/Persona4POS.csv"):
            os.remove(CSVdir+"/Persona4POS.csv")
        if os.path.exists(CSVdir+"/Persona4POSComparison.csv"):
            os.remove(CSVdir+"/Persona4POSComparison.csv")
        if os.path.exists(CSVdir+"/Persona4Words.csv"):
            os.remove(CSVdir+"/Persona4Words.csv")
        if os.path.exists(CSVdir+"/Persona4WordsComparison.csv"):
            os.remove(CSVdir+"/Persona4WordsComparison.csv")
        if os.path.exists(CSVdir+"/Persona5Lemma.csv"):
            os.remove(CSVdir+"/Persona5Lemma.csv")
        if os.path.exists(CSVdir+"/Persona5LemmaComparison.csv"):
            os.remove(CSVdir+"/Persona5LemmaComparison.csv")
        if os.path.exists(CSVdir+"/Persona5POS.csv"):
            os.remove(CSVdir+"/Persona5POS.csv")
        if os.path.exists(CSVdir+"/Persona5POSComparison.csv"):
            os.remove(CSVdir+"/Persona5POSComparison.csv")
        if os.path.exists(CSVdir+"/Persona5Words.csv"):
            os.remove(CSVdir+"/Persona5Words.csv")
        if os.path.exists(CSVdir+"/Persona5WordsComparison.csv"):
            os.remove(CSVdir+"/Persona5WordsComparison.csv")
                
        print("All project files cleared.\n")
        
    elif(userInput == "exit" or userInput == "quit"):
        os.system('clear')
        break
    
    else:
        os.system('clear')
        input("INVALID INPUT\n",
              "Press 'ENTER' to continue.")
    
    input("Press 'ENTER' to continue.")

with open("OperationTracker.csv", "w") as CSV:
    trackerOutput = csv.writer(CSV)
    trackerOutput.writerow(["Operation","#"])
    trackerOutput.writerows(tracker)