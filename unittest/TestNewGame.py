import unittest
import pickle
import random
#import NewGame

class Planet:
    _name = "Unknown"
    _ressource = 0
    
    def __init__(self, iName):
        self._name = iName
    
class System:
    _planetDict= {}
    _name = "Unkown"
    
    def __init__(self, iName):
        self._name = iName
    
    
nameList = ["Uranus", "Saturn", "Jupiter", "Mars"]
planetary = {}

aSystem = System("Sol")
iterateur = 0
for i in range(0,2):
    for j in range(0,2):
        aPlanet = Planet(nameList[iterateur])
        aPlanet._ressource = random.randint(0,100)
        planetary[(i,j)] = aPlanet
        iterateur+=1
    
#planetary = {(0,0):"Uranus",(0,1):"Saturn",(1,0):"Jupiter",(1,1):"Mars"}
print(planetary)
print (planetary[(0,0)]._ressource)

#aSystem = System("Sol")
aSystem._planetDict = planetary

file = open("UTFile.txt", "wb")
pickle.dump(aSystem, file)
file.close()

loadFile = open("UTFile.txt", "rb")
loadedPlanet = pickle.load(loadFile)
loadFile.close()

print(loadedPlanet._planetDict)
print(loadedPlanet._planetDict[(0,0)]._ressource)

if __name__ == '__main__':
    unittest.main()