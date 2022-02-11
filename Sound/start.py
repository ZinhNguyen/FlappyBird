import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
flap_sound = pygame.mixer.Sound('Sources/sounds/swing.wav')
hit_sound = pygame.mixer.Sound('Sources/sounds/hit.wav')
point_sound = pygame.mixer.Sound('Sources/sounds/point.wav')
background_sound = pygame.mixer.Sound('Sources/sounds/devastates.mp3')
