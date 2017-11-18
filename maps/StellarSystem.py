import random
#from maps.hyperlane import Hyperlane

class StellarSystem:
	#class defining a system composed from one star
	#and any number of planets and asteroids.
	_systemPosition = (0,0)
	_systemOwner = "None"
	_sun = "Undefined"
	_planeteList = []
	_asteroidList = []
	_name = "Unknown"
	
	def __init__(self, iGSize):		
		#Define system position within the Galaxy bounds passed as argument
		self._systemPosition =(random.randint(0,iGSize[0]),random.randint(0,iGSize[1]))

	
	