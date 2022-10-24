import pygame

from game_types import Pixels, Color


class Display:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_pixels(self, pixels: Pixels):
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x, y, pixels[y][x])

    def set_pixel(self, x: int, y: int, color: Color):
        NotImplementedError("set_pixel not implemented")

    def fill(self, color: Color):
        NotImplementedError("fill not implemented")

    def render(self):
        NotImplementedError("render not implemented")
