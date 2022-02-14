import pygame.image
from Utils import constant as const
from Utils import variables as var

class medal():
    """This is medal class to display when finished game"""
    def __init__(self):
        """initial contractor for Medal class"""
        self._x = const.MEDAL_X_POS
        self._y = const.MEDAL_Y_POS
        self._width = const.MEDAL_WIDTH
        self._center = self._width/2
        self._surface = var.GOLD_MEDAL

    def draw(self):
        var.SCREEN.blit(self._surface, (self._x, self._y))

class NoMedal(medal):
    """This is noMedal class inherited from medal class to display circle"""
    def __init__(self):
        """initial contractor for NoMedal class"""
        medal.__init__(self)
    def draw(self):
        """This function will draw 1 circle and 1 border circle into Background"""
        pygame.draw.circle(var.SCREEN, (215, 206, 137), (self._x + self._center, self._y + self._center), self._center)
        pygame.draw.circle(var.SCREEN, (225, 216, 145), (self._x + self._center, self._y + self._center), self._center, 2)

class BronzeMedal(medal):
    """This is BronzeMedal class inherited from medal class to display Bronze Medal"""
    def __init__(self):
        """initial contractor BronzeMedal class"""
        medal.__init__(self)
        self._surface = var.BRONZE_MEDAL

class SilverMedal(medal):
    """This is SilverMedal class inherited from medal class to display Silver Medal"""
    def __init__(self):
        """initial contractor SilverMedal class"""
        medal.__init__(self)
        self._surface = var.SILVER_MEDAL

class GoldMedal(medal):
    """This GoldMedal class inherited from medal class to display Gold Medal"""
    def __init__(self):
        """initial contractor GoldMedal class"""
        medal.__init__(self)
        self._surface = var.GOLD_MEDAL

class DiamondMedal(medal):
    """This DiamondMedal class inherited from medal class to display Diamond Medal"""
    def __init__(self):
        """initial contractor DiamondMedal class"""
        medal.__init__(self)
        self._surface = var.DIAMOND_MEDAL