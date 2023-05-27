import math

import pygame

from Source.constants import SCREEN_SIZE


class Sprite:
    def __init__(self, start_position: tuple[int, int], size: tuple[int, int], image: pygame.Surface):
        self.__rect__ = pygame.rect.Rect(*start_position, *size)
        self.__start_position__ = start_position
        self.__size__ = size
        self.__start__image__ = image
        self.__image__ = image
        self.__angle__ = 0

    def get_coordinates(self) -> tuple[int, int]:
        return self.__rect__.x, self.__rect__.y

    def change_coordinates(self, x: int = 0, y: int = 0) -> None:
        self.__rect__.x += x
        self.__rect__.y += y

    def set_coordinates(self, x: int = 0, y: int = 0) -> None:
        self.__rect__.x = x
        self.__rect__.y = y

    def get_rect(self) -> pygame.rect.Rect:
        return self.__rect__
    
    def move(self, key_pressed: pygame.key.ScancodeWrapper) -> None:
        player_x, player_y = self.get_coordinates()
        
        if key_pressed[pygame.K_a] and player_x > 0:
            self.change_coordinates(-5)
        if key_pressed[pygame.K_d] and player_x < SCREEN_SIZE[0] - self.__rect__.width:
            self.change_coordinates(5)

        if key_pressed[pygame.K_w] and player_y > 0:
            self.change_coordinates(y=-5)
        if key_pressed[pygame.K_s] and player_y < SCREEN_SIZE[1] - self.__rect__.height:
            self.change_coordinates(y=5)

    def rotate(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.__rect__.center

        self.__angle__ = -math.atan2((mouse_y - player_y), (mouse_x - player_x)) * 180 / math.pi

        image_rect = self.__image__.get_rect()

        self.__image__ = pygame.transform.rotate(self.__start__image__, self.__angle__)
        rotated_image_rect = self.__image__.get_rect(center=image_rect.center)

        self.change_coordinates(*rotated_image_rect.topleft)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__image__, self.get_coordinates())
