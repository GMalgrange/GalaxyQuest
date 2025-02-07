from tkinter import *
from tkinter import filedialog

class BaseRenderer:
    
    def __init__(self):
        #Initialize the root widget
        self._root = Tk()
        self._canvas = []
        
    def addCanvas(self, iCanvas):
        #receive canvas from a contextual renderer and display it
        self._canvas.append(iCanvas)
        
    def getRoot(self):
        return self._root
        
    def renderBasic(self):
        for canva in self._canvas:
            canva.pack()
        self._root.mainloop()   
    
class SystemRenderer:
    
    def __init__(self, iSystem):
        print("Render system")
        
        #TODO