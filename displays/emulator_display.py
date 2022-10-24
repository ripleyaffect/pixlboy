import pygame

from displays.display import Display
from game_types import Color


class EmulatorDisplay(Display):
    def __init__(self, width: int, height: int, scale: int = 30):
        super(EmulatorDisplay, self).__init__(width, height)

        self.scale = scale

        self.screen = pygame.display.set_mode((width * scale, height * scale))

    def set_pixel(self, x: int, y: int, color: Color):
        screen_y = (self.height - 1) - y
        pixel_rect = pygame.Rect(x * self.scale, screen_y * self.scale, self.scale, self.scale)
        self.screen.fill(color, pixel_rect)

    def fill(self, color: Color):
        self.screen.fill(color)

    def render(self):
        pygame.display.flip()
