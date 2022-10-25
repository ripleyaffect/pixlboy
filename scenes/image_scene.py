import pygame

from colors import Colors
from game_types import Pixels, Color
from .scene import Scene


class ImageScene(Scene):
    def __init__(
            self,
            display,
            seconds_between_renders: float = 1.0,
            image_name: str = 'test',
    ):
        super(ImageScene, self).__init__(display, seconds_between_renders)

        self.img = pygame.image.load(f'images/{image_name}.png')

        self.display.set_pixels(self.to_pixels(self.img))

    def update(self):
        self.display.set_pixels(self.to_pixels(self.img))

    def to_pixels(self, img) -> Pixels:
        max_y = self.display.height - 1
        return [
            [img.get_at((x, max_y - y))[:3] for x in range(self.display.width)]
            for y in range(self.display.height)
        ]
