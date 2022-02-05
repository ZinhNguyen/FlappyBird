# Add all library
import pygame, sys
from pygame.locals import *

# Init pygame
pygame.init()

# Set screen for game
Displaysurf = pygame.display.set_mode((1080, 640))

# Set title
pygame.display.set_caption('Hello world')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Displaysurf.fill((255, 255, 255))

    surface2rec = pygame.Surface((150, 80))
    surface2rec.fill((0, 255, 0))
    pygame.draw.rect(surface2rec, (255, 0, 0), (20, 20, 50, 20))
    Displaysurf.blit(surface2rec, (100, 80))

    pygame.display.update()