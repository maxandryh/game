import pygame


class Sprite:
    def __init__(self, start_position: tuple[int, int], size: tuple[int, int], image: pygame.Surface):
        self.__rect__ = pygame.rect.Rect(*start_position, *size)
        self.__start_position__ = start_position
        self.__size__ = size
        self.__image__ = image

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
    