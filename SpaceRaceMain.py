#Generic imports
#Local imports - controller
from NewGame import NewGame
#Local imports - renderer
from basicRender import GalaxyRenderer

print("Start Galaxy colonization program")
#Generate game 
aGame = NewGame()
aGame.generateNewGame()
print("Game can start")

#Call render
render = GalaxyRenderer(aGame._galaxy)
render.renderGalaxy()

