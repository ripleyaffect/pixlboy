import pygame

from displays.display import Display
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
            pixel_order=neopixel.GRB
        )

        # Store the position map for later lookup
        self.pixel_position_map = self.get_pixel_position_map()

        # Need this for event system to work correctly?
        self.screen = pygame.display.set_mode((0, 0))

    def get_pixel_position_map(self):
        """Map screen position pixels to neopixel positions"""
        pixel_position_map = []

        for x in range(self.width):
            pixel_position_map.append([])
            for y in range(self.height):
                neo_x = x if y % 2 == 1 else (self.width - 1) - x
                neo_y = (self.height - 1) - y
                pixel_position_map[x].append(neo_y * self.width + neo_x)

        return pixel_position_map

    def set_pixel(self, x: int, y: int, color: Color):
        neo_pos = self.pixel_position_map[x][y]

        # Only update the pixel if it's different from current color
        if self.leds[neo_pos] != color:
            self.leds[neo_pos] = color

    def fill(self, color: Color):
        self.screen.fill(color)

    def render(self):
        # Needed for event system to work correctly?
        pygame.display.flip()
