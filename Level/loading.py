import pygame, sys
from pygame.locals import *
from Image import background as bg
from Image import column as co
from Utils import function as fn
from Sound import loading as st
from Utils import constant as const
from Utils import variables as var

BG = bg.BACKGROUND
SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
FPS = const.FPS
fpsClock = var.fpsClock
SCREEN_SPEED = co.COLUMNSPEED
BIRD_MOVING_RANGE = const.BIRD_MOVING_RANGE

def Loading(bird, mscreen, background, GuideLoadingContent):
    bird.__init__()
    M_SCREEN_X_POS = 0
    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Click or use "Space" to start', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
    up = True
    st.battle_sound.play()
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
        #SCREEN.blit(BG, (0, 0))
        # make bird fly on loading
        bird_y = bird.getY()
        bird_y, up = fn.flying(up, bird_y, BIRD_MOVING_RANGE)
        bird.setY(bird_y)
        bird.draw()
        # SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0] ) /2), 100))
        GuideLoadingContent.draw()
        # SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 500))
        M_SCREEN_X_POS -= SCREEN_SPEED
        if M_SCREEN_X_POS <= -WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        mscreen.draw(M_SCREEN_X_POS)
        #bg.draw_m_screen(M_SCREEN_X_POS)
        pygame.display.update()
        fpsClock.tick(FPS)
