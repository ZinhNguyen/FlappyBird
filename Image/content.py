import pygame
from Utils import variables as var
from Utils import constant as const

class Content():
    """This is Content class to display information in screen"""
    def __init__(self, fontURL, fontSize, content, color, y_pos):
        """initial contractor for Content class"""
        self._fontURL = fontURL
        self._fontSize = fontSize
        self._content = content
        self._color = color
        self._font = pygame.font.Font(self._fontURL, self._fontSize)
        self._surface = self._font.render(content, True, color)
        self._size = self._surface.get_size()
        self._x_pos = int((const.WINDOWWIDTH - self._size[0])/2)
        self._y_pos = y_pos
    def setXplus(self, x_pos):
        """This function will add x_pos for content"""
        self._x_pos += x_pos
    def setXminus(self, x_pos):
        """This function will minus x_pos for content"""
        self._x_pos -= x_pos
    def getX(self):
        """This function will get x_pos for content"""
        return self._x_pos
    def draw(self):
        """This function will draw content into Background"""
        var.SCREEN.blit(self._surface, (self._x_pos, self._y_pos))

class ScoreContent(Content):
    """This is ScoreContent class inherited from Content class to display information Score in Gamve over screen"""
    def __init__(self, fontURL, fontSize, content, color, y_pos):
        Content.__init__(self, fontURL, fontSize, content, color, y_pos)
        self._surface = self._font.render(self._content, True, self._color, True)






