class AncientObject:
    def __init__(self, age, metal):
        self._age = age
        self._metal = metal
    
    def __del__(self):
        pass
    
    def getAge(self):
        return self._age
        
    def setAge(self, age):
        self._age = age
        
    def getMetal(self):
        return self._metal
        
    def setMetal(self, metal):
        self._metal = metal

    def isOld(self):
        return self._age > 1000
        
    def destroy(self):
        self._age = -1
        
    def toString(self):
        return "* Age: " + str(self.getAge()) + "\n" + str(self.getMetal().toString())
    