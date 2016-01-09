import pygame

class Board():

    def __init__(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def llenarCasillas(self):
        for i in range(10):
            for j in range(20):
                if self.copTile(i, j) == 1:
                    self.board[i][j].setOccupied(1)

    def copTile(self, x, y):
        if(x == 0 and y == 0 or x == 9 and y == 0 or x == 0 and y == 19 or x == 9 and y == 19):
            return 1
        return 0

    def pintarCasilla(self, x, y,ventana,cuadro):
        if self.board[x][y].getOccupied() != 0:
            pygame.draw.rect(ventana, self.board[x][y].getColor(), cuadro)

    def getNeighborsList(self,x,y):
        lNeig = []
        for i in range(3):
            for j in range(3):
                if x - 1 + i >= 0 and x - 1 + i < 10 and y - 1 + j >= 0 and y - 1 + j < 20:
                    if self.board[x - 1 + i][y - 1 + j].getType != 0:
                        if x - 1 + i != x or y - 1 + j != y:
                            lNeig.append(self.board[x - 1 + i][y - 1 + j])
                            #print ((str(x - 1 + i) + ":" + str(y - 1 + j)))