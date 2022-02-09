import pygame, sys
from pygame.locals import *
from Image import screen as sc
from Image import background as bg
from Image import bird as b
from Image import column as co
from Function import checkGameOver as go
from Sound import start as st
from Function import birdAnimation as ba



BG = bg.BACKGROUND
SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
FPS = sc.FPS
fpsClock = sc.fpsClock
SPEEDFLY = b.SPEEDFLY
SCREEN_SPEED = co.COLUMNSPEED


def Start(bird, columns, score):
    bird.__init__()
    bird.speed = SPEEDFLY
    columns.__init__()
    score.__init__()
    M_SCREEN_X_POS = 0
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
                b.BIRD = ba.bird_animation()
        if go.isGameOver(bird, columns) == True:
            st.die_sound.play()
            return

        SCREEN.blit(BG, (0, 0))
        columns.draw()
        columns.update()

        bird.draw()
        bird.update(mouseClick)

        score.draw()
        score.update(bird, columns)
        M_SCREEN_X_POS -= SCREEN_SPEED
        if M_SCREEN_X_POS <= -WINDOWWIDTH:
            M_SCREEN_X_POS = 0
        bg.draw_screen(M_SCREEN_X_POS)
        pygame.display.update()
        fpsClock.tick(FPS)
