import pygame
from Utils import constant as const
from Utils import variables as var

class ScoreBoard():
    """This is ScoreBoard class to display table created by polygon"""
    def __init__(self):
        """initial contractor ScoreBoard class"""
        self._color = (223, 214, 144)
        self._borderColor = (0, 0, 0)
        self._borderWidth = 3
        self._table = const.table
    def draw(self):
        """This function will draw table with border"""
        pygame.draw.polygon(var.SCREEN, self._color, self._table)
        pygame.draw.polygon(var.SCREEN, self._borderColor, self._table, self._borderWidth)