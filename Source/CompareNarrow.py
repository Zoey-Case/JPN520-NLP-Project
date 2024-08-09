from MethodLibrary import Methods

countOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 COUNT", "SCRIPT 2 COUNT"]
percentOutputHeader = ["WORD", "LEMMA", "POS", "SCRIPT 1 PERCENT", "SCRIPT 2 PERCENT"]
outData = []

while(True):
    Methods.ClearScreen()
    
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
    
    print("Enter the number corresponding to your choice.")
    userInput = str(input("Enter '0' to return to the previous menu, once you are done extracting POS.\n"))
    userInput.lower()
    
    if(userInput == "0" or userInput == "zero"):
        S1dataset = outData
        Methods.BubbleSortAlt(S1dataset)
        S1total = Methods.CountEntriesAlt(S1dataset)
        
        S2dataset = Methods.CopyArray(outData)
        Methods.BubbleSort(S2dataset)
        S2total = Methods.CountEntries(S2dataset)
        
        S1datasetByP = Methods.CopyArray(S1dataset)
        Methods.ConvertToPercentages(S1datasetByP, S1total)
        Methods.ConvertToPercentagesAlt(S1datasetByP, S2total)
        S2datasetByP = Methods.CopyArray(S2dataset)
        Methods.ConvertToPercentages(S2datasetByP, S1total)
        Methods.ConvertToPercentagesAlt(S2datasetByP, S2total)
        
        tracker = Methods.ReadFromCSV("_OperationTracker")
        fileNum = str(int(tracker[5][1]) + 1)
        Methods.WriteToCSV(countOutputHeader, S1dataset, "CountCompareScript1Custom-" + fileNum)
        Methods.WriteToCSV(countOutputHeader, S2dataset, "CountCompareScript2Custom-" + fileNum)
        Methods.WriteToCSV(countOutputHeader, S1datasetByP, "PercentCompareScript1Custom-" + fileNum)
        Methods.WriteToCSV(countOutputHeader, S2datasetByP, "PercentCompareScript2Custom-" + fileNum)
        break
    # Extract い-Adjectives and な-Adjectives.
    if(userInput == "1" or userInput == "one"):
        for item in outData:
            if item[2] == "い-Adjective" or item[2] == "な-Adjective":
                outData.remove(item)
        outData = Methods.Extract("Adjective")
    # Extract い-Adjectives
    elif(userInput == "2" or userInput == "two"):
        for item in outData:
            if item[2] == "い-Adjective":
                outData.remove(item)
        outData = Methods.Extract("い-Adjective")
    # Extract な-Adjectives
    elif(userInput == "3" or userInput == "three"):
        for item in outData:
            if item[2] == "な-Adjective":
                outData.remove(item)
        outData = Methods.Extract("な-Adjective")
    # Extract Adnominals
    elif(userInput == "4" or userInput == "four"):
        for item in outData:
            if item[2] == "Adnominal":
                outData.remove(item)
        outData = Methods.Extract("Adnominal")
    # Extract Adverbs
    elif(userInput == "5" or userInput == "five"):
        for item in outData:
            if item[2] == "Adverb":
                outData.remove(item)
        outData = Methods.Extract("Adverb")
    # Extract Auxiliary Verbs
    elif(userInput == "6" or userInput == "six"):
        for item in outData:
            if item[2] == "Auxiliary Verb":
                outData.remove(item)
        outData = Methods.Extract("Auxiliary Verb")
    # Extract Coda
    elif(userInput == "7" or userInput == "seven"):
        for item in outData:
            if item[2] == "Coda":
                outData.remove(item)
        outData = Methods.Extract("Coda")
    # Extract Conjunctions
    elif(userInput == "8" or userInput == "eight"):
        for item in outData:
            if item[2] == "Conjunction":
                outData.remove(item)
        outData = Methods.Extract("Conjunction")
    # Extract Interjections
    elif(userInput == "9" or userInput == "nine"):
        for item in outData:
            if item[2] == "Interjection":
                outData.remove(item)
        outData = Methods.Extract("Interjection")
    # Extract Nouns
    elif(userInput == "10" or userInput == "ten"):
        for item in outData:
            if item[2] == "Noun":
                outData.remove(item)
        outData = Methods.Extract("Noun")
    # Extract Particles
    elif(userInput == "11" or userInput == "eleven"):
        for item in outData:
            if item[2] == "Particle":
                outData.remove(item)
        outData = Methods.Extract("Particle")
    # Extract Prefixes
    elif(userInput == "12" or userInput == "twelve"):
        for item in outData:
            if item[2] == "Prefix":
                outData.remove(item)
        outData = Methods.Extract("Prefix")
    # Extract Pronouns
    elif(userInput == "13" or userInput == "thirteen"):
        for item in outData:
            if item[2] == "Pronoun":
                outData.remove(item)
        outData = Methods.Extract("Pronoun")
    # Extract Suffixes
    elif(userInput == "14" or userInput == "fourteen"):
        for item in outData:
            if item[2] == "Suffix":
                outData.remove(item)
        outData = Methods.Extract("Suffix")
    # Extract Verbs
    elif(userInput == "15" or userInput == "fifteen"):
        for item in outData:
            if item[2] == "Verb":
                outData.remove(item)
        outData = Methods.Extract("Verb")
    # Erroneous Input
    else:
        Methods.ClearScreen()
        Methods.PromptInvalid()
        Methods.PromptContinue()

Methods.PromptContinue()