import pygame
import os


CAPTION = "Андрух Максим"
SCREEN_SIZE = (1280, 720)

PLAYER_SIZE = (100, 100)
PLAYER_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "player.png")), PLAYER_SIZE
)
