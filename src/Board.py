import pygame
import Tile
from PathFinding import Node,PathFinding

class Board():

    def __init__(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def loadBoard(self):
        for i in range(10):
            for j in range(20):
                    self.getBoard()[i][j] = Tile.Tile(i, j)
                    self.getBoard()[i][j].type = 2

        with open('board.txt') as f:
           for line in f:
               currentline = line.split(",") #have the row cols information
               last = currentline[2].split("\n")[0] #third number indicates if is a wall or a place
               posix = int(currentline[0])
               posiy = int(currentline[1])
               typet = int(last)
               self.getBoard()[posix][posiy] = Tile.Tile(posix, posiy)
               self.getBoard()[posix][posiy].type = typet

    def llenarCasillas(self):
        for i in range(10):
            for j in range(20):
                if self.copTile(i, j) == 1:
                    self.board[i][j].setOccupied(1)

    def cleanAllNear(self):
        for i in range(10):
            for j in range(20):
                self.board[i][j].near = 0

    def copTile(self, x, y):
        if(x == 0 and y == 0 or x == 9 and y == 0 or x == 0 and y == 19 or x == 9 and y == 19):
            return 1
        return 0

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

    def pintarCasilla(self, x, y, ventana, cuadro):
        self.board[x][y].setCoord(cuadro)
        if self.board[x][y].getOccupied() != 0:
            pygame.draw.rect(ventana, self.board[x][y].getColor(), cuadro)
        if self.board[x][y].getOccupied() == 0:
            pygame.draw.rect(ventana, self.board[x][y].getColor(), cuadro)

    def pintarFicha(self, x, y, ventana, cuadro):
        if self.board[x][y].getOccupied() != 0:
            # ficha=pygame.image.load("police.png")
            if self.board[x][y].coin != None:
                # print str(x)+":"+str(y)
                ficha = self.board[x][y].coin.imagen
                ficha = pygame.transform.scale(ficha, (self.board[x][y].cuadro[2], self.board[x][y].cuadro[3]))
                ventana.blit(ficha,(self.board[x][y].cuadro[0], self.board[x][y].cuadro[1]))

    def getMouseSelectedTile(self, pos):
        for i in range(10):
            for j in range(20):
                if self.board[i][j].isMouseSelected(pos):
                    return self.board[i][j]
        return None

    def countByCoin(self, typeCoin):
        conteo = 0
        for i in range(10):
            for j in range(20):
                if self.board[i][j].occupied == typeCoin:
                    conteo = conteo + 1
        return conteo

    def countNoStoled(self):
        conteo = 0
        for i in range(10):
            for j in range(20):
                if self.board[i][j].type == 1 and self.board[i][j].stoled == 0:
                    conteo = conteo + 1
        return conteo

    def noMovesPermissionsFor(self, typeCoin):
        count = 0
        for i in range(10):
            for j in range(20):
                if self.board[i][j].occupied == typeCoin:
                    if self.board[i][j].coin.leftMov != 0: #if the coin have movements left
                        count = count + 1 #count how many coins have movements left
        if count == 0: #if all the coins have no movements left, answer YES noMovesPermisionForCoin
            return 1
        return 0 #Otherwise answer NO there are still coins hace movements left

    def resetMovesByCoin(self, typeCoin):
        for i in range(10):
            for j in range(20):
                if self.board[i][j].occupied == typeCoin:
                    self.board[i][j].coin.resetMoves()

    def getNeighborsList(self,x,y):
        lNeig = []
        for i in range(3):
            for j in range(3):
                if x - 1 + i >= 0 and x - 1 + i < 10 and y - 1 + j >= 0 and y - 1 + j < 20:
                    if self.board[x][y].occupied == 1:
                        if self.board[x - 1 + i][y - 1 + j].getType() != 0 and self.board[x - 1 + i][y - 1 + j].occupied != 1:
                            if x - 1 + i != x or y - 1 + j != y:
                                lNeig.append(self.board[x - 1 + i][y - 1 + j])
                    elif self.board[x][y].occupied == 2:
                        if self.board[x - 1 + i][y - 1 + j].getType() != 0 and self.board[x - 1 + i][y - 1 + j].occupied == 0:
                            lNeig.append(self.board[x - 1 + i][y - 1 + j])
        return lNeig

    def setNeighborsList(self,x,y):
        lNeig = []
        for i in range(3):
            for j in range(3):
                if x - 1 + i >= 0 and x - 1 + i < 10 and y - 1 + j >= 0 and y - 1 + j < 20:
                    if self.board[x - 1 + i][y - 1 + j].getType() != 0 and self.board[x - 1 + i][y - 1 + j].stoled == 0:
                        if x - 1 + i != x or y - 1 + j != y:
                            self.board[x - 1 + i][y - 1 + j].near = 1
                            lNeig.append(self.board[x - 1 + i][y - 1 + j])
        return lNeig

    def selectAllPolices(self):
        lPoli = []
        for i in range(10):
            for j in range(20):
                if self.board[i][j].occupied == 1:
                    if self.board[i][j].coin.leftMov != 0:
                        lPoli.append(self.board[i][j])
        return lPoli

    def selectAllBurglars(self):
        lBurglar = []
        for i in range(10):
            for j in range(20):
                if self.board[i][j].occupied == 2:
                    lBurglar.append(self.board[i][j])
        return lBurglar

    def getNearBurglar(self, x, y):
        burglars = self.selectAllBurglars()
        tmp = 0
        lenght = 100
        for j in range(len(burglars)):
            if x == burglars[j].x and y == burglars[j].y:
                return burglars[j]
            else:
                pathb = PathFinding(board = self.board, initPos = [x, y], goalPos = [burglars[j].x, burglars[j].y])
                #print(("To burglar " + str(burglars[j].x) + "," + str(burglars[j].y) + " from cop " + str(x) + "," + str(y) + ":", pathb.goalPath))
                if lenght > len(pathb.goalPath):
                    lenght = len(pathb.goalPath)
                    tmp = j
        return burglars[tmp]