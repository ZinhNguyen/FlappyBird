import pygame
from Utils import constant as const

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
Choice_sound = pygame.mixer.Sound(const.CHOICE_SOUND_URL)
