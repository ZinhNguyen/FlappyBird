import pygame
from Utils import constant as const

WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT

# Display Screen
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Set Fps Clock
fpsClock = pygame.time.Clock()