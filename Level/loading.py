import pygame, sys
from pygame.locals import *
from Image import content as ct
from Sound import loading as st
from Utils import constant as const
from Utils import variables as var
from Utils import function as fn


def Loading(bird, mscreen, background):
    """
    This function will display Loading Screen

    Parameters:
        bird (object): The bird will be displayed in Screen
        mscreen (object): The moving screen at the bottom will be displayed
        background (object): The background will be displayed
        GuideLoadingContent (object): This GuideContent will be displayed

    Returns:
        no return
    """
    bird.__init__()
    M_SCREEN_X_POS = 0
    up = True
    st.battle_sound.play()
    GuideLoadingContent = ct.Content(const.GUIDEFONT_URL, const.GUIDEFONT_SIZE, 'Click or use "Space" to start', const.BLACK_COLOR, 530)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                st.battle_sound.stop()
                return
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    st.battle_sound.stop()
                    return
        background.draw()
        bird_y = bird.getY()
        bird_y, up = fn.flying(up, bird_y, const.BIRD_MOVING_RANGE)
        bird.setY(bird_y)
        bird.draw()
        GuideLoadingContent.draw()
        M_SCREEN_X_POS -= const.COLUMNSPEED
        if M_SCREEN_X_POS <= -const.WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        mscreen.draw(M_SCREEN_X_POS)
        pygame.display.update()
        var.fpsClock.tick(const.FPS)
