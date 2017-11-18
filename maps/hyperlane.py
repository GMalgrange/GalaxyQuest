from maps.StellarSystem import StellarSystem

class Hyperlane :
    def __init__(self, system1, system2):
        self._systemPair = (system1, system2)
        
    def __eq__(self, other):
        if isinstance(other, Hyperlane):
            return (self._systemPair[0] == other._systemPair[0] or self._systemPair[0] == other._systemPair[1]) and (self._systemPair[1] == other._systemPair[0] or self._systemPair[1] == other._systemPair[1])
        return self._systemPair == other._systemPair  
    def __ne__(self, other):
        if isinstance(other, Hyperlane):
            a = (self._systemPair[0]._name != other._systemPair[0]._name or self._systemPair[1]._name != other._systemPair[1]._name)  
            b = (self._systemPair[0]._name != other._systemPair[1]._name or self._systemPair[1]._name != other._systemPair[0]._name)
            #print(a and b)
        return a and b        
        
    
    def getCoordinate(self):
        #print(str(self._systemPair[0]._systemPosition[0]) + ", "+ str(self._systemPair[0]._systemPosition[1]))
        return self._systemPair[0]._systemPosition[0], self._systemPair[0]._systemPosition[1], self._systemPair[1]._systemPosition[0], self._systemPair[1]._systemPosition[1]
    
    def getSystemPair(self):
        return str(self._systemPair[0]._name) + ", " + str(self._systemPair[1]._name) + " ; "