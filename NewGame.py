#!/usr/bin/env python
#Generic import
import random
import math
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
		#print("Sun: "+ iSystem._name)
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
		
		aHyperlaneList = []
		
		for coord, system in self._galaxy._systemList.items():		
			#print("System "+ str(coord))
			targetSystemFound = 0
			targetSectorList = []
			#Put all valid proximity sector in a list
			for j in range(coord[0] - 1, coord[0]+2):
				for k in range(coord[1] - 1, coord[1]+2):
					if (j,k) != (coord[0], coord[1]) and self.isMatrixPositionValid((j,k)):
						targetSectorList.append((j,k))
			#Shuffle the list
			random.shuffle(targetSectorList)
			
			#Take the first 2 sectors in the list,
			#retrieve the corresponding Systems
			targetSystemPair = []
			for key, value in self._galaxy._systemList.items():
				if key == targetSectorList[0]:
					targetSystemPair.append(value)
				elif key == targetSectorList[1]:
					targetSystemPair.append(value)
					
			#Create a lane
			laneA = Hyperlane(system, targetSystemPair[0])
			laneB = Hyperlane(system, targetSystemPair[1])			
		
			#The first pair is safe, put them directly in the list
			if not aHyperlaneList:
				aHyperlaneList.append(laneA)
				aHyperlaneList.append(laneB)
			#Then for the next ones, check for duplicates before adding to the list
			for k in range(0, len(aHyperlaneList)):	
				if laneA != aHyperlaneList[k]:
					aHyperlaneList.append(laneA)
					#print(laneA.getSystemPair())
					break
					
			for k in range(0, len(aHyperlaneList)):
				if laneB != aHyperlaneList[k]:
					aHyperlaneList.append(laneB)
					#print(laneB.getSystemPair())
					break			
		
		self._galaxy._hyperlaneList = aHyperlaneList
			#while targetSystemFound != 2 :
				#randX = random.randint(sytemI[0] - 1, sytemI[0] + 1)
				#randY = random.randint(sytemI[1] - 1, sytemI[1] + 1)
				#aRandPos = [randX, randY]
				#print(aRandPos)
				
				#if self.isMatrixPositionValid(aRandPos) and aRandPos != [sytemI[0], sytemI[1]]:
					#targetSectorList.append(aRandPos)
					#targetSystemFound = targetSystemFound+1
		
		
		
	def generateNewGame(self):
		
		#print("New game")
		print("Generate a new Galaxy")
		self._galaxy = Galaxy()
		print("Generate System list")
		
		#Retrieve the name list file and shuffle it
		aNameFile = open("Name_list.txt", "r")
		aNameList = parseNameList(aNameFile)
		random.shuffle(aNameList)
		
		#Generate a list of system with random position 
		#within each square of the matrix
			
		aSectorMatrix = self._galaxy._sectorMatrix
		aGalaxySquaredDimension = self._galaxy._dimension[0] // self._galaxy.getSquaredSize()
		
		aSystemList = {}
		count = 0
		for x in range(0, self._galaxy.getSquaredSize()):
			for y in range(0, self._galaxy.getSquaredSize()):
				aXBound = (x * aGalaxySquaredDimension, (x+1) * aGalaxySquaredDimension)
				aYBound = (y * aGalaxySquaredDimension, (y+1) * aGalaxySquaredDimension)
				aSystem = StellarSystem(aXBound, aYBound, (x, y))
				aSystem._name = aNameList[count]
				count = count +1
				self.populateSystem(aSystem)
				aSystemList[(x,y)] = aSystem
				
		self._galaxy._systemList = aSystemList
		self.generateHyperlane()
	
	def isMatrixPositionValid(self, iPosition):
		aMatrixSize = self._galaxy.getSquaredSize()
		aPosX = (iPosition[0] >= 0) and (iPosition[0] < aMatrixSize)
		aPosY = (iPosition[1] >= 0) and (iPosition[1] < aMatrixSize)
		return aPosX and aPosY