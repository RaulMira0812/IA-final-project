import Burglar
import Cop

class Tile():
    #types 0-Wall 1-Store 2-Regular
    #Occupied 0-Empty 1-Cop 2-Burglar
    # near indicates if the tile is a neighbor tile
    def __init__(self, x, y):
        self.occupied = 0
        self.x = x
        self.y = y
        self.type = 2
        self.coin = None
        self.near = 0
        self.stoled = 0 #0-not stolen/1-stolen

    def setCoin(self, coin):
        self.coin = coin

    def setOccupied(self, typ):
        if self.type != 0:
            self.occupied = typ
        if typ == 1:
            self.coin=Cop.Cop(self.x, self.y)
        if typ == 2:
            self.coin=Burglar.Burglar(self.x, self.y)

    def setCoord(self,cuadro):
        self.cuadro = cuadro

    def isMouseSelected(self,MousePos):
        if MousePos[0] > self.cuadro[0] and MousePos[0] < self.cuadro[0] + self.cuadro[2]:
            if MousePos[1] > self.cuadro[1] and MousePos[1] < self.cuadro[1] + self.cuadro[3]:
                return 1
        return 0

    def getOccupied(self):
        return self.occupied

    def getType(self):
        return self.type

    def getColor(self):
        #if(self.x == 3 and self.y == 4):
            #return (0, 0, 0)
        if(self.near == 1): #if the tile is a neighbor
            return (200, 200, 000) #paint it almost yellow
        if(self.occupied == 2):
            return (200, 25, 10)
        if(self.occupied == 1):
            return (25, 10, 200)
        if(self.occupied == 0):
            if self.isBurglarStartPoint(self.x, self.y) == 1:
                return (200, 150, 125)
            else:
                if self.type == 0:
                    return (200, 50, 50)
                elif self.type == 1:
                    if self.stoled == 0:
                        return (70, 220, 60)
                    else:
                        return (50, 20, 255)
                else:
                    return (200, 200, 200)

    def isBurglarStartPoint(self, x, y):
        if(x > 3 and x < 6 and y == 0):
            return 1
        if(x > 3 and x < 6 and y == 19):
            return 1
        if(y > 8 and y < 11 and x == 0):
            return 1
        if(y > 8 and y < 11 and x == 9):
            return 1
        return 0