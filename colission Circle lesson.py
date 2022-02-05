# Include library
import pygame, sys, math
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
def CircleCollision(center1, radius1, center2, radius2):
    d = math.sqrt((center1[0]-center2[0])**2 + (center1[1]-center2[1])**2)
    if d <= radius1 + radius2:
        return True
    return False

# set parameter for 2 circles
center1 = [0, 0]
radius1 = 20
center2 =[150, 150]
radius2 = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)

    #get position of cursor
    center1[0], center1[1] = pygame.mouse.get_pos()

    pygame.draw.circle(DISPLAYSURF, YELLOW , center2, radius2)
    if CircleCollision(center1, radius1, center2, radius2) == True:
        pygame.draw.circle(DISPLAYSURF, RED, center1, radius1)
    else:
        pygame.draw.circle(DISPLAYSURF, GREEN, center1, radius1)

    pygame.display.update()
    fpsClock.tick(FPS)