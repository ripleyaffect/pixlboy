import argparse
import pygame

from displays import EmulatorDisplay, PixelDisplay
from inputs import Keyboard, Gamepad
from pixl_boy import PixlBoy
from utils import ImageUtils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--display')

    args = parser.parse_args()
    print(args)
    use_emulator = args.display == 'emulator'

    screen_size = (16, 16)
    use_gamepad = not use_emulator

    if use_emulator:
        ImageUtils.set_base_path('images/')

    pygame.init()

    game_display = EmulatorDisplay(*screen_size) if use_emulator else PixelDisplay(*screen_size)
    game_input = Gamepad() if use_gamepad else Keyboard()

    PixlBoy(game_display, game_input).run()
