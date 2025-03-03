from functools import partial
from Source.MethodLibrary import MenuMethods
import Source.Strings as strings
import tkinter as tk

mainMenu = tk.Tk()
mainMenu.minsize(480,270)
mainMenu.title(strings.MENU_TITLE)

width = 480
height = 270
screenWidth = mainMenu.winfo_screenwidth()
screenHeight = mainMenu.winfo_screenheight()
xLoc = (screenWidth/2) - (width/2)
yLoc = (screenHeight/2) - (height/2)
mainMenu.geometry('%dx%d+%d+%d' % (width, height, xLoc, yLoc))

menuLabel = tk.Label(master = mainMenu, text = strings.MENU_LABEL, font = ("Ariel", 20))
buildParsed = tk.Button(master = mainMenu, text = strings.MENU_OPTION_0, bg = "gray", fg = "black", command = partial(MenuMethods.ParseText, mainMenu, strings))
buildCompare = tk.Button(master = mainMenu, text = strings.MENU_OPTION_1, bg = "gray", fg = "black", command = partial(MenuMethods.DefaultComparisonMenu, mainMenu, strings))
buildCustom = tk.Button(master = mainMenu, text = strings.MENU_OPTION_2, bg = "gray", fg = "black", command = partial(MenuMethods.CustomComparisonMenu, mainMenu, strings))
resetApp = tk.Button(master = mainMenu, text = strings.MENU_OPTION_3, bg = "gray", fg = "black", command = partial(MenuMethods.ResetApp))
exitApp = tk.Button(master = mainMenu, text = strings.MENU_OPTION_4, bg = "gray", fg = "black", command = partial(MenuMethods.CloseApp, mainMenu))

menuLabel.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
buildParsed.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
buildCompare.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
buildCustom.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
resetApp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)
exitApp.pack(fill = tk.BOTH, padx = 15, pady = 5, expand = True)

mainMenu.mainloop()