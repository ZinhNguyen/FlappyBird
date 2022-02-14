import pygame
from Utils import constant as const

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
flap_sound = pygame.mixer.Sound(const.FLAP_SOUND_URL)
hit_sound = pygame.mixer.Sound(const.HIT_SOUND_URL)
point_sound = pygame.mixer.Sound(const.POINT_SOUND_URL)
background_sound = pygame.mixer.Sound(const.BACKGROUND_SOUND_URL)
