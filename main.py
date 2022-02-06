# Import library
import pygame, sys
from pygame.locals import *

# Create function for forever running
def draw_screen():
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS, 600))
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS + WINDOWWIDTH, 600))

# Set variable for Screen
WINDOWWIDTH = 432
WINDOWHEIGHT = 768


# Init pygame
pygame.init()

# Set FPS
FPS = 60
fpsClock = pygame.time.Clock()

# Load Background
BG = pygame.image.load('images/background1.png')
BG = pygame.transform.scale(BG, (WINDOWWIDTH, WINDOWHEIGHT))

# Add moving screen for Background
M_SCREEN = pygame.image.load('images/floor.png')
M_SCREEN = pygame.transform.scale2x(M_SCREEN)
M_SCREEN_X_POS = 0

# Display Screen
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


# Set constants variable for Bird
BIRDWIDTH = 60
BIRDHEIGHT = 45
G = 0.5
SPEEDFLY = -8
# Load bird
BIRD = pygame.image.load('images/bird1.png')
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

bird = Bird()
while True:
    mouseClick = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouseClick = True
    SCREEN.blit(BG, (0, 0))
    bird.draw()
    bird.update(mouseClick)
    M_SCREEN_X_POS -= 3
    if M_SCREEN_X_POS <= -WINDOWWIDTH:
        M_SCREEN_X_POS = 0
    draw_screen()
    pygame.display.update()
    fpsClock.tick(FPS)
