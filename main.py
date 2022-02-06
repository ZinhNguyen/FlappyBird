# Import library
import random

import pygame, sys
from pygame.locals import *

# Create function for forever running
def draw_screen():
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS, 600))
    SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS + WINDOWWIDTH, 600))

# Set variable for Screen
WINDOWWIDTH = 432
WINDOWHEIGHT = 768


# Init pygame
pygame.init()

# Set FPS
FPS = 60
fpsClock = pygame.time.Clock()

# Load Background
BG = pygame.image.load('images/background1.png')
BG = pygame.transform.scale(BG, (WINDOWWIDTH, WINDOWHEIGHT))

# Add moving screen for Background
M_SCREEN = pygame.image.load('images/floor.png')
M_SCREEN = pygame.transform.scale2x(M_SCREEN)
M_SCREEN_X_POS = 0

# Display Screen
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


# Set constants variable for Bird
BIRDWIDTH = 60
BIRDHEIGHT = 45
G = 0.5
SPEEDFLY = -8
# Load bird
BIRD = pygame.image.load('images/bird1.png')
BIRD = pygame.transform.scale(BIRD, (BIRDWIDTH, BIRDHEIGHT))

# colission between bird and columns
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

# Check GameOver
def isGameOver(bird, columns):
    for i in range(3):
        rectBird = [bird.x, bird.y, bird.width, bird.height]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT:
        return True
    return False

class Bird():
    def __init__(self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/2
        self.y = (WINDOWHEIGHT - self.height)/2
        self.speed = 0
        self.surface = BIRD

    def draw(self):
        SCREEN.blit(self.surface, (int(self.x), int(self.y)))

    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G
        if mouseClick == True:
            self.speed = SPEEDFLY

# Set constants variable for Column
COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 2
COLUMNIMG = pygame.image.load('images/column.png')

class Columns():
    def __init__(self):
        self.width = COLUMNWIDTH
        self.height = COLUMNHEIGHT
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = COLUMNSPEED
        self.surface = COLUMNIMG
        self.ls = []
        for i in range(3):
            x = WINDOWWIDTH + i*self.distance
            y = random.randrange(60, WINDOWHEIGHT - self.blank - 60, 20)
            self.ls.append([x, y])

    def draw(self):
        for i in range(3):
            SCREEN.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            SCREEN.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))

    def update(self):
        for i in range(3):
            self.ls[i][0] -= self.speed
        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = random.randrange(60, WINDOWHEIGHT - self.blank - 60, 10)
            self.ls.append([x, y])


class Score():
    def __init__(self):
        self.score = 0
        self.addScore = True

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
            if rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += 1
            self.addScore = False
        else:
            self.addScore = True

bird = Bird()
columns = Columns()
score = Score()
while True:
    mouseClick = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouseClick = True
    if isGameOver(bird, columns) == True:
        pygame.quit()
        sys.exit()
    SCREEN.blit(BG, (0, 0))
    columns.draw()
    columns.update()

    bird.draw()
    bird.update(mouseClick)

    score.draw()
    score.update(bird, columns)
    M_SCREEN_X_POS -= 3
    if M_SCREEN_X_POS <= -WINDOWWIDTH:
        M_SCREEN_X_POS = 0
    draw_screen()
    pygame.display.update()
    fpsClock.tick(FPS)
