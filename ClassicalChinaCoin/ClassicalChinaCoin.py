from AncientObject import AncientObject

class ClassicalChinaCoin(AncientObject):
    def __pi(self):
        return 3.1416
    
    def __init__(self, radius, square, age, metal):
        AncientObject.__init__(self, age, metal)
        self._radius = float(radius)
        self._square = square
    
    def __del__(self):
        pass
    
    def getRadius(self):
        return self._radius
        
    def setRadius(self, radius):
        self._radius = float(radius)
        
    def getSquare(self):
        return self._square
        
    def setSquare(self, square):
        self._square = square

    def area(self):
        return self._radius * self._radius * self.__pi() - self.getSquare().area()
    
    def isValid(self):
        return self.area() > 0
        
    def destroy(self):
        self._radius = -1
    
    def toString(self):
        return "* Radius: " + str(self.getRadius()) + "\n" + str(self.getSquare().toString()) + "\n* Age: " + str(self.getAge()) + "\n" + str(self.getMetal().toString())