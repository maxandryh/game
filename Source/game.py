import sys

import pygame

import Source.constants as constants
from Source.sprites import Sprite


class Game:
    def __init__(self):
        self.__screen__ = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__clock__ = pygame.time.Clock()

        self.player = Sprite((100, 100), (100, 100), None)

        pygame.display.set_caption(constants.CAPTION)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.rotate(10)

            pygame.draw.rect(self.__screen__, (255, 255, 255), self.player.get_rect())

            pygame.display.update()
            self.__clock__.tick(60)