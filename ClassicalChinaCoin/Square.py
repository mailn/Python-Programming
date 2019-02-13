class Square:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self, b=1):
        self._side = int(b)
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getSide(self):
        return self._side
    def setSide(self, b):
        self._side = int(b)
    def isLarge(self):
        return self._side > 10

    ############################
    # Implementor function
    ############################
    def toString(self):
        return "* Side= " + str(self._side)
    def area(self):
        return self._side * self._side
    def perimeter(self):
        return self._side * 4