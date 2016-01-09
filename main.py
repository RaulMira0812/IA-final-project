import pygame
import sys
import Tile
from pygame.locals import *

def main():
    pygame.init()
    M = []
    for i in range(10):
        a = [0] * 20
        M.append(a)
    """
    M[0][0] = 1
    M[9][0] = 1
    M[0][19] = 1
    M[9][19] = 1

    """
    for i in range(10):
        for j in range(20):
            M[i][j] = Tile.Tile(i, j)
    llenarCasillas(M)
    ventanaP = pygame.display.set_mode((330, 460))  # x,y
    tablero = pygame.image.load("mena.jpg")
    pygame.display.set_caption("My Hello World")
    xIni = 0
    yIni = 0
    xFug = 3
    yFug = 3
      # cuadro = (xIni + xFug, yIni + yFug, 40, 15)  # iniX,iniY,distX,distY

    ventanaP.blit(tablero, (0, 0))

    while True:
        xIni = 0
        yIni = 0
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        for j in range(20):
            # print ((xIni + xFug + 40))
            # iniX,iniY,distX,distY
            for i in range(10):
                xIni = i * 30
                yIni = j * 20
                cuadro = (xIni + (xFug * i), yIni + (yFug * j), 30, 20)
                pintarCasilla(M, i, j, ventanaP, cuadro)
        # cuadro = (50, 100, 40, 15)
        # pygame.draw.rect(ventanaP, color, cuadro)
        pygame.display.update()

def pintarCasilla(M, x, y,ventana,cuadro):
    if M[x][y].getOccupied() != 0:
        pygame.draw.rect(ventana, M[x][y].getColor(), cuadro)

def llenarCasillas(M):
    for i in range(10):
        for j in range(20):
            if copTile(i, j) == 1:
                M[i][j].setOccupied(1)

def copTile(x, y):
    if(x == 0 and y == 0 or x == 9 and y == 0 or x == 0 and y == 19 or x == 9 and y == 19):
        return 1
    return 0

main()