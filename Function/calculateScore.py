import pygame
from Image import screen as sc
from Function import checkCollision as co
from Sound import start as st

SCREEN = sc.SCREEN
WINDOWWIDTH = sc.WINDOWWIDTH
WINDOWHEIGHT = sc.WINDOWHEIGHT

class Score():
    def __init__(self):
        self.score = 0
        self.addScore = True
    def getScore(self):
        return self.score
    def draw(self):
        font = pygame.font.SysFont('consolas', 40)
        scoreSuface = font.render(str(self.score), True, (0, 0, 0))
        textSize = scoreSuface.get_size()
        SCREEN.blit(scoreSuface, (int((WINDOWWIDTH - textSize[0]) / 2), 100))

    def update(self, bird, columns):
        collision = False
        for i in range(3):
            rectColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            rectBird = [bird.x, bird.y, bird.width, bird.height]
            if co.rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += 1
                st.point_sound.play()
            self.addScore = False
        else:
            self.addScore = True