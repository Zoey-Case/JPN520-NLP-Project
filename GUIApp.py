from Source.MethodLibrary import Methods
from Source.MethodLibrary import MenuMethods
import Source.Strings as STR
from tkinter import *
from threading import Thread


def ParseText():
    print("PARSING")
    MenuMethods.ParseText(mainMenu, tracker, STR)

def ComparisonMenu():
    MenuMethods.GoToComparisonMenu(mainMenu, tracker, STR)

def CustomMenu():
    MenuMethods.GoToCustomMenu(mainMenu, tracker, STR)

def ResetApp():
    Methods.ResetApp(tracker)
    
def CloseApp():
    Methods.WriteToCSV(trackerHeader, tracker, "_OperationTracker")
    mainMenu.destroy()
    
tracker = Methods.SetUpDataTracker()
trackerHeader = tracker.pop(0)



mainMenu = Tk()
mainMenu.minsize(480, 270)
mainMenu.title(STR.MENU_TITLE)

menuLabel = Label(master = mainMenu, text = STR.MENU_LABEL, font = ("Ariel", 20))
buildParsed = Button(master = mainMenu, text = STR.MENU_OPTION_0, bg = "gray", fg = "black", command = ParseText)
buildCompare = Button(master = mainMenu, text = STR.MENU_OPTION_1, bg = "gray", fg = "black", command = ComparisonMenu)
buildCustom = Button(master = mainMenu, text = STR.MENU_OPTION_2, bg = "gray", fg = "black", command = CustomMenu)
resetApp = Button(master = mainMenu, text = STR.MENU_OPTION_3, bg = "gray", fg = "black", command = ResetApp)
exitApp = Button(master = mainMenu, text = STR.MENU_OPTION_4, bg = "gray", fg = "black", command = CloseApp)

menuLabel.pack(padx = 15, pady = 5, fill = BOTH, expand = True)
buildParsed.pack(fill = BOTH, padx = 15, pady = 5, expand = True)
buildCompare.pack(fill = BOTH, padx = 15, pady = 5, expand = True)
buildCustom.pack(fill = BOTH, padx = 15, pady = 5, expand = True)
resetApp.pack(fill = BOTH, padx = 15, pady = 5, expand = True)
exitApp.pack(fill = BOTH, padx = 15, pady = 5, expand = True)

mainMenu.mainloop()

Methods.ClearScreen()