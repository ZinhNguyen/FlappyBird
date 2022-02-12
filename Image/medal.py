import pygame.image

from Image import screen as sc

SCREEN = sc.SCREEN
MEDAL_WIDTH = 70
MEDAL_HEIGHT = 70

MEDAL_X_POS = 190
MEDAL_Y_POS = 280

# Load bronze medal images
BRONZE_MEDAL = pygame.image.load('Sources/images/bronze.png')
BRONZE_MEDAL = pygame.transform.scale(BRONZE_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load silver medal images
SILVER_MEDAL = pygame.image.load('Sources/images/silver.png')
SILVER_MEDAL = pygame.transform.scale(SILVER_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load gold medal images
GOLD_MEDAL = pygame.image.load('Sources/images/gold.png')
GOLD_MEDAL = pygame.transform.scale(GOLD_MEDAL, (MEDAL_WIDTH, MEDAL_HEIGHT))

# Load diamond medal images
DIAMOND_MEDAL = pygame.image.load('Sources/images/diamond.png')
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