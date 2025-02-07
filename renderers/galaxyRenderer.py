from tkinter import *
from tkinter import filedialog
from tkinter import Button
from tkinter import PhotoImage
from maps.galaxy import Galaxy
from saveEngine import saveGame


def circle(canvas, x, y, r, coul ='white'):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=coul, fill='white')
    
class ClickableSystem(Button):
    
    def __init__(self, iParent, iSystem):
        self.loadImage = PhotoImage(file='starPic.gif')
        Button.__init__(self, iParent, image=self.loadImage, bd=0, relief='flat', command = lambda arg1=self: self.displaySystem())
        self.bd = 0
        self.height = 5
        self.width = 5
        self.bg = 'black'
        self.relief = FLAT
        self.activebackground = 'red'
        
        self._system = iSystem



        
    def displaySystem(self):
        print(self._system._name)
        

class GalaxyRenderer:
    
    def __init__(self, iGalaxy, iRoot):
        self._galaxy = iGalaxy
        self._root = iRoot

        #Add a Menu bar for Saving
        menuSave = Menu(self._root)
        self._root['menu'] = menuSave
        menuSave.add_command(label='Save', command= self.callSaveEngine)
        
        self._canvas = Canvas(self._root, width=iGalaxy._dimension[0], height=iGalaxy._dimension[1], background='black')
        
    def displayMarker(self, evt):
        marker = Label(self._root, background = 'red', text = "Galaxy", foreground="white")
        print("I clicked on the canvas")
        
    def callSaveEngine(self):
        saveGame(self._galaxy) 
        
    def renderGalaxy(self):
        
        #Render systems
        for system in self._galaxy._systemList.values():
            #circle(self._canvas, system._systemPosition[0], system._systemPosition[1], 5)
            temp = ClickableSystem(self._canvas, system)
            temp.place(x = system._systemPosition[0] - 5 , y=system._systemPosition[1] -5 )
            #self._root.addCanvas(renderedSystem._canvas)
        #Render hyperlanes
        aHyperList = self._galaxy._hyperlaneList
        for i in range(0, len(aHyperList)):
            self._canvas.create_line(aHyperList[i].getCoordinate(), fill='white')
        
        self._canvas.bind('<Button-1>', self.displayMarker)
        
        #self._canvas.pack()
        
        #self._root.mainloop()
        return self._canvas