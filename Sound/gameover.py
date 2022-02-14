import pygame
from Utils import constant as const

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
die_sound = pygame.mixer.Sound(const.DIE_SOUND_URL)
