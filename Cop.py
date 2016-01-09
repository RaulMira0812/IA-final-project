#import Burglar
import pygame


class Cop():

    def __init__(self, x, y):
        self.id = Cop.newid()
        self.xpos = x
        self.ypos = y
        self.objective = None
        self.tile = None
        self.imagen = pygame.image.load("resources\images\police.jpg")

    def setXposition(self, x):
        self.xpos = x

    def getXposition(self):
        return self.xpos

    def setYposition(self, y):
        self.ypos = y

    def getTile(self):
        return self.tile

    def movePolice(self, tile):
        if tile.type == 2:
            self.tile = tile
            self.xpos = tile.x
            self.ypos = tile.y
        else:
            print("No se puede mover a ese casillero")

    def getBurglarTarget(self):
        return self.objective

    def setBurglarTarget(self, burglar):
        self.objective = burglar

    def getPlayerState(self):
        return self.state