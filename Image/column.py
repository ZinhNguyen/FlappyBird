import pygame
import random
from Utils import constant as const
from Utils import variables as var

SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT

# Set constants variable for Column
COLUMNWIDTH = const.COLUMNWIDTH
COLUMNHEIGHT = const.COLUMNHEIGHT
BLANK = const.BLANK
DISTANCE = const.DISTANCE
COLUMNSPEED = const.COLUMNSPEED
COLUMN_URL = const.COLUMN_URL
COLUMNIMG = pygame.image.load(COLUMN_URL)
COLUMNIMG = pygame.transform.scale(COLUMNIMG, (COLUMNWIDTH, COLUMNHEIGHT))
DELAY_PLAYING = const.DELAY_PLAYING

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
            x = DELAY_PLAYING + i*self.distance
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
