import pygame


class Burglar():

    def __init__(self, x, y):
        # self.id = Burglar.newid()
        self.xpos = x
        self.ypos = y
        self.tile = None
        self.leftMov = 3
        self.imagen = pygame.image.load("burglar.png")

    def resetMoves(self):
        self.leftMov = 3

    def countDownMoves(self):
        self.leftMov= self.leftMov - 1

    def setXposition(self, x):
        self.xpos = x

    def getXposition(self):
        return self.xpos

    def setYposition(self, y):
        self.ypos = y

    def getTile(self):
        return self.tile

    def moveBurglar(self, tile):
        if self.tile.type == 1:  # if current tile is a place
            print("You robbed the place succesfully")
        if tile.type != 0:  # If next tile is not a wall
            print("You cant move trough a wall")
        else:
            if tile.occupied == 0:  # If next tile is empty
                self.tile = tile  # move it
                self.xpos = tile.x
                self.ypos = tile.y
                tile.occupied = 2  # Set the tile to be occupied by a burglar
            elif tile.occupied == 1:  # If in the next tile is a police
                print("Wait! There is a police")
            elif tile.occupied == 2:  # If in the next tile is a burglar
                print("The tile is been occupied by another burglar")

    def getBurglarTarget(self):
        return self.objective

    def setBurglarTarget(self, burglar):
        self.objective = burglar

    def getPlayerState(self):
        return self.state