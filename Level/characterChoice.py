import pygame, sys
from pygame.locals import *
from Image import background as bg
from Sound import characterChoice as st
from Utils import constant as const
from Utils import variables as var

BG = bg.BACKGROUND
SCREEN = var.SCREEN

LOGO_WIDTH = const.LOGO_WIDTH
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
FPS = const.FPS
fpsClock = var.fpsClock
SCREEN_SPEED = const.COLUMNSPEED
DEFAULT_BIRD_POS = const.DEFAULT_BIRD_POS
CHARACTER_SELECT_FONT_URL = const.CHARACTER_SELECT_FONT_URL
CHARACTER_SELECT_SIZE = const.CHARACTER_SELECT_SIZE
SYSFONT = const.SYSFONT
SYSFONT_SIZE = const.SYSFONT_SIZE
BLACK_COLOR = const.BLACK_COLOR
WHITE_COLOR = const.WHITE_COLOR


def CharacterChoice(bird1, bird2, bird3, arrow, logo, mscreen, background, CharSelContent, GuideContent):
    bird1.__init__()
    bird2.__init__()
    bird3.__init__()
    DEFAULT_POS = DEFAULT_BIRD_POS
    up = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if DEFAULT_POS == 300:
                        return 2
                    elif DEFAULT_POS == 420:
                        return 1
                    else:
                        return
                if event.key == K_UP:
                    DEFAULT_POS -= 60
                    st.Choice_sound.play()
                    if DEFAULT_POS < 300:
                        DEFAULT_POS = 300
                if event.key == K_DOWN:
                    DEFAULT_POS += 60
                    st.Choice_sound.play()
                    if DEFAULT_POS > 420:
                        DEFAULT_POS = 420

        background.draw()
        arrow.draw()
        logo.draw()
        bird1.setY(DEFAULT_POS - 60)
        bird1.draw()
        bird2.setY(DEFAULT_POS)
        bird2.draw()
        bird3.setY(DEFAULT_POS + 60)
        bird3.draw()
        CharSelContent.draw()
        GuideContent.draw()
        mscreen.draw(0)
        pygame.display.update()
        fpsClock.tick(FPS)

