#Generic imports
from tkinter import *
#Local imports
from NewGame import NewGame
from maps.galaxy import Galaxy
from maps.StellarSystem import StellarSystem
from maps.hyperlane import Hyperlane

#TO DO: move rendering code to a dedicated module

def cercle(x, y, r, coul ='black'):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=coul, fill='white')

print("Start Galaxy colonization program")
#Generate game 
aGame = NewGame()
aGame.generateNewGame()
print("Game can start")

#Call render
fenetre = Tk()
print(str(aGame._galaxy._dimension[1]))
canvas = Canvas(fenetre, width=aGame._galaxy._dimension[0], height=aGame._galaxy._dimension[1], background='black')
#Render systems
for i in range(0, len(aGame._galaxy.aSystemList)):
    cercle(aGame._galaxy.aSystemList[i]._systemPosition[0], aGame._galaxy.aSystemList[i]._systemPosition[1], 5)
#Render hyperlanes
aHyperList = aGame._galaxy._hyperlaneList
for i in range(0, len(aHyperList)):
    canvas.create_line(aHyperList[i].getCoordinate(), fill='white')

canvas.pack()

fenetre.mainloop()

