import pygame, sys
from pygame.locals import *
from Image import screen as sc
from Image import background as bg
from Image import column as co
from Sound import characterChoice as st
from Function import flyLoading as fl
from Image import bird as b

BG = bg.BACKGROUND
SCREEN = sc.SCREEN
ARROW = bg.ARROW
LOGO = bg.LOGO
LOGO_WIDTH = bg.LOGO_WIDTH
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT
FPS = sc.FPS
fpsClock = sc.fpsClock
SCREEN_SPEED = co.COLUMNSPEED


def CharacterChoice(bird1, bird2, bird3):
    bird1.__init__()
    bird2.__init__()
    bird3.__init__()
    M_SCREEN_X_POS = 0
    DEFAULT_POS = 360
    font = pygame.font.Font('Sources/fonts/PhoenixGaming.ttf', 40)
    headingSuface = font.render('CHARACTER SELECT', True, (255, 255, 255))
    headingSize = headingSuface.get_size()


    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "Space" to choose', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
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
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(ARROW, (170, 355))
        SCREEN.blit(LOGO, ((WINDOWWIDTH-LOGO_WIDTH)/2, 100))
        # make bird fly on loading
        # bird1.y, up = fl.flying(up, bird1.y, 5)
        bird1.setY(DEFAULT_POS - 60 )
        bird1.draw()
        bird2.setY(DEFAULT_POS)
        bird2.draw()
        bird3.setY(DEFAULT_POS + 60)
        bird3.draw()
        SCREEN.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) /2), 200))
        SCREEN.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0] ) /2), 530))
        bg.draw_screen(0)
        # M_SCREEN_X_POS -= SCREEN_SPEED
        # if M_SCREEN_X_POS <= -WINDOWWIDTH:
        #     M_SCREEN_X_POS = 0
        bg.draw_screen(M_SCREEN_X_POS)

        pygame.display.update()
        fpsClock.tick(FPS)

