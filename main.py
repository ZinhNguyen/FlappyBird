# Import library
import pygame
from Image import bird as b
from Image import column as cl
from Level import loading as lo
from Level import start as st
from Level import gameover as go
from Level import characterChoice as cc
from Function import calculateScore as cs

pygame.init()


def main():
    blueBird = b.BlueBird()
    brownBird = b.BrownBird()
    defaultBird = b.Bird()
    bird = defaultBird
    columns = cl.Columns()
    score = cs.Score()
    record = 0
    while True:
        temp = cc.CharacterChoice(blueBird, defaultBird, brownBird)
        if temp == 1:
            bird = blueBird
        elif temp == 2:
            bird = brownBird
        else:
            bird = defaultBird
        lo.Loading(bird)
        st.Start(bird, columns, score)
        if score.getScore() > record:
            record = score.getScore()
        go.Over(bird, columns, score, record)

if __name__ == '__main__':
    main()
