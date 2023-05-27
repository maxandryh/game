import sys

import pygame
import Source.constants as constants


class Game:
    def __init__(self):
        self.__screen__ = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__clock__ = pygame.time.Clock()

        pygame.display.set_caption(constants.CAPTION)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
