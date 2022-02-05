import pygame, sys
from pygame.locals import *

pygame.init()

Displaysurf = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello world')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()