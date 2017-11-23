#!/usr/bin/env python
#Generic import
import random
import math
from operator import itemgetter
#Local import
from maps.galaxy import Galaxy
from maps.StellarSystem import StellarSystem
from maps.hyperlane import Hyperlane
from maps.planete import Planete
from maps.asteroid import Asteroid
from maps.star import Star


def parseNameList(iNameList):
	#print type(iNameList)
	oList = iNameList.read().split(",")
	return oList

####################################################################	
#Class NewGame

#For each system, generate it's celestial bodies
#Pick any system with an inhabitable Planet
#The pirate hideout should be placed at a safe distance 
#relative to the Player starting position
#Generate the CelestialBodies in a given StellarSystem	
####################################################################

class NewGame:
	
	
	
	def populateSystem(self, iSystem):
		#Link system with hyperlanes:
		#Check for redundancy.
		#Some systems may end up with more than 2 lane connexion; this is fine.
		#print("Generate hyperlane connexions")		
		iSystem._star = Star(iSystem._name)
		#Instanciate a random number of planets and asteroids
		randAsteroid= random.randint(0, 8)
		if randAsteroid > 6:
			randPlanet = 2
		else:
			randPlanet= random.randint(2, (8 - randAsteroid))
		print("Sun: "+ iSystem._name)
		#Generate planet list
		#name should be StarNameX
		#With X the number of the planet inside the system, in roman numeral
		_romanNumerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
		for i in range(0, randPlanet):
			#print("New Planet " + iSystem._name + " " + _romanNumerals[i])
			aPlanetName = iSystem._name + " " + _romanNumerals[i]
			aPlanet = Planete(aPlanetName)
			iSystem._planeteList.append(aPlanet)
		#Generate asteroid list
		for i in range(0, randAsteroid):
			aAsteroid = Asteroid()
			iSystem._asteroidList.append(aAsteroid)
			
	def generateHyperlane(self):
		
		#New matrix based generation
		#select 2 random systems within the immediate proximity of the current one 
		#(In the matrix representation of the galaxy)
		for i in range(0, self._galaxy._size):
			sytemI = self._galaxy.aSystemList[i]._matrixIndex
			print("System "+str(sytemI))
			aRandPos = [sytemI[0], sytemI[1]]
			targetSystemFound = 0
			targetSectorList = []
			#Put all valid proximity sector in a list
			for j in range(sytemI[0] - 1, sytemI[0]+2):
				for k in range(sytemI[1] - 1, sytemI[1]+2):
					if (j,k) != (sytemI[0], sytemI[1]) and self.isMatrixPositionValid((j,k)):
						targetSectorList.append((j,k))
			#Shuffle the list
			random.shuffle(targetSectorList)
			#Take the first 2 sectors in the list,
			#retrieve the corresponding Systems
			targetSystemPair = []
			for l in range(0, self._galaxy._size):
				if self._galaxy.aSystemList[l]._matrixIndex == targetSectorList[0]:
					targetSystemPair.append(self._galaxy.aSystemList[l])
				elif self._galaxy.aSystemList[l]._matrixIndex == targetSectorList[1]:
					targetSystemPair.append(self._galaxy.aSystemList[l])
					
			#Create a lane
			laneA = Hyperlane(self._galaxy.aSystemList[i], targetSystemPair[0])
			laneB = Hyperlane(self._galaxy.aSystemList[i], targetSystemPair[1])
			#The first pair is safe, put them directly in the list
			if not self._galaxy._hyperlaneList:
				self._galaxy._hyperlaneList.append(laneA)
				self._galaxy._hyperlaneList.append(laneB)
			#Then for the next ones, check for duplicates before adding to the list
			for k in range(0, len(self._galaxy._hyperlaneList)):	
				if laneA != self._galaxy._hyperlaneList[k]:
					self._galaxy._hyperlaneList.append(laneA)
					#print(laneA.getSystemPair())
					break
					
			for k in range(0, len(self._galaxy._hyperlaneList)):
				if laneB != self._galaxy._hyperlaneList[k]:
					self._galaxy._hyperlaneList.append(laneB)
					#print(laneB.getSystemPair())
					break					
			#while targetSystemFound != 2 :
				#randX = random.randint(sytemI[0] - 1, sytemI[0] + 1)
				#randY = random.randint(sytemI[1] - 1, sytemI[1] + 1)
				#aRandPos = [randX, randY]
				#print(aRandPos)
				
				#if self.isMatrixPositionValid(aRandPos) and aRandPos != [sytemI[0], sytemI[1]]:
					#targetSectorList.append(aRandPos)
					#targetSystemFound = targetSystemFound+1
		
		
		
	def generateNewGame(self):
		
		print("New game")
		print("Generate a new Galaxy")
		self._galaxy = Galaxy()
		print("Generate System list")
		
		#Retrieve the name list file and shuffle it
		aNameFile = open("Name_list.txt", "r")
		aNameList = parseNameList(aNameFile)
		random.shuffle(aNameList)
		
		#Generate a list of system with random position
		
		#Old style, full randomized. Causes clusterization
		#for i in range(0, self._galaxy._size):
			#aSystem = StellarSystem(self._galaxy._dimension)
			##aSystem.generateSystem(self._galaxy._dimension)
			#aSystem._name = aNameList[i]
			#self.populateSystem(aSystem)
			#self._galaxy.aSystemList.append(aSystem)
			
		aSectorMatrix = self._galaxy._sectorMatrix
		aGalaxySquaredDimension = self._galaxy._dimension[0] // self._galaxy.getSquaredSize()
		
		count = 0
		for x in range(0, self._galaxy.getSquaredSize()):
			for y in range(0, self._galaxy.getSquaredSize()):
				aXBound = (x * aGalaxySquaredDimension, (x+1) * aGalaxySquaredDimension)
				aYBound = (y * aGalaxySquaredDimension, (y+1) * aGalaxySquaredDimension)
				aSystem = StellarSystem(aXBound, aYBound, (x, y))
				#aSystem.generateSystem(self._galaxy._dimension)
				aSystem._name = aNameList[count]
				count = count +1
				self.populateSystem(aSystem)
				self._galaxy.aSystemList.append(aSystem)				
		
		self.generateHyperlane()
	
	def isMatrixPositionValid(self, iPosition):
		aMatrixSize = self._galaxy.getSquaredSize()
		aPosX = (iPosition[0] >= 0) and (iPosition[0] < aMatrixSize)
		aPosY = (iPosition[1] >= 0) and (iPosition[1] < aMatrixSize)
		return aPosX and aPosY