import sys

import pygame

import Source.constants as constants
from Source.sprites import Sprite


class Game:
    def __init__(self):
        self.__screen__ = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__clock__ = pygame.time.Clock()

        self.player = Sprite((400, 500), (100, 100), constants.PLAYER_IMAGE)

        pygame.display.set_caption(constants.CAPTION)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.rotate()
            self.player.move(pygame.key.get_pressed())

            self.__screen__.fill((255, 255, 255))
            self.player.draw(self.__screen__)

            pygame.display.update()
            self.__clock__.tick(60)
