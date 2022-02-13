import pygame
from Utils import variables as var
from Utils import constant as const

SCREEN = var.SCREEN
CHARACTER_SELECT_FONT_URL = const.CHARACTER_SELECT_FONT_URL
CHARACTER_SELECT_SIZE = const.CHARACTER_SELECT_SIZE
WHITE_COLOR = const.WHITE_COLOR
WINDOWWIDTH = const.WINDOWWIDTH
SYSFONT = const.SYSFONT
SYSFONT_SIZE = const.SYSFONT_SIZE
BLACK_COLOR = const.BLACK_COLOR

class Content():
    def __init__(self, fontURL, fontSize, content, color, y_pos):
        self.fontURL = fontURL
        self.fontSize = fontSize
        self.content = content
        self.color = color
        self.font = pygame.font.Font(fontURL, fontSize)
        self.surface = self.font.render(content, True, color)
        self.size = self.surface.get_size()
        self.x_pos = int((WINDOWWIDTH - self.size[0])/2)
        self.y_pos = y_pos
    def setXplus(self, x_pos):
        self.x_pos += x_pos
    def setXminus(self, x_pos):
        self.x_pos -= x_pos
    def getX(self):
        return self.x_pos
    def draw(self):
        SCREEN.blit(self.surface, (self.x_pos, self.y_pos))






