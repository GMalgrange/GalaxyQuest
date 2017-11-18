#!/usr/bin/env python
from maps.StellarSystem import StellarSystem
from maps.hyperlane import Hyperlane

class Galaxy:
	_size = 20
	_dimension = "Unknown"
	aSystemList = []
	_hyperlaneList = []
	
	def __init__(self):
		self._dimension = (400, 400)
		print("New Galaxy created")
		
	def getListAsString(self):
		oList=""
		for i in range(0, len(self.aSystemList)):
			oList = oList+self.aSystemList[i]._name+":("+str(self.aSystemList[i]._systemPosition[0])+ ","+str(self.aSystemList[i]._systemPosition[1])+") ;" 
			
		return oList