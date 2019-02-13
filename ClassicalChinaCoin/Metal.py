class Metal:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self, b):
        self._material = b
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getMaterial(self):
        return self._material
    def setMaterial(self, b):
        self._material = b
    def isGold(self):
        return self._material == "gold"

    ############################
    # Implementor function
    ############################
    def toString(self):
        return "* Material= " + str(self._material)
    def changeMaterial(self, b):
        self._material = b
