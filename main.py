# Import library
import pygame
from Image import bird as b, score as sc
from Image import column as cl, arrow as ar, logo as lg, mcreen as ms, background as bg, content as ct
from Level import loading as lo, start as st, gameover as go, characterChoice as cc

# Set init for pygame
pygame.init()
# Set title
pygame.display.set_caption('FLAPPY BIRD')

def main():
    """This is main function for game"""
    record = 0
    blueBird = b.BlueBird()
    brownBird = b.BrownBird()
    defaultBird = b.Bird()
    background = bg.Background()
    columns = cl.Columns()
    score = sc.Score()
    arrow = ar.Arrow()
    logo = lg.Logo()
    mscreen = ms.Mscreen()
    while True:
        temp = cc.CharacterChoice(blueBird, defaultBird, brownBird, arrow, logo, mscreen, background)
        if temp == 1:
            bird = blueBird
        elif temp == 2:
            bird = brownBird
        else:
            bird = defaultBird
        lo.Loading(bird, mscreen, background)
        st.Start(bird, columns, score, mscreen, background)
        if score.getScore() > record:
            record = score.getScore()
        go.Gameover(bird, columns, score, record, mscreen, background)

if __name__ == '__main__':
    main()
