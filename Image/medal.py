import pygame.image
from Utils import constant as const
from Utils import variables as var

SCREEN = var.SCREEN
MEDAL_WIDTH = const.MEDAL_WIDTH
MEDAL_HEIGHT = const.MEDAL_HEIGHT
MEDAL_X_POS = const.MEDAL_X_POS
MEDAL_Y_POS = const.MEDAL_Y_POS

BRONZE_MEDAL_URL = const.BRONZE_MEDAL_URL
SILVER_MEDAL_URL = const.SILVER_MEDAL_URL
GOLD_MEDAL_URL = const.GOLD_MEDAL_URL
DIAMOND_MEDAL_URL = const.DIAMOND_MEDAL_URL

# Load bronze medal images
BRONZE_MEDAL = pygame.image.load(BRONZE_MEDAL_URL)
BRONZE_MEDAL = pygame.transform.scale(BRONZE_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load silver medal images
SILVER_MEDAL = pygame.image.load(SILVER_MEDAL_URL)
SILVER_MEDAL = pygame.transform.scale(SILVER_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load gold medal images
GOLD_MEDAL = pygame.image.load(GOLD_MEDAL_URL)
GOLD_MEDAL = pygame.transform.scale(GOLD_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load diamond medal images
DIAMOND_MEDAL = pygame.image.load(DIAMOND_MEDAL_URL)
DIAMOND_MEDAL = pygame.transform.scale(DIAMOND_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))


class medal():
    def __init__(self):
        self.x = MEDAL_X_POS
        self.y = MEDAL_Y_POS
        self.surface = GOLD_MEDAL

    def draw(self):
        SCREEN.blit(self.surface, (self.x, self.y))

class NoMedal(medal):
    def __init__(self):
        medal.__init__(self)
    def draw(self):
        pygame.draw.circle(SCREEN, (215, 206, 137), (self.x + MEDAL_WIDTH/2, self.y + MEDAL_WIDTH/2), MEDAL_WIDTH/2)
        pygame.draw.circle(SCREEN, (225, 216, 145), (self.x + MEDAL_WIDTH/2, self.y + MEDAL_WIDTH/2), MEDAL_WIDTH/2, 2)

class BronzeMedal(medal):
    def __init__(self):
        medal.__init__(self)
        self.surface = BRONZE_MEDAL

class SilverMedal(medal):
    def __init__(self):
        medal.__init__(self)
        self.surface = SILVER_MEDAL

class GoldMedal(medal):
    def __init__(self):
        medal.__init__(self)
        self.surface = GOLD_MEDAL

class DiamondMedal(medal):
    def __init__(self):
        medal.__init__(self)
        self.surface = DIAMOND_MEDAL