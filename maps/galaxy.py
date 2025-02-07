#!/usr/bin/env python
from math import sqrt
from maps.StellarSystem import StellarSystem
from maps.hyperlane import Hyperlane

class Galaxy:
	_size = 25
	_squaredSize = 5
	_dimension = "Unknown"
	_systemList = {}
	_hyperlaneList = []
	
	def __init__(self):
		self._dimension = (400, 400)		
		self._sectorMatrix = self.defineSectors(self.getSquaredSize())
		print("New Galaxy created")
		
	def getListAsString(self):
		oList=""
		for i in range(0, len(self._systemList)):
			oList = oList+self._systemList[i]._name+":("+str(self._systemList[i]._systemPosition[0])+ ","+str(self._systemList[i]._systemPosition[1])+") ;" 
			
		return oList
	
	def defineSectors(self, squareSize):
		
		return [[0 for x in range(int(squareSize))] for y in range(int(squareSize))]
	
	def getSquaredSize(self):
		return self._squaredSize
