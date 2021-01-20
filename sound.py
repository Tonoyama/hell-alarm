import pygame.mixer

pygame.mixer.init()
sounda = pygame.mixer.Sound("wadaiko.wav")

while True:
    sounda.play()