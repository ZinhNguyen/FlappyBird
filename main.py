# Import library
import pygame
from Image import bird as b, score as cs
from Image import column as cl
from Level import loading as lo
from Level import start as st
from Level import gameover as go
from Level import characterChoice as cc
from Image import arrow as ar
from Image import logo as lg
from Image import mcreen as ms
from Image import background as bg
from Image import content as ct
from Utils import constant as const
CHARACTER_SELECT_FONT_URL = const.CHARACTER_SELECT_FONT_URL
CHARACTER_SELECT_SIZE = const.CHARACTER_SELECT_SIZE
GUIDEFONT_URL = const.GUIDEFONT_URL
GUIDEFONT_SIZE = const.GUIDEFONT_SIZE
WHITE_COLOR = const.WHITE_COLOR
BLACK_COLOR = const.BLACK_COLOR

pygame.init()


def main():
    record = 0
    blueBird = b.BlueBird()
    brownBird = b.BrownBird()
    defaultBird = b.Bird()
    background = bg.Background()
    columns = cl.Columns()
    score = cs.Score()
    arrow = ar.Arrow()
    logo = lg.Logo()
    mscreen = ms.Mscreen()
    CharSelContent = ct.Content(CHARACTER_SELECT_FONT_URL, CHARACTER_SELECT_SIZE, 'CHARACTER SELECT', WHITE_COLOR, 200)
    GuideContent = ct.Content(GUIDEFONT_URL, GUIDEFONT_SIZE, 'Press "Space" to choose', BLACK_COLOR, 530)
    GuideLoadingContent = ct.Content(GUIDEFONT_URL, GUIDEFONT_SIZE, 'Click or use "Space" to start', BLACK_COLOR, 530)

    while True:
        temp = cc.CharacterChoice(blueBird, defaultBird, brownBird, arrow, logo, mscreen, background, CharSelContent, GuideContent)
        if temp == 1:
            bird = blueBird
        elif temp == 2:
            bird = brownBird
        else:
            bird = defaultBird
        lo.Loading(bird, mscreen, background, GuideLoadingContent)
        st.Start(bird, columns, score, mscreen, background)
        if score.getScore() > record:
            record = score.getScore()
        go.Over(bird, columns, score, record, mscreen, background)

if __name__ == '__main__':
    main()
