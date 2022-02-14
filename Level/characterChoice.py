import pygame, sys
from pygame.locals import *
from Sound import characterChoice as st
from Image import content as ct
from Utils import constant as const
from Utils import variables as var

def CharacterChoice(bird1, bird2, bird3, arrow, logo, mscreen, background):
    """
    This function will loading Character Selection Screen

    Parameters:
        bird1 (object): The first bird will be displayed
        bird2 (object): The second bird will be displayed
        bird3 (object): The third bird will be displayed
        arrow (object): The Arrow will be displayed
        logo (object): The logo will be displayed
        mscreen (object): The moving screen at the bottom will be displayed
        background (object): The background will be displayed

    Returns:
        Return 1 if DEFAULT_POS == 420:
        Return 2 if DEFAULT_POS == 300:
        Return default if DEFAULT_POS differ with upper
    """
    bird1.__init__()
    bird2.__init__()
    bird3.__init__()
    CharSelContent = ct.Content(const.CHARACTER_SELECT_FONT_URL, const.CHARACTER_SELECT_SIZE, 'CHARACTER SELECT', const.WHITE_COLOR, 200)
    GuideContent = ct.Content(const.GUIDEFONT_URL, const.GUIDEFONT_SIZE, 'Press "Space" to choose', const.BLACK_COLOR, 530)
    DEFAULT_POS = const.DEFAULT_BIRD_POS
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
        var.fpsClock.tick(const.FPS)

