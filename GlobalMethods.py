import csv

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


Methods = GlobalMethods()