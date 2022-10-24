import pygame

from displays import EmulatorDisplay, PixelDisplay
from pixl_boy import PixlBoy

if __name__ == '__main__':
    pygame.init()

    # TODO: switch between displays with a parameter? Allow multiple displays?
    display = EmulatorDisplay(16, 16)

    PixlBoy(display).run()
