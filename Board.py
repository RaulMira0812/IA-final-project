import pygame
import Tile

#tipos 0-Pared 1-Tienda 2-casillero
#Ocupado 0-Vacio 1-policia 2-Ladron

class Board():

    def __init__(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def num(s):
        try:
            return int(s)
        except ValueError:
            return float(s)

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

    def getNeighborsList(self,x,y):
        lNeig = []
        for i in range(3):
            for j in range(3):
                if x - 1 + i >= 0 and x - 1 + i < 10 and y - 1 + j >= 0 and y - 1 + j < 20:
                    if self.board[x - 1 + i][y - 1 + j].getType() != 0:
                        if x - 1 + i != x or y - 1 + j != y:
                            lNeig.append(self.board[x - 1 + i][y - 1 + j])
                            #print ((str(x - 1 + i) + ":" + str(y - 1 + j)))
        return lNeig