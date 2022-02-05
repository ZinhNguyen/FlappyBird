# Include library
import pygame, sys
from pygame.locals import *

# Set Variable for Screen
WINDOWWIDTH = 350
WINDOWHEIGHT = 540

# Set colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# init pygame
pygame.init()

# Set FPS
FPS = 60
fpsClock = pygame.time.Clock()

# Load Background
BG = pygame.image.load('full_background.png')
BG = pygame.transform.scale(BG, (1000, 500))


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('SCROLLING BACKGROUND')

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = BG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
    def update(self, player):
        x_camera = player.x - (WINDOWWIDTH/2 - player.width/2)
        if x_camera < 0:
            x_camera = 0
        if x_camera + WINDOWWIDTH > self.width:
            x_camera = self.width - WINDOWWIDTH
        self.x = -x_camera
class Player():
    def __init__(self):
        self.width = 200
        self.height = 70
        self.x = 0
        self.y = 400
        self.surface = pygame.image.load('car.png')
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
        # self.surface = pygame.Surface((self.width, self.height))
        # self.surface.fill(RED)
        self.speed = 5

    def draw(self, bg):
        DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
    def update(self, bg, left, right):
        if left == True:
            self.x -= self.speed
        if right == True:
            self.x += self.speed
        if self.x < 0:
            self.x = 0
        if self.x + self.width > bg.width:
            self.x = bg.width - self.width
def main():
    bg = Background()
    player = Player()
    left = False
    right = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
        bg.draw()
        bg.update(player)
        player.draw(bg)

        player.update(bg, left, right)


        pygame.display.update()
        fpsClock.tick(FPS)
if __name__ == '__main__':
    main()