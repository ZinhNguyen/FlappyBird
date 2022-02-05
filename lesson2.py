# Add all library
import pygame, sys
from pygame.locals import *

# Init pygame
pygame.init()

# Set screen for game
DISPLAYSURF = pygame.display.set_mode((800, 640))

# Set title
pygame.display.set_caption('Hello world')

# Create colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(DISPLAYSURF, RED, (10, 10, 100, 50))
    # Draw rectangle with no color inside
    pygame.draw.rect(DISPLAYSURF, GREEN, (150, 10, 100, 50), 2)
    # Draw Circle
    pygame.draw.circle(DISPLAYSURF, RED, (50, 100), 20)
    # Draw Circle without color inside
    pygame.draw.circle(DISPLAYSURF, BLUE, (200, 100), 20, 2)
    # Draw ellipse
    pygame.draw.ellipse(DISPLAYSURF, RED, (10, 150, 100, 50))
    # Draw ellipse without colors inside
    pygame.draw.ellipse(DISPLAYSURF, BLUE, (150, 150, 100, 50), 2)
    # Draw polygon
    pygame.draw.polygon(DISPLAYSURF, RED, ((10, 220), (150, 230), (100, 290), (30, 270)))
    # Draw polygon without colors inside
    pygame.draw.polygon(DISPLAYSURF, GREEN, ((160, 220), (310, 230), (260, 290), (180, 270)), 2)

    pygame.display.update()
