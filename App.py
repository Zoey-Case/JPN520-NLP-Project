from Source.GlobalMethods import Methods
import csv
import os

tracker = Methods.SetUpDataTracker()
CSVdir = "DATA"

while(True):
    os.system("clear")
    
    print(" 1: Build parsed datasets.\n",
          "2: Build comparison datasets.\n",
          "3: Build POS dataset.\n",
          "4: Build Total Word Counts.\n",
          "5: Reset Application.\n",
          "\n")
    
    print("Enter the number corresponding to your choice.")
    userInput = str(input("Enter \"exit\" or \"quit\" to exit the application.\n\n"))
    userInput.lower()
    
    if(userInput == "1" or userInput == "one"):
        tracker[0][1] = "YES"
        os.system("clear")
        os.system("Python3 Source/BuildParsedDatasets.py")
    
    elif(userInput == "2" or userInput == "two"):
        if(tracker[0][1] == "NO"):
            os.system("clear")
            print("Must build parsed datasets before building comparison datasets.")
            input("Press 'ENTER' to continue.")
        else:
            while(True):
                os.system("clear")
                print(" 1: Build Word Comparison Dataset\n",
                    "2: Build Lemma Comparison Dataset\n",
                    "3: Return to previous options.")
                
                userInput = str(input("Enter the number corresponding to your choice.\n"))
                
                if(userInput == "1" or userInput == "one"):
                    tracker[1][1] = "YES"
                    os.system("clear")
                    os.system("Python3 Source/BuildWordDatasets.py")
                elif(userInput == "2" or userInput == "two"):
                    tracker[2][1] = "YES"
                    os.system("clear")
                    os.system("Python3 Source/BuildLemmaDatasets.py")
                elif(userInput == "3" or userInput == "three"):
                    os.system("clear")
                    print("Returning to previous menu.\n")
                    break
                
                print("\n")
                
    elif(userInput == "3" or userInput == "three"):
        if(tracker[0][1] == "NO"):
            os.system("clear")
            print("Must build parsed datasets before building comparison datasets.")
            input("Press 'ENTER' to continue.")
        else:
            tracker[3][1] = "YES"
            os.system("clear")
            os.system("Python3 Source/BuildPOSDatasets.py")
    
    elif(userInput == "4" or userInput == "four"):
        if(tracker[3][1] == "NO"):
            os.system("clear")
            print("Must build POS comparison datasets before building POS datasets.")
            input("Press 'ENTER' to continue.")
        else:
            tracker[4][1] = "YES"
            os.system("clear")
            os.system("Python3 Source/BuildTotalWordCounts.py")
    
    elif(userInput == "5" or userInput == "five"):
        Methods.ResetApp(tracker, CSVdir)
        
    elif(userInput == "exit" or userInput == "quit"):
        os.system("clear")
        break
    
    else:
        os.system("clear")
        input("INVALID INPUT\n",
              "Press 'ENTER' to continue.")
    
    input("Press 'ENTER' to continue.")

with open("Source/OperationTracker.csv", "w") as CSV:
    trackerOutput = csv.writer(CSV)
    trackerOutput.writerow(["Operation", "Completed"])
    trackerOutput.writerows(tracker)