import pygame
import sys
import Board
import random
import Dice
from PathFinding import Node,PathFinding
from pygame.locals import *

def throwDice():
    return random.randrange(1, 7)


"""def convertLTileToLNode(board):
    lista = []
    for i in range(10):
        a = [0] * 20
        lista.append(a)

    for i in range(10):
        for j in range(20):
            lista[i][j]=convertTiletoNode(board.getBoard()[i][j])
    return lista

def convertTiletoNode(tile):
    return PathFinding.Node(pos=[tile.x, tile.y], element=tile)

def getNeighborsListNode(board,nodo):
    lNeig = []
    x = nodo.pos[0]
    y = nodo.pos[1]
    for i in range(3):
        for j in range(3):
            if x - 1 + i >= 0 and x - 1 + i < 10 and y - 1 + j >= 0 and y - 1 + j < 20:
                if board[x - 1 + i][y - 1 + j].element.getType() != 0:
                    if x - 1 + i != x or y - 1 + j != y:
                        lNeig.append(board[x - 1 + i][y - 1 + j])
    return lNeig
"""

def main():
    #Inicio variables
    pygame.init()
    globalTile = None
    lastSelected = None
    lAdy = None
    fps = pygame.time.Clock()
    dice = Dice.Dice()
    turno = -1  #cero si es policia, uno si es ladron
    throwed = 0
    numDado = 0
    fuente1 = pygame.font.SysFont(None, 20, False, True)
    textPolice = fuente1.render("Cops: ", 0, (0, 255, 0))
    textBurglar = fuente1.render("Burglars: ", 0, (0, 255, 0))
    textPlaces = fuente1.render("No Stoled: ", 0, (0, 255, 0))
    textDice = fuente1.render("Steps left: ", 0, (0, 255, 0))
    #creacion del tablero 10 * 20
    board = Board.Board([])
    for i in range(10):
        a = [0] * 20
        board.getBoard().append(a)

    """
    M[0][0] = 1
    M[9][0] = 1
    M[0][19] = 1
    M[9][19] = 1
    """
    board.loadBoard()

    board.llenarCasillas()
    ventanaP = pygame.display.set_mode((420, 460))  # x,y (Tablero 330, 460)
      # tablero = pygame.image.load("mena.jpg")
    pygame.display.set_caption("Cops and Burglars")
    xIni = 0
    yIni = 0
    xFug = 3
    yFug = 3
      # cuadro = (xIni + xFug, yIni + yFug, 40, 15)  # iniX,iniY,distX,distY
    #lista = convertLTileToLNode(board)
    #lnei = getNeighborsListNode(lista, PathFinding.Node(pos=[1, 3]))
    #for i in range(len(lnei)):
    #    print ((lnei[i].pos))

      # ventanaP.blit(tablero, (0, 0))
    print ("/********************PathFinding***********************/")
    vecinos=board.getNeighborsList(0, 0)
    for i in range(len(vecinos)):
        path = PathFinding(board=board.board, initPos=[vecinos[i].x, vecinos[i].y], goalPos=[3, 4])
        print (("El final path es desde [0, 0] por " + str(vecinos[i].x) + ":" + str(vecinos[i].y), path.goalPath))

    print ("Choose 4 tiles for starting the game")
    countIniLadron = 0

    while True:
        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
        dice.drawDice(ventanaP, (350, 400, 45, 45))
        xIni = 0
        yIni = 0
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                selTile = board.getMouseSelectedTile(pos)
                globalTile = selTile
                if selTile is not None and selTile.stoled == 0:
                    if selTile.occupied == 0:
                        if lAdy is not None:
                            for i in range(len(lAdy)):
                                if selTile is not lAdy[i]:
                                    lAdy[i].near = 0
                                else:
                                    if lastSelected.coin.leftMov > 0:
                                        selTile.setOccupied(2)
                                        selTile.coin = lastSelected.coin
                                        if selTile.type == 1 and selTile.stoled == 0:
                                            selTile.stoled = 1;
                                            selTile.coin.leftMov = 0
                                        else:
                                            selTile.coin.countDownMoves()
                                    else:
                                        board.cleanAllNear()
                            if selTile.occupied == 2:
                                numDado = numDado - 1
                                lastSelected.setOccupied(0)
                                lastSelected.coin = None
                            lAdy = None
                    else:
                        board.cleanAllNear()
                if selTile is None:
                    if dice.isDiceSelect(pos) and throwed == 0 and turno == 1:
                        for abc in range(random.randrange(30, 60)):
                            pygame.display.update()
                            ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
                            pygame.time.wait(20 + abc / 2)
                            dice.setSelectDice(throwDice() - 1)
                            dice.drawDice(ventanaP, (170, 200, 90, 90))
                        pygame.display.update()
                        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
                        dice.drawDice(ventanaP, (170, 200, 90, 90))
                        pygame.time.wait(666)
                        throwed = 1
                        numDado = dice.selectDice + 1
                else:
                    if countIniLadron < 4 and board.isBurglarStartPoint(selTile.x, selTile.y) and selTile.occupied == 0:
                        selTile.setOccupied(2)
                        countIniLadron = countIniLadron + 1
                        if countIniLadron == 4:
                            turno = 1


        if turno == 1 and throwed == 1 and globalTile is not None:
            if board.noMovesPermissionsFor(2) == 1:
                board.resetMovesByCoin(2)
                turno = 0
                throwed = 0
            else:
                if numDado != 0:
                    if globalTile.occupied == 2:
                        if globalTile.coin.leftMov != 0:
                            lastSelected = globalTile
                            lAdy = board.setNeighborsList(globalTile.x, globalTile.y)
                        else:
                            board.cleanAllNear()
                else:
                    board.resetMovesByCoin(2)
                    turno = 0
                    throwed = 0

        if turno == 0:
            moved = 0
            if throwed == 0:
                numDado = throwDice()
                throwed = 1
            else:
                polices = board.selectAllPolices()
                for i in range(len(polices)):
                    polices[i].coin.setListMov(board.getNeighborsList(polices[i].x, polices[i].y))
                #poner aqui todo lo de policia, cuando termine turno policia se hace el turno 1 es decir, se devuelve
                turno = 1
                throwed = 0
            board.cleanAllNear()

        for j in range(20):
            # print ((xIni + xFug + 40))
            # iniX,iniY,distX,distY
            for i in range(10):
                xIni = i * 30
                yIni = j * 20
                cuadro = (xIni + (xFug * i), yIni + (yFug * j), 30, 20)
                board.pintarCasilla(i, j, ventanaP, cuadro)
        for j in range(20):
            # print ((xIni + xFug + 40))
            # iniX,iniY,distX,distY
            for i in range(10):
                xIni = i * 30
                yIni = j * 20
                cuadro = (xIni + (xFug * i), yIni + (yFug * j), 30, 20)
                board.pintarFicha(i, j, ventanaP, cuadro)
        # cuadro = (50, 100, 40, 15)
        # pygame.draw.rect(ventanaP, color, cuadro)
        textNumPolic = fuente1.render(str(board.countByCoin(1)), 0, (0, 255, 0))
        textNumBurgl = fuente1.render(str(board.countByCoin(2)), 0, (0, 255, 0))
        textNumPlaces = fuente1.render(str(board.countNoStoled()), 0, (0, 255, 0))
        textNumDice = fuente1.render(str(numDado), 0, (0, 255, 0))
        ventanaP.blit(textPolice, (330, 0))
        ventanaP.blit(textNumPolic, (370, 20))
        ventanaP.blit(textBurglar, (330, 40))
        ventanaP.blit(textNumBurgl, (370, 60))
        ventanaP.blit(textPlaces, (330, 80))
        ventanaP.blit(textNumPlaces, (370, 100))
        ventanaP.blit(textDice, (330, 120))
        ventanaP.blit(textNumDice, (370, 140))
        pygame.display.update()
        fps.tick(100)
        if (board.countByCoin(2) == 0 or board.countNoStoled() == 0) and countIniLadron != 0:
            break
    i = 0
    while(i < 10):
        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
        print ("ganador")
        pygame.time.wait(100)
        i = i + 1
main()
