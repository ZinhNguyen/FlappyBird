import pygame
from Utils import function as fn
from Utils import constant as const
from Utils import variables as var
from Sound import start as st

SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT

class Score():
    def __init__(self):
        self.score = 0
        self.addScore = True
    def getScore(self):
        return self.score
    def draw(self):
        font = pygame.font.Font('Sources/fonts/04B_19.ttf', 50)
        scoreSuface = font.render(str(self.score), True, (255, 255, 255), True)
        textSize = scoreSuface.get_size()
        SCREEN.blit(scoreSuface, (int((WINDOWWIDTH - textSize[0]) / 2), 100))

    def update(self, bird, columns):
        collision = False
        for i in range(3):
            rectColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            rectBird = [bird.getX(), bird.getY(), bird.getWidth(), bird.getHeight()]
            if fn.rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += 1
                st.point_sound.play()
            self.addScore = False
        else:
            self.addScore = True
