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
FAR_BG = pygame.image.load('far-background.png')
FAR_BG = pygame.transform.scale(FAR_BG, (960, 540))

NEAR_BG = pygame.image.load('near-background.png')
NEAR_BG = pygame.transform.scale(NEAR_BG, (960, 540))

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('SCROLLING BACKGROUND')

class Background():
    def __init__(self, img, speed):
        self.x = 0
        self.y = 0
        self.speed = speed
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x + self.width), int(self.y)))
    def update(self):
        self.x -=self.speed
        if self.x < -self.width:
            self.x +=self.width
def main():
    far_bg = Background(FAR_BG, 0.5)
    near_bg = Background(NEAR_BG, 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        far_bg.draw()
        far_bg.update()

        near_bg.draw()
        near_bg.update()
        pygame.display.update()
        fpsClock.tick(FPS)
if __name__ == '__main__':
    main()