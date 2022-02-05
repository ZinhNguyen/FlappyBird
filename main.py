# Add all library
import pygame, sys
from pygame.locals import *

# Init pygame
pygame.init()

# Set screen for game
Displaysurf = pygame.display.set_mode((1080, 400))
pygame.display.set_caption('Hello world')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()