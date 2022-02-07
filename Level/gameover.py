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


def Over(bird, columns, score, record):
    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSuface.get_size()

    font = pygame.font.SysFont('consolas', 30)
    scoreSuface = font.render('Score: ' + str(score.score), True, (0, 0, 0))
    scoreSize = scoreSuface.get_size()

    font = pygame.font.SysFont('consolas', 30)
    recordSuface = font.render('Record: ' + str(record), True, (0, 0, 0))
    recordSize = recordSuface.get_size()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    return

        SCREEN.blit(BG, (0, 0))
        columns.draw()
        bird.draw()
        SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0] ) /2), 100))
        SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0] ) /2), 500))
        SCREEN.blit(scoreSuface, (int((WINDOWWIDTH - scoreSize[0] ) /2), 160))
        SCREEN.blit(recordSuface, (int((WINDOWWIDTH - scoreSize[0]) / 2), 200))
        bg.draw_screen(0)

        pygame.display.update()
        fpsClock.tick(FPS)