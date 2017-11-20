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
	
	def __init__(self, iXBound, aYBound):		
		#Define system position within the Galaxy bounds passed as argument
		self._systemPosition =(random.randint(iXBound[0],iXBound[1]),random.randint(aYBound[0],aYBound[1]))
		print(self._systemPosition)

	
	