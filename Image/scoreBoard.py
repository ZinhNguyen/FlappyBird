import pygame
from Utils import constant as const
from Utils import variables as var

SCREEN = var.SCREEN
WHD_2 = const.WHD_2
WT = 260
HT = 160
p1 = (WHD_2 - WT / 2, WHD_2 - HT / 2 + 10)
p2 = (WHD_2 - WT / 2 + 3, WHD_2 - HT / 2 + 3)
p3 = (WHD_2 - WT / 2 + 10, WHD_2 - HT / 2)
p4 = (WHD_2 + WT / 2 - 10, WHD_2 - HT / 2)
p5 = (WHD_2 + WT / 2 - 3, WHD_2 - HT / 2 + 3)
p6 = (WHD_2 + WT / 2, WHD_2 - HT / 2 + 10)
p7 = (WHD_2 + WT / 2, WHD_2 + HT / 2 - 10)
p8 = (WHD_2 + WT / 2 - 3, WHD_2 + HT / 2 - 3)
p9 = (WHD_2 + WT / 2 - 10, WHD_2 + HT / 2)
p10 = (WHD_2 - WT / 2 + 10, WHD_2 + HT / 2)
p11 = (WHD_2 - WT / 2 + 3, WHD_2 + HT / 2 - 3)
p12 = (WHD_2 - WT / 2, WHD_2 + HT / 2 - 10)
table = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)

class ScoreBoard():
    def __init__(self):
        self. color = (223, 214, 144)
        self.borderColor = (0, 0, 0)
        self.table = table
    def draw(self):
        pygame.draw.polygon(SCREEN, (223, 214, 144), self.table)
        pygame.draw.polygon(SCREEN, (0, 0, 0), self.table, 3)