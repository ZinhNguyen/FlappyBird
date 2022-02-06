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

### Create Class for car ###
class Car():
    def __init__(self):
        # Set x coordinate
        self.x = 0

        # Set surface for car
        self.surface = pygame.Surface((120, 50), SRCALPHA)
        pygame.draw.polygon(self.surface, RED, ((15, 0), (65, 0), (85, 15), (110, 15), (120, 20), (120, 35), (115, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, BLUE, (15, 40), 10)
        pygame.draw.circle(self.surface, BLUE, (85, 40), 10)

    # Draw car
    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, 100))

    # Update car
    def update(self):
        self.x +=2
        if self.x + 120 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 120

car = Car()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    print(car.x)
    car.draw()
    car.update()
    pygame.display.update()
    fpsClock.tick(FPS)