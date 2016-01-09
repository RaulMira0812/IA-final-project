class Tile():

    def __init__(self, x, y):
        self.occupied = 0
        self.x = x
        self.y = y
        self.type = 2

    def setOccupied(self, typ):
        if self.type != 0:
            self.occupied = typ

    def getOccupied(self):
        return self.occupied

    def getType(self):
        return self.type

    def getColor(self):
        if(self.occupied == 1):
            return (25, 10, 200)