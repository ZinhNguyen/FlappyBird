import pygame
from Image import screen as sc

SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT

# Load Background
BACKGROUND = pygame.image.load('Sources/images/background1.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))

# Add moving screen for Background
M_SCREEN = pygame.image.load('Sources/images/floor.png')
M_SCREEN = pygame.transform.scale2x(M_SCREEN)

# Add Arrow for Background
ARROW = pygame.image.load('Sources/images/arrow1.png')
ARROW = pygame.transform.scale(ARROW, (60, 50))

# Add Logo for Background
LOGO = pygame.image.load('Sources/images/logo.png')
LOGO = pygame.transform.scale(LOGO, (350, 80))
LOGO_WIDTH = LOGO.get_width()

def draw_screen(M_SCREEN_X_POS):
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS, 600))
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS + WINDOWWIDTH + 25, 600))
