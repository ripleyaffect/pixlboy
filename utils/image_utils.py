import pygame

from game_types import Pixels


class ImageUtils:
    base_path = '/home/ripley/Projects/pixlboy/images/'

    @classmethod
    def set_base_path(cls, new_base_path):
        cls.base_path = new_base_path

    @classmethod
    def get_pixels(cls, image_name):
        img = pygame.image.load(f'{cls.base_path}{image_name}.png')
        return cls.to_pixels(img)

    @classmethod
    def to_pixels(cls, img, size: int = 16) -> Pixels:
        max_y = size - 1
        return [
            [img.get_at((x, max_y - y))[:3] for x in range(size)]
            for y in range(size)
        ]
