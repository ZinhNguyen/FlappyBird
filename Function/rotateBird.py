import pygame
from Image import bird as b

def rotate_bird(bird, angle):
   # new_bird = pygame.transform.rotozoom(bird,-b.SPEEDFLY*4, 1)
    new_bird = pygame.transform.rotate(bird, angle)
    return new_bird
