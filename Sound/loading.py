import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
battle_sound = pygame.mixer.Sound('Sources/sounds/Journey.mp3')
