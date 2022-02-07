import pygame
import random
from Image import screen as sc

SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT

# Set constants variable for Column
COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 3
COLUMNIMG = pygame.image.load('Sources/images/column.png')
COLUMNIMG = pygame.transform.scale(COLUMNIMG, (COLUMNWIDTH, COLUMNHEIGHT))

class Columns():
    def __init__(self):
        self.width = COLUMNWIDTH
        self.height = COLUMNHEIGHT
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = COLUMNSPEED
        self.surface = COLUMNIMG
        self.ls = []
        for i in range(3):
            x = WINDOWWIDTH + i*self.distance
            y = random.randrange(40, WINDOWHEIGHT - self.blank - 200, 20)
            self.ls.append([x, y])

    def draw(self):
        for i in range(3):
            SCREEN.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            SCREEN.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))

    def update(self):
        for i in range(3):
            self.ls[i][0] -= self.speed
        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = random.randrange(40, WINDOWHEIGHT - self.blank - 200, 10)
            self.ls.append([x, y])