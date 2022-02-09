import pygame
from Image import screen as sc
from Function import rotateBird as rb

SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
# Set constants variable for Bird
BIRDWIDTH = 60
BIRDHEIGHT = 40
G = 0.5
SPEEDFLY = -9

# Load bird
BIRD_MID = pygame.image.load('Sources/images/yellowbird-midflap.png')
BIRD_MID = pygame.transform.scale(BIRD_MID, (BIRDWIDTH, BIRDHEIGHT))

BIRD_DOWN = pygame.image.load('Sources/images/yellowbird-downflap.png')
BIRD_DOWN = pygame.transform.scale(BIRD_DOWN, (BIRDWIDTH, BIRDHEIGHT))

BIRD_UP = pygame.image.load('Sources/images/yellowbird-upflap.png')
BIRD_UP = pygame.transform.scale(BIRD_UP, (BIRDWIDTH, BIRDHEIGHT))

BIRD_LIST = [BIRD_DOWN, BIRD_MID, BIRD_UP]
BIRD_INDEX = 0
BIRD = BIRD_LIST[BIRD_INDEX]

BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 50)

class Bird():
    def __init__(self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/2 - 30
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
            self.Angle += 180
            self.speed = SPEEDFLY
        if self.Angle > 20:
            self.Angle = 20
        if self.Angle < -90:
            self.Angle = -90
