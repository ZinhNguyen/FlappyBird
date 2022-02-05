import pygame, sys
from pygame.locals import *

# Set size for Screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# set Colors

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Init pygame
pygame.init()

# Set FPS for game
FPS = 60
fpsClock = pygame.time.Clock()

# Create Surface for Screen
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('TEXT')

# Set font for TEXT
font = pygame.font.SysFont('consolas', 30)
textSurface = font.render('Hello world', False, GREEN, 'blue')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurface, (50, 100))

    pygame.display.update()
    fpsClock.tick(FPS)
