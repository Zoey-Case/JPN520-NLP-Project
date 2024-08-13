from Source.MethodLibrary import Methods

tracker = Methods.SetUpDataTracker()
trackerHeader = tracker.pop(0)

while(True):
    Methods.ClearScreen()
    
    print(" 1: Build parsed datasets.\n",
          "2: Build comparison datasets.\n",
          "3: Extract narrowed datasets.\n",
          "4: Reset Application.\n",
          "\n")
    
    print("Enter the number corresponding to your choice.")
    userInput = str(input("Enter EXIT or QUIT to exit the application.\n\n"))
    userInput.lower()
    
    if(userInput == "1" or userInput == "one"):
        tracker[0][1] = "YES"
        Methods.RunModule("DataParser")
    
    elif(userInput == "2" or userInput == "two"):
        if(tracker[0][1] == "NO"):
            Methods.ClearScreen()
            print("Must build parsed datasets before building comparison datasets.")
        else:
            while(True):
                Methods.ClearScreen()
                print(" 1: Build Word Comparison Dataset\n",
                    "2: Build Lemma Comparison Dataset\n",
                    "3: Build POS Comparison Dataset\n",
                    "4: Return to previous options.")
                
                userInput = str(input("Enter the number corresponding to your choice.\n"))
                
                if(userInput == "1" or userInput == "one"):
                    tracker[1][1] = "YES"
                    Methods.ClearScreen()
                    Methods.RunModule("CompareWords")
                elif(userInput == "2" or userInput == "two"):
                    tracker[2][1] = "YES"
                    Methods.ClearScreen()
                    Methods.RunModule("CompareLemma")
                elif(userInput == "3" or userInput == "three"):
                    tracker[3][1] = "YES"
                    Methods.ClearScreen()
                    Methods.RunModule("ComparePOS")
                elif(userInput == "4" or userInput == "four"):
                    Methods.ClearScreen()
                    Methods.PromptReturn()
                    break
                else:
                    Methods.ClearScreen()
                    Methods.PromptInvalid()
                    Methods.PromptContinue()
    
    elif(userInput == "3" or userInput == "three"):
        if tracker[1][1] == "YES":
            tracker[5][1] = int(tracker[5][1]) + 1
            Methods.RunModule("CompareNarrow")
        else:
            Methods.ClearScreen()
            print("Must build word comparison datasets before building comparison datasets.")
    
    elif(userInput == "4" or userInput == "four"):
        Methods.ResetApp(tracker)
        
    elif(userInput == "exit" or userInput == "quit"):
        Methods.ClearScreen()
        break
    
    else:
        Methods.ClearScreen()
        Methods.PromptInvalid()
    
    Methods.PromptContinue()

Methods.WriteToCSV(trackerHeader, tracker, "_OperationTracker")