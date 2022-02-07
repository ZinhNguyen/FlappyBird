import pygame, sys
from pygame.locals import *
from Image import screen as sc
from Image import background as bg

BG = bg.BACKGROUND
SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
FPS = sc.FPS
fpsClock = sc.fpsClock

def Loading(bird):
    bird.__init__()

    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('FLAPPY BIRD', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Click to start', True, (0, 0, 0))
    commentSize = commentSuface.get_size()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return

        SCREEN.blit(BG, (0, 0))
        bird.draw()
        bg.draw_screen(0)
        SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0] ) /2), 100))
        SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0] ) /2), 500))

        pygame.display.update()
        fpsClock.tick(FPS)