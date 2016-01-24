#import Burglar
import pygame
import PathFinding

class Cop():

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.objective = None
        self.tile = None
        self.listMov = None
        self.countListMov = None
        self.imagen = pygame.image.load("police.png")

    def setListMov(self,listmov):
        self.listMov = listmov

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