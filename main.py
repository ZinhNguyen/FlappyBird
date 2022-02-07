# Import library
import pygame
from Image import bird as b
from Image import column as cl
from Level import loading as lo
from Level import start as st
from Level import gameover as go
from Function import calculateScore as cs

pygame.init()


def main():
    bird = b.Bird()
    columns = cl.Columns()
    score = cs.Score()
    record = 0
    while True:
        lo.Loading(bird)
        st.Start(bird, columns, score)
        if score.getScore() > record:
            record = score.getScore()
            print(record)
        go.Over(bird, columns, score, record)

if __name__ == '__main__':
    main()
