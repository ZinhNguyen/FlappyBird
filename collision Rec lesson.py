# Include library
import pygame, sys
from pygame.locals import *

# Set Variable for Screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# Set colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# init pygame
pygame.init()

# Set FPS
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Check Collison
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
        return True
    return False
# Set Moving Rec
rect1 = [0, 0, 80, 50]

# Set stable Rec
rect2 = [150, 150, 90, 60]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)

    #get position of cursor
    rect1[0], rect1[1] = pygame.mouse.get_pos()

    pygame.draw.rect(DISPLAYSURF, YELLOW , rect2)
    if rectCollision(rect1, rect2) == True:
        pygame.draw.rect(DISPLAYSURF, RED, rect1)
    else:
        pygame.draw.rect(DISPLAYSURF, GREEN, rect1)

    pygame.display.update()
    fpsClock.tick(FPS)