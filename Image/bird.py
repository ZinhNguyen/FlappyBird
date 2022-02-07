import pygame
from Image import screen as sc

SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
# Set constants variable for Bird
BIRDWIDTH = 50
BIRDHEIGHT = 45
G = 0.5
SPEEDFLY = -8
# Load bird
BIRD = pygame.image.load('Sources/images/bird1.png')
BIRD = pygame.transform.scale(BIRD, (BIRDWIDTH, BIRDHEIGHT))

class Bird():
    def __init__(self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/2
        self.y = (WINDOWHEIGHT - self.height)/2
        self.speed = 0
        self.surface = BIRD

    def draw(self):
        SCREEN.blit(self.surface, (int(self.x), int(self.y)))

    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G
        if mouseClick == True:
            self.speed = SPEEDFLY