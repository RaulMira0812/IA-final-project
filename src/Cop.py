#import Burglar
import pygame
import Graph
from PathFinding import Node,PathFinding

class Cop():

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.objective = None
        self.tile = None
        self.leftMov = 2
        self.listMov = None
        self.countListMov = None
        self.imagen = pygame.image.load("police.png")

    def setListMov(self, listmov, board):
        self.countListMov = []
        self.listMov = listmov
        if self.listMov is not None:
            for i in range(len(self.listMov)):
                iniX = self.listMov[i].x
                iniY = self.listMov[i].y
                #print str(iniX)+":"+str(iniY)
                goalPoint = board.getNearBurglar(iniX, iniY)
                #print "burglar "+str(goalPoint.x)+":"+str(goalPoint.y)
                if iniX == goalPoint.x and iniY == goalPoint.y:
                    self.countListMov.append(1)
                else:
                    path = PathFinding(board=board.board, initPos=[iniX, iniY], goalPos=[goalPoint.x, goalPoint.y])
                    self.countListMov.append(len(path.goalPath) + 1)

    def getListMov(self):
        return self.listMov

    def setXposition(self, x):
        self.xpos = x

    def getXposition(self):
        return self.xpos

    def setYposition(self, y):
        self.ypos = y

    def getTile(self):
        return self.tile

    def movePolice(self, tile):
        if tile.type == 2:  # if next tile is a space (neither a wall nor a place)
            self.tile = tile
            self.xpos = tile.x
            self.ypos = tile.y
            tile.occupied = 1  # The tile its been occupied by a police
        else:
            print("You cant move there")

    def getBurglarTarget(self):
        return self.objective

    def setBurglarTarget(self, burglar):
        self.objective = burglar

    def getPlayerState(self):
        return self.state

    def countDownMoves(self):
        self.leftMov = self.leftMov - 1

    def resetMoves(self):
        self.leftMov = 2