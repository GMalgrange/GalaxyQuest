from maps.celestialBody import CelestialBody
from enum import Enum

class PlaneteType(Enum):
	ROCKY_BARREN=1
	ROCKY_FROZEN=2
	ROCKY_MOLTEN=3
	ROCKY_INHABITABLE =4
	GAS_GIANT = 5
	ICE_DWARF = 6

class Planete(CelestialBody):
	_name="Unknown"
	_habitabilityFactor=100
	_population = 0
	_type = PlaneteType.ROCKY_BARREN
	def __init__(self, iName):
		self._name = iName
		#print("Create new Planete: "+self._name)
		
	def getPlaneteType(self):
		return self._type
		
	def getPlanetHabilityFactor(self):
		return self._habitabilityFactor
		
	def getPlanetPopulation(self):
		return self._population

