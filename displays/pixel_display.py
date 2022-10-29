import pygame

from displays.display import Display
from colors import Colors
from game_types import Color


class PixelDisplay(Display):
    def __init__(self, width: int, height: int):
        import board
        import neopixel

        super(PixelDisplay, self).__init__(width, height)

        # TODO Use NeoPixel lib
        self.leds = neopixel.NeoPixel(
            board.D18,
            width * height,
            brightness=0.01,
            pixel_order=neopixel.GRB,
            auto_write=False,
        )

        # Store the position map for later lookup
        self.pixel_position_map = self.get_pixel_position_map()

        # Need this for event system to work correctly
        self.screen = pygame.display.set_mode((1, 1))

    def get_pixel_position_map(self):
        """Map screen position pixels to neopixel positions"""
        pixel_position_map = []

        for y in range(self.height):
            pixel_position_map.append([])
            for x in range(self.width):
                neo_x = (self.width - 1) - x if y % 2 != 0 else x
                pixel_position_map[y].append(y * self.width + neo_x)

        return pixel_position_map

    def set_pixel(self, x: int, y: int, color: Color):
        neo_pos = self.pixel_position_map[y][x]

        # Only update the pixel if it's different from current color
        if self.leds[neo_pos] != color:
            self.leds[neo_pos] = color

    def fill(self, color: Color):
        self.leds.fill(color)

    def render(self):
        self.leds.show()
        pygame.display.flip()
