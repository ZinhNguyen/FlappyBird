import pygame, sys
from pygame.locals import *
from Utils import function as fn
from Utils import constant as const
from Utils import variables as var
from Sound import start as st
from Sound import gameover as so

def Start(bird, columns, score, mscreen, background):
    """
    This function will display playing Screen

    Parameters:
        bird (object): The bird will be displayed in Screen
        columns (object): The Column will be displayed
        score (object): The Score will be displayed
        mscreen (object): The moving screen at the bottom will be displayed
        background (object): The background will be displayed

    Returns:
        Return score for next Screen
    """
    bird.__init__()
    bird.setSpeed(const.SPEEDFLY)
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
            if event.type == var.BIRD_FLAP:
                if var.BIRD_INDEX < 2:
                    var.BIRD_INDEX +=1
                else:
                    var.BIRD_INDEX =0
                var.BIRD = var.BIRD_LIST[var.BIRD_INDEX]
                var.BROWNBIRD = var.BROWNBIRD_LIST[var.BIRD_INDEX]
                var.BLUEBIRD = var.BLUEBIRD_LIST[var.BIRD_INDEX]
        if fn.isGameOver(bird, columns) == True:
            so.die_sound.play()
            st.background_sound.stop()
            var.BIRD = var.BIRD_LIST[1]
            var.BROWNBIRD = var.BROWNBIRD_LIST[1]
            var.BLUEBIRD = var.BLUEBIRD_LIST[1]
            return
        background.draw()
        columns.draw()
        columns.update()
        bird.draw()
        bird.update(mouseClick)
        score.draw()
        score.update(bird, columns)
        M_SCREEN_X_POS -= const.COLUMNSPEED
        if M_SCREEN_X_POS <= -const.WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        mscreen.draw(M_SCREEN_X_POS)
        pygame.display.update()
        var.fpsClock.tick(const.FPS)
