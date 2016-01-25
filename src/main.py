#!/usr/bin/env python
import pygame
import sys
import Board
import random
import Dice
import Graph
import Image
from PathFinding import Node,PathFinding
from pygame.locals import *

def throwDice():
    return random.randrange(1, 7)


def main():
    #Initialize variables
    pygame.init()
    globalTile = None
    lastSelected = None
    lAdy = None
    fps = pygame.time.Clock()
    dice = Dice.Dice()
    turno = -1  #zero if cop, one if burglar
    throwed = 0
    numDado = 0
    white = (255, 64, 64)
    fuente1 = pygame.font.SysFont(None, 20, False, True)
    textPolice = fuente1.render("Cops: ", 0, (0, 255, 0))
    textBurglar = fuente1.render("Burglars: ", 0, (0, 255, 0))
    textPlaces = fuente1.render("No Stoled: ", 0, (0, 255, 0))
    textDice = fuente1.render("Steps left: ", 0, (0, 255, 0))
    #creation of the board 10x20
    board = Board.Board([])
    for i in range(10):
        a = [0] * 20
        board.getBoard().append(a)

    board.loadBoard()

    board.llenarCasillas()

    #screen = pygame.display.set_mode((600,600))
    ventanaP = pygame.display.set_mode((950, 460))  # x,y (Tablero 330, 460)
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
    #print ("/********************PathFinding***********************/")
    #vecinos=board.getNeighborsList(0, 0)
    #for i in range(len(vecinos)):
        #path = PathFinding(board=board.board, initPos=[vecinos[i].x, vecinos[i].y], goalPos=[3, 4])
        #print (("The final path from [0, 0] through " + str(vecinos[i].x) + " is :" + str(vecinos[i].y), path.goalPath))

    print ("Choose 4 tiles for starting the game")
    countIniLadron = 0

    while True:
        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
        dice.drawDice(ventanaP, (350, 400, 45, 45)) #draw the dice GUI
        xIni = 0
        yIni = 0
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                selTile = board.getMouseSelectedTile(pos) #get the tile selected by the user
                globalTile = selTile
                if selTile is not None and selTile.stoled == 0: #if selected tile hasnt been stolen

                    if selTile.occupied == 0: #if the tile is not occupied

                        if lAdy is not None: #lAdy = if list of Adjacents has elements

                            for i in range(len(lAdy)): #for each element in the list of adjacents

                                #if the selected tile is not in the list
                                if selTile is not lAdy[i]:
                                    lAdy[i].near = 0 #paint as a regular tile (not neighbor)

                                #if the selected tile is a neighbor (is on the list)
                                else:
                                    #if the player still has movements
                                    if lastSelected.coin.leftMov > 0:
                                        selTile.setOccupied(2) #then move and set occupied by a burglar
                                        selTile.coin = lastSelected.coin
                                        #if the burglar is standed on a store and it hasnt been stoled
                                        if selTile.type == 1 and selTile.stoled == 0:
                                            selTile.stoled = 1; #then set the store as stoled
                                            selTile.coin.leftMov = 0 #prohibit the burglar to move until next movement
                                        #If the burglar is not standed on a store just move and decrease movements
                                        else:
                                            selTile.coin.countDownMoves()
                                    #if the player does not have movements
                                    else:
                                        board.cleanAllNear() #move and hide all the neighbors
                            if selTile.occupied == 2: #if tile is occupied by a burglar
                                numDado = numDado - 1
                                lastSelected.setOccupied(0)
                                lastSelected.coin = None
                            lAdy = None
                    else: #if the tile is occupied, then hide the adjacents
                        board.cleanAllNear()


                if selTile is None: #if the player hasnt selected a tile
                    if dice.isDiceSelect(pos) and throwed == 0 and turno == 1: #if the user select the dice and it hasnt been throw and is its turn
                        for abc in range(random.randrange(30, 60)):
                            #throw the dice
                            pygame.display.update()
                            ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
                            pygame.time.wait(20 + abc / 2)
                            dice.setSelectDice(throwDice() - 1)
                            dice.drawDice(ventanaP, (170, 200, 90, 90))
                        pygame.display.update()
                        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
                        dice.drawDice(ventanaP, (170, 200, 90, 90))
                        pygame.time.wait(666)
                        throwed = 1 #set as throwed
                        numDado = dice.selectDice + 1  #get the number

                else: #if the player has selected a tile

                    #let the player place its four burglars on the board
                    if countIniLadron < 4 and board.isBurglarStartPoint(selTile.x, selTile.y) and selTile.occupied == 0:
                        selTile.setOccupied(2)
                        countIniLadron = countIniLadron + 1
                        if countIniLadron == 4:
                            turno = 1


        if turno == 1 and throwed == 1 and globalTile is not None:  #if its burglar (player) turn and if the player already throwed the dice

            if board.noMovesPermissionsFor(2) == 1: #if all the burglars on the board have wasted all their movements
                board.resetMovesByCoin(2) #reset the movements allowed to the maximun (3 each burglar)
                turno = 0 #set the turn to the cop
                throwed = 0 #set the dice as not throwed
            else: #if there are still burglars that have movements left

                if numDado != 0: #and the player still have dice numbers
                    if globalTile.occupied == 2:  #if the tile is a burglar

                        if globalTile.coin.leftMov != 0: #if it still have movements left
                            lastSelected = globalTile
                            lAdy = board.setNeighborsList(globalTile.x, globalTile.y) #set the neighbors tiles where it can move
                        else:
                            board.cleanAllNear() #hide the tiles where it can move
                else: #if the player have no more dice numbers
                    board.resetMovesByCoin(2) #reset movements for the coin
                    turno = 0 #give the turn to the police
                    throwed = 0 #set dice as not throwed


        if turno == 0: #if the turn if for the PC (cop)
            #print "cop turn"
            moved = 0
            if throwed == 0: #if the dice hasnt been throwed
                numDado = throwDice() #throw it
                throwed = 1
                print numDado
            else:
                tmp = 0
                tmp2 = 0
                tam = 100
                cops = board.selectAllPolices() #get the list of polices in the board com movimientos disponibles




                if len(cops) != 0:
                    for i in range(len(cops)): #for each cop on the board
                        cops[i].coin.setListMov(board.getNeighborsList(cops[i].x, cops[i].y), board) #set the neighbors
                    for i in range(len(cops)): # The best police is selected for the movement
                        for j in range(len(cops[i].coin.countListMov)):
                            if tam > cops[i].coin.countListMov[j]:
                                tmp = i
                                tmp2 = j
                                tam = cops[i].coin.countListMov[j]
                                root = "["+str(cops[i].x)+","+str(cops[i].y)+"]"
                                taml=len(board.getNeighborsList(cops[i].x, cops[i].y))
                                listnei=board.getNeighborsList(cops[i].x, cops[i].y)
                                levels = ["[0,0]","[0,0]","[0,0]","[0,0]","[0,0]","[0,0]","[0,0]","[0,0]","[0,0]"]
                                for k in range(len(listnei)):
                                    levels[k] = "["+str(listnei[k].x)+","+str(listnei[k].y)+"]"

                                a = Graph.CustomTree(root = root,leafs=levels)
                                #a.addLevels(root = "[2,3]",leafs=["[5,6]","[7,8]"])
                                a.draw()
                                filename = "example.png" # ensure filename is correct
                                img=pygame.image.load(filename)
                                img = pygame.transform.scale(img, (500,150))
                                ventanaP.blit(img, (420, 20))

                                #ventanaP.blit(img, (400,460))
                                #pygame.display.update()
                                #fps.tick(100)
                                #pygame.display.flip()



                    # print "SelectedCop:"+str(cops[tmp].x)+":"+str(cops[tmp].y)
                    #selecciona casilla a ubicarse y le entrega el coin
                    selTile = cops[tmp].coin.listMov[tmp2]
                    if selTile.occupied == 2: #Si la posicion que tomara esta ocupada por ladron
                        print "Atrapado"
                        cops[tmp].coin.leftMov = 1 #Indica que le queda un movimiento (El que realizara)
                    selTile.setOccupied(1) #then move and set occupied by a cop
                    selTile.coin = cops[tmp].coin
                    selTile.coin.countDownMoves()
                    cops[tmp].setOccupied(0)
                    cops[tmp].coin = None
                    numDado = numDado - 1
                    pygame.time.wait(666)
                else:
                    numDado = 0
                if numDado == 0: #Si policia usa todos sus movimientos, termina su turno o no tiene movimientos posibles
                    turno = 1
                    throwed = 0
                    board.resetMovesByCoin(1)
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
        pygame.display.update()
        ventanaP.fill((0, 0, 0), (0, 0, 420, 460))
        fuente1 = pygame.font.SysFont(None, 30, False, True)
        textGanador = fuente1.render("Ganador", 0, (0, 255, 0))
        ventanaP.blit(textGanador, (0, 0))
        if board.countByCoin(2) == 0:
            textWho = fuente1.render("Policia", 0, (0, 255, 0))
        else:
            textWho = fuente1.render("Ladron", 0, (0, 255, 0))
        ventanaP.blit(textWho, (100, 60))
        textCount = fuente1.render("Faltaron por robar: "+str(board.countNoStoled())+" Tiendas", 0, (0, 255, 0))
        ventanaP.blit(textCount, (60,100))
        pygame.display.update()
        pygame.time.wait(666)
        i = i + 1
main()
