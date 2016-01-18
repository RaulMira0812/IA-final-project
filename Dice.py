import pygame
import random

class Dice():

    def __init__(self):
        self.selectDice = random.randrange(0, 6)
        self.images = []
        for i in range(6):
            self.images.append(pygame.image.load("dado" + str(i + 1) + ".png"))

    def setSelectDice(self, numDice):
        self.selectDice = numDice

    def getDiceImage(self):
        return self.images[self.selectDice]

    def isDiceSelect(self, MousePos):
        if MousePos[0] > self.cuadro[0] and MousePos[0] < self.cuadro[0] + self.cuadro[2]:
            if MousePos[1] > self.cuadro[1] and MousePos[1] < self.cuadro[1] + self.cuadro[3]:
                return 1
        return 0

    def drawDice(self, ventana, cuadro):
        self.cuadro = cuadro
        selIma = pygame.transform.scale(self.getDiceImage(), (cuadro[2], cuadro[3]))
        ventana.blit(selIma, (cuadro[0], cuadro[1]))