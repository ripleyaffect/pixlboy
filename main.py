import pygame

from displays import EmulatorDisplay, PixelDisplay
from inputs import Keyboard, Gamepad
from pixl_boy import PixlBoy

if __name__ == '__main__':
    use_emulator = True
    use_gamepad = not use_emulator

    pygame.init()

    game_display = EmulatorDisplay(16, 16) if use_emulator else PixelDisplay(16, 16)
    game_input = Gamepad() if use_gamepad else Keyboard()

    PixlBoy(game_display, game_input).run()
