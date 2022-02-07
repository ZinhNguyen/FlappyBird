import pygame
from Image import screen as sc
from Function import rotateBird as rb

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
#rotated_bird = rb.rotate_bird(BIRD, Angle)
class Bird():
    def __init__(self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/2
        self.y = (WINDOWHEIGHT - self.height)/2
        self.speed = 0
        self.surface = BIRD
        self.Angle = 0

    def draw(self):
        SCREEN.blit(rb.rotate_bird(BIRD, self.Angle), (int(self.x), int(self.y)))

    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G
        self.Angle -= G*self.speed
        if mouseClick == True:
            self.Angle += 45
            self.speed = SPEEDFLY
        if self.Angle > 45:
            self.Angle = 45
        if self.Angle <= -90:
            self.Angle = -90

