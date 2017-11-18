from maps.celestialBody import CelestialBody
from enum import Enum

class StarEnum(Enum):
	BLACK_HOLE=1
	NEUTRON_STAR=2
	SUPERNOVA=3
	RED_GIANT=4
	YELLOW = 5
	BLUE_DWARF=6
	
class Star(CelestialBody):
	_name="Unknown"
	_class=StarEnum.YELLOW
	def __init__(self, name):
		print("New sun")
		self.ressource = "Gas"
		self._name = name
		

	