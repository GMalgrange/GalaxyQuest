import pickle
from maps.galaxy import Galaxy
from tkinter import filedialog

def saveGame(iGalaxy):
    
    #aSaveName = input("Name of the file: ")
    fileName = filedialog.asksaveasfilename(defaultextension='.txt')
    
    try:
        #Pickle the Galaxy object (and it's many children) to a file with the name given in input
        #print(iGalaxy._systemList)
        saveFile = open(fileName, "wb")
        aPickeled = pickle.dumps(iGalaxy, pickle.HIGHEST_PROTOCOL)
        saveFile.write(aPickeled)
        saveFile.close()
        
    except IOError:
        print("This file name is invalid, try another one")
    
def loadGame(iParent):
    
    #aSaveName = input("Which save do you want to load? ")
    dialog = filedialog.askopenfilename(defaultextension='.txt',title="Please select a save file:", parent=iParent)
    loadFromDialog = open(dialog, "rb")
    #loadFile = open(aSaveName+".txt", "rb")
    oGalaxy = pickle.loads(loadFromDialog.read())
    #print(oGalaxy._systemList)
    loadFromDialog.close()
    return oGalaxy