import pygame, sys
from pygame.locals import *
from Image import screen as sc
from Image import background as bg
from Image import column as co
from Function import flyLoading as fl

BG = bg.BACKGROUND
SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
FPS = sc.FPS
fpsClock = sc.fpsClock
SCREEN_SPEED = co.COLUMNSPEED

def Loading(bird):
    bird.__init__()
    M_SCREEN_X_POS = 0
    # font = pygame.font.SysFont('consolas', 60)
    # headingSuface = font.render('FLAPPY BIRD', True, (255, 0, 0))
    # headingSize = headingSuface.get_size()
    #
    # font = pygame.font.SysFont('consolas', 20)
    # commentSuface = font.render('Click to start', True, (0, 0, 0))
    # commentSize = commentSuface.get_size()
    up = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return

        SCREEN.blit(BG, (0, 0))
        # make bird fly on loading
        bird.y, up = fl.flying(up, bird.y, 5)
        bird.draw()
        # SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0] ) /2), 100))
        # SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0] ) /2), 500))
        M_SCREEN_X_POS -= SCREEN_SPEED
        if M_SCREEN_X_POS <= -WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        bg.draw_screen(M_SCREEN_X_POS)

        pygame.display.update()
        fpsClock.tick(FPS)
