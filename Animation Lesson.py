import pygame, sys
from pygame.locals import *

# Set Variable for Screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Init pygame
pygame.init()

### Set FPS for game ###
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Animation')

### Create Surface for car ###
# Set x coordinate
car_x = 0
carSurface = pygame.Surface((120, 50), SRCALPHA)
pygame.draw.polygon(carSurface, RED, ((15, 0), (65, 0), (85, 15), (110, 15), (120, 20), (120, 35), (115, 40), (0, 40), (0, 15)))
pygame.draw.circle(carSurface, BLUE, (15, 40), 10)
pygame.draw.circle(carSurface, BLUE, (85, 40), 10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(carSurface, (car_x, 100))

    ### Change position of car ###
    car_x +=5
    if car_x + 120 > WINDOWWIDTH:
        car_x = WINDOWWIDTH - 120
    pygame.display.update()
    fpsClock.tick(FPS)