import pygame, sys
from pygame.locals import *
from Image import background as bg
from Image import bird as b
from Utils import function as fn
from Sound import start as st
from Sound import gameover as so
from Utils import constant as const
from Utils import variables as var


BG = bg.BACKGROUND
SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
FPS = const.FPS
fpsClock = var.fpsClock
SPEEDFLY = const.SPEEDFLY
SCREEN_SPEED = const.COLUMNSPEED


def Start(bird, columns, score, mscreen, background):
    bird.__init__()
    bird.setSpeed(SPEEDFLY)
    columns.__init__()
    score.__init__()
    M_SCREEN_X_POS = 0
    st.background_sound.play()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
                st.flap_sound.play()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    mouseClick = True
                    st.flap_sound.play()
            if event.type == b.BIRD_FLAP:
                if b.BIRD_INDEX < 2:
                    b.BIRD_INDEX +=1
                else:
                    b.BIRD_INDEX =0
                b.BIRD = b.BIRD_LIST[b.BIRD_INDEX]
                b.BROWNBIRD = b.BROWNBIRD_LIST[b.BIRD_INDEX]
                b.BLUEBIRD = b.BLUEBIRD_LIST[b.BIRD_INDEX]
                #b.BIRD = ba.bird_animation()
        if fn.isGameOver(bird, columns) == True:
            so.die_sound.play()
            st.background_sound.stop()
            b.BIRD = b.BIRD_LIST[1]
            b.BROWNBIRD = b.BROWNBIRD_LIST[1]
            b.BLUEBIRD = b.BLUEBIRD_LIST[1]
            return
        background.draw()
        columns.draw()
        columns.update()

        bird.draw()
        bird.update(mouseClick)

        score.draw()
        score.update(bird, columns)
        M_SCREEN_X_POS -= SCREEN_SPEED
        if M_SCREEN_X_POS <= -WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        mscreen.draw(M_SCREEN_X_POS)
        pygame.display.update()
        fpsClock.tick(FPS)
