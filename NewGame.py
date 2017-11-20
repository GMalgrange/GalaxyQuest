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
	
class NewGame:
	
	#Generate new game	
	#For each system, generate it's celestial bodies
	#Pick any system with an inhabitable Planet
	#The pirate hideout should be placed at a safe distance 
	#relative to the Player starting position
	#Generate the CelestialBodies in a given StellarSystem
	def populateSystem(self, iSystem):
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
			print("New Planet " + iSystem._name + " " + _romanNumerals[i])
			aPlanetName = iSystem._name + " " + _romanNumerals[i]
			aPlanet = Planete(aPlanetName)
			iSystem._planeteList.append(aPlanet)
		#Generate asteroid list
		for i in range(0, randAsteroid):
			aAsteroid = Asteroid()
			iSystem._asteroidList.append(aAsteroid)
			
	def generateHyperlane(self):
		
		#Link system with hyperlanes:
		#For each system, define hyperlanes to the 2 closest systems
		#Check for redundancy.
		#Some systems may end up with more than 2 lane connexion; this is fine.
		print("Generate hyperlane connexions")
		
		for i in range(0, self._galaxy._size):
			#print("Creating hyperlane for system: " + self._galaxy.aSystemList[i]._name)
			#Calculate the system distance
			closerSystem = []
			for j in range(0, self._galaxy._size):
				x= math.pow(abs(self._galaxy.aSystemList[i]._systemPosition[0] - self._galaxy.aSystemList[j]._systemPosition[0]),2)
				y= math.pow(abs(self._galaxy.aSystemList[i]._systemPosition[1] - self._galaxy.aSystemList[j]._systemPosition[1]),2)
				h = math.sqrt(x+y)
				closerSystem.append((self._galaxy.aSystemList[j], h))
			#Sort the system list by distance
			sortedCloserList = sorted(closerSystem, key=itemgetter(1))
			#pick the 2nd and 3d one (1st is the always the current system)
			#Create a lane
			laneA = Hyperlane(self._galaxy.aSystemList[i], sortedCloserList[1][0])
			laneB = Hyperlane(self._galaxy.aSystemList[i], sortedCloserList[2][0])
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
					
		#print("Hperlane list: " + str(self._galaxy._hyperlaneList))
		
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
				aSystem = StellarSystem(aXBound, aYBound)
				#aSystem.generateSystem(self._galaxy._dimension)
				aSystem._name = aNameList[count]
				count = count +1
				self.populateSystem(aSystem)
				self._galaxy.aSystemList.append(aSystem)				
		
		self.generateHyperlane()
	
