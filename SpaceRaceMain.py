#Generic imports
import pickle
#Local imports - controller
from NewGame import NewGame
from saveEngine import loadGame
#Local imports - renderer
from renderers.galaxyRenderer import GalaxyRenderer
from renderers.basicRender import BaseRenderer

from maps.galaxy import Galaxy

print("Start Galaxy colonization program")
start = input("Do you want to load a saved game? Y : N ")
if start == "Y":
    #print("Saved file Loaded")
    aGame = NewGame()
    renderBasic = BaseRenderer()
    aGalaxy = loadGame(renderBasic._root)
    aGame._galaxy = aGalaxy
        
    #Call render
    renderGalaxy = GalaxyRenderer(aGame._galaxy, renderBasic.getRoot())
    renderBasic.addCanvas(renderGalaxy.renderGalaxy())
    renderBasic.renderBasic()    

else:    
    print("New Game")
    #Generate game 
    aGame = NewGame()
    aGame.generateNewGame()
    print("Game can start")
    
    #Call render
    renderBasic = BaseRenderer()
    renderGalaxy = GalaxyRenderer(aGame._galaxy, renderBasic.getRoot())
    renderBasic.addCanvas(renderGalaxy.renderGalaxy())
    renderBasic.renderBasic()    

