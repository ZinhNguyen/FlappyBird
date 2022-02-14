import pygame
from Utils import function as fn
from Utils import constant as const
from Utils import variables as var
from Sound import start as st

class Score():
    """This is Score Class to display Score"""
    def __init__(self):
        """initial contractor Score class"""
        self._score = 0
        self._addScore = True
    def getScore(self):
        """This function will return score"""
        return self._score
    def getStateScore(self):
        """This function will return status of flag addScore"""
        return self._addScore
    def draw(self):
        """This function will draw Score into Background"""
        font = pygame.font.Font(const.SCORE_FONT_URL, const.SCORE_FONT_SIZE_PLAYING)
        scoreSuface = font.render(str(self._score), True, const.WHITE_COLOR, True)
        textSize = scoreSuface.get_size()
        var.SCREEN.blit(scoreSuface, (int((const.WINDOWWIDTH - textSize[0]) / 2), const.SCORE_Y_POS_PLAYING))

    def update(self, bird, columns):
        """This function will update Score when bird fly collision with rectangle"""
        collision = False
        for i in range(3):
            rectColumn = [columns.ls[i][0] + columns.getWidth(), columns.ls[i][1], 1, columns.getBlank()]
            rectBird = [bird.getX(), bird.getY(), bird.getWidth(), bird.getHeight()]
            if fn.rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self._addScore == True:
                self._score += 1
                st.point_sound.play()
            self._addScore = False
        else:
            self._addScore = True
