import random
from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

class Columns():
    """This is Column class"""
    def __init__(self):
        """initial contractor for Column class"""
        self._width = const.COLUMNWIDTH
        self._height = const.COLUMNHEIGHT
        self._blank = const.BLANK
        self._distance = const.DISTANCE
        self._speed = const.COLUMNSPEED
        self._surface = fn.load_scale_image(const.COLUMN_URL, self._width, self._height)
        self.ls = []
        for i in range(3):
            x = const.DELAY_PLAYING + i*self._distance
            y = random.randrange(40, const.WINDOWHEIGHT - self._blank - 200, 20)
            self.ls.append([x, y])
    def getHeight(self):
        """This function will get the height of column"""
        return self._height
    def getWidth(self):
        """This function will get the width of column"""
        return self._width
    def getBlank(self):
        """This function will get the blank between upper and lower column"""
        return self._blank
    def draw(self):
        """This function will draw upper column and lower column"""
        for i in range(3):
            var.SCREEN.blit(self._surface, (self.ls[i][0], self.ls[i][1] - self._height))
            var.SCREEN.blit(self._surface, (self.ls[i][0], self.ls[i][1] + self._blank))
    def update(self):
        """This function will delete and update new column"""
        for i in range(3):
            self.ls[i][0] -= self._speed
        if self.ls[0][0] < -self._width:
            self.ls.pop(0)
            x = self.ls[1][0] + self._distance
            y = random.randrange(40, const.WINDOWHEIGHT - self._blank - 200, 10)
            self.ls.append([x, y])
