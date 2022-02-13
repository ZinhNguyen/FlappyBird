import pygame, sys
from pygame.locals import *
from Image import background as bg
from Image import medal as md
from Sound import gameover as so
from Utils import constant as const
from Utils import variables as var
from Image import content as ct
from Image import scoreBoard as sc

BG = bg.BACKGROUND
SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
FPS = const.FPS
fpsClock = var.fpsClock
SCORE_FONT_URL = const.SCORE_FONT_URL
SCORE_FONT_SIZE = const.SCORE_FONT_SIZE
WHITE_COLOR = const.WHITE_COLOR
GUIDEFONT_URL = const.GUIDEFONT_URL
GUIDEFONT_SIZE = const.GUIDEFONT_SIZE
BLACK_COLOR = const.BLACK_COLOR
GAMEOVER_FONT_SIZE = const.GAMEOVER_FONT_SIZE
SCORE_TITLE_FONT_URL = const.SCORE_TITLE_FONT_URL
SCORE_TITLE_FONT_SIZE = const.SCORE_TITLE_FONT_SIZE


def Over(bird, columns, score, record, mscreen, background):
    WHD_2 = const.WHD_2
    goContent = ct.Content(GUIDEFONT_URL, GAMEOVER_FONT_SIZE, 'GAMEOVER', (235, 134, 52), 100)
    goGuide = ct.Content(GUIDEFONT_URL, GUIDEFONT_SIZE, 'Press "Space" to replay', BLACK_COLOR, 530)
    scoreTitle = ct.Content(SCORE_TITLE_FONT_URL, SCORE_TITLE_FONT_SIZE, 'SCORE', (235, 134, 52), WHD_2 - 60)
    BestTitle = ct.Content(SCORE_TITLE_FONT_URL, SCORE_TITLE_FONT_SIZE, 'BEST', (235, 134, 52), WHD_2)
    MedalTitle = ct.Content(SCORE_TITLE_FONT_URL, SCORE_TITLE_FONT_SIZE, 'MEDAL', (235, 134, 52), WHD_2 - 60)
    scoreContent = ct.Content(SCORE_FONT_URL, SCORE_FONT_SIZE, str(score.score), WHITE_COLOR, WHD_2 - 35)
    BestContent = ct.Content(SCORE_FONT_URL, SCORE_FONT_SIZE, str(record), WHITE_COLOR, WHD_2 + 25)

    scoreBoard = sc.ScoreBoard()
    noMedal = md.NoMedal()
    bronzeMedal = md.BronzeMedal()
    silverMedal = md.SilverMedal()
    goldMedal = md.GoldMedal()
    diamondMedal = md.DiamondMedal()
    scoreTitle.setXplus(70)
    scoreContent.setXplus(70)
    BestTitle.setXplus(70)
    BestContent.setXplus(70)
    MedalTitle.setXminus(70)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    scoreTitle.setXminus(70)
                    scoreContent.setXminus(70)
                    BestTitle.setXminus(70)
                    BestContent.setXminus(70)
                    MedalTitle.setXplus(70)
                    so.die_sound.stop()
                    return
        background.draw()
        columns.draw()
        bird.draw()
        scoreBoard.draw()
        goContent.draw()
        goGuide.draw()
        scoreTitle.draw()
        scoreContent.draw()
        BestTitle.draw()
        BestContent.draw()
        MedalTitle.draw()
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
        mscreen.draw(0)
        bird_y = bird.getY()
        bird.setY(bird_y + 8)
        bird.Angle = -90
        if bird.getY() >= 600 - bird.getHeight():
            bird.setY(600 - bird.getHeight())
        pygame.display.update()
        fpsClock.tick(FPS)
