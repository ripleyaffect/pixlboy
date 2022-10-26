import random

from game_types import Color


class Colors:
    MIN = 0
    MAX = 255

    black: Color = (MIN, MIN, MIN)
    gray: Color = (MAX // 2, MAX // 2, MAX // 2)
    white: Color = (MAX, MAX, MAX)

    red: Color = (MAX, 0, 0)
    orange: Color = (MAX, MAX // 2, 0)
    yellow: Color = (MAX, MAX, 0)
    green: Color = (0, MAX, 0)
    blue: Color = (0, 0, MAX)
    indigo: Color = (MAX // 4, 0, MAX // 2)
    violet: Color = (MAX // 2, 0, MAX)

    rainbow = [
        red,
        orange,
        yellow,
        green,
        blue,
        indigo,
        violet,
    ]

    palette_0 = rainbow
    palette_1 = [
        blue,
        blue,
        blue,
        blue,
        blue,
        red,
        white,
        red,
        white,
        red,
        white,
        red,
        white,
        red,
        white,
        red,
    ]
    palette_2 = [
        (98, 71, 170),
        (221, 221, 223),
        (208, 196, 223),
        (220, 171, 223),
        (199, 146, 223),
    ]
    palette_3 = [
        red,
        green,
        blue,
    ]
    palette_4 = [
        violet,
        orange,
    ]
    palette_5 = [
        blue,
        blue,
        blue,
        blue,
        blue,
        blue,
        blue,
        blue,
        yellow,
        yellow,
        yellow,
        yellow,
        yellow,
        yellow,
        yellow,
        yellow,
    ]

    palettes = [
        palette_0,
        palette_1,
        palette_2,
        palette_3,
        palette_4,
        palette_5,
    ]

    @classmethod
    def get_random_palette(cls):
        return cls.palettes[random.randint(0, len(cls.palettes) - 1)]
