# Include library
import pygame, sys, math
from pygame.locals import *

# Set Variable for Screen
WINDOWWIDTH = 800
WINDOWHEIGHT = 640

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
def Collision(surface1, pos1, surface2, pos2):
    mask1 = pygame.mask.from_surface(surface1)
    mask2 = pygame.mask.from_surface(surface2)
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    if mask1.overlap(mask2, (x ,y)) != None:
        return True
    return False

# set parameter for 2 shapes
star1 = pygame.image.load('star1.png')
star1 = pygame.transform.scale(star1, (120, 120))
star1_pos = [0, 0]

star2 = pygame.image.load('star2.png')
star2 = pygame.transform.scale(star2, (100, 100))
star2_pos = [300, 300]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)

    #get position of cursor
    star1_pos = pygame.mouse.get_pos()

    DISPLAYSURF.blit(star2, star2_pos)
    DISPLAYSURF.blit(star1, star1_pos)
    if Collision(star1, star1_pos, star2, star2_pos) == True:
        pygame.draw.rect(DISPLAYSURF, RED, (50, 350, 300, 40))

    pygame.display.update()
    fpsClock.tick(FPS)