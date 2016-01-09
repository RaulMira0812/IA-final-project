class Tile():

    def __init__(self, x, y):
        self.occupied = 0

    def setOccupied(self, tipo):
        self.occupied = tipo

    def getOccupied(self):
        return self.occupied

    def getColor(self):
        if(self.occupied == 1):
            return (25, 10, 200)