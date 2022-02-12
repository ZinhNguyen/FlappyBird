import pygame, sys
from pygame.locals import *
from Image import screen as sc
from Image import background as bg
from Image import medal as md
from Sound import gameover as so
from Function import calculateScore as cs

BG = bg.BACKGROUND
SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
FPS = sc.FPS
fpsClock = sc.fpsClock



def Over(bird, columns, score, record):
    font = pygame.font.Font('Sources/fonts/AtariClassic.ttf', 60)
    headingSuface = font.render('GAMEOVER', True, (235, 134, 52))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSuface.get_size()

    font = pygame.font.Font('Sources/fonts/Pixel.ttf', 20)
    scoreSuface = font.render('SCORE', True, (235, 134, 52))
    scoreSize = scoreSuface.get_size()

    font = pygame.font.Font('Sources/fonts/04B_19.ttf', 40)
    scoreSuface1 = font.render(str(score.score), True, (255, 255, 255), True)
    scoreSize1 = scoreSuface1.get_size()

    font = pygame.font.Font('Sources/fonts/Pixel.ttf', 20)
    recordSuface = font.render('BEST', True, (235,134, 52))
    recordSize = recordSuface.get_size()

    font = pygame.font.Font('Sources/fonts/04B_19.ttf', 40)
    recordSuface1 = font.render(str(record), True, (255, 255, 255), True)
    recordSize1 = recordSuface1.get_size()

    font = pygame.font.Font('Sources/fonts/Pixel.ttf', 20)
    medalSurface = font.render('MEDAL', True, (235, 134, 52))
    medalSize = scoreSuface.get_size()

    WWD_2 = WINDOWWIDTH/2
    WHD_2 = (WINDOWHEIGHT - 168)/2
    WT = 260
    HT = 160
    p1 = (WHD_2 - WT/2, WHD_2 - HT/2 + 10)
    p2 = (WHD_2 - WT/2 + 3, WHD_2 - HT/2 + 3)
    p3 = (WHD_2 - WT/2 + 10, WHD_2 - HT/2)
    p4 = (WHD_2 + WT/2 - 10, WHD_2 - HT/2)
    p5 = (WHD_2 + WT/2 - 3, WHD_2 - HT/2 + 3)
    p6 = (WHD_2 + WT/2, WHD_2 - HT/2 + 10)
    p7 = (WHD_2 + WT/2, WHD_2 + HT / 2 - 10)
    p8 = (WHD_2 + WT / 2 - 3, WHD_2 + HT / 2 - 3)
    p9 = (WHD_2 + WT/2 - 10, WHD_2 + HT/2)
    p10 = (WHD_2 - WT / 2 + 10, WHD_2 + HT/2)
    p11 = (WHD_2 - WT / 2 + 3, WHD_2 + HT / 2 - 3)
    p12 = (WHD_2 - WT / 2, WHD_2 + HT/2 - 10)
    table = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)

    #md.medal(WWD_2 - 110, WHD_2 - 20)
    noMedal = md.NoMedal()
    bronzeMedal = md.BronzeMedal()
    silverMedal = md.SilverMedal()
    goldMedal = md.GoldMedal()
    diamondMedal = md.DiamondMedal()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    so.die_sound.stop()
                    return

        SCREEN.blit(BG, (0, 0))
        columns.draw()
        bird.draw()
        pygame.draw.polygon(SCREEN, (223, 214, 144), table)
        pygame.draw.polygon(SCREEN, (0, 0, 0), table,3)
        SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
        SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 500))
        SCREEN.blit(scoreSuface, (int((WINDOWWIDTH - scoreSize[0])/2) + 70, WHD_2 - 60))
        SCREEN.blit(scoreSuface1, (int((WINDOWWIDTH - scoreSize1[0])/2) + 70, WHD_2 - 35))
        SCREEN.blit(recordSuface, (int((WINDOWWIDTH - recordSize[0])/2) + 70, WHD_2))
        SCREEN.blit(recordSuface1, (int((WINDOWWIDTH - recordSize1[0])/2) + 70, WHD_2 + 25))
        SCREEN.blit(medalSurface, (int((WINDOWWIDTH - medalSize[0]) / 2) - 70, WHD_2 - 60))
        if score.score < 5:
            noMedal.draw()
        elif score.score < 10:
            bronzeMedal.draw()
        elif score.score < 15:
            silverMedal.draw()
        elif score.score < 20:
            goldMedal.draw()
        else:
            diamondMedal.draw()
        bg.draw_screen(0)
        bird.y +=8
        bird.Angle = -90
        if bird.y >= 600 - bird.height:
            bird.y = 600 - bird.height
        pygame.display.update()
        fpsClock.tick(FPS)
