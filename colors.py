import random

from game_types import Color


class Colors:
    MIN = 0
    MAX = 255

    black: Color = (MIN, MIN, MIN)
    gray: Color = (MAX // 2, MAX // 2, MAX // 2)
    white: Color =  gray

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

    rainbow_palette = rainbow
    usa_palette = [
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
    purple_palette = [
        (98, 71, 170),
        (221, 221, 223),
        (208, 196, 223),
        (220, 171, 223),
        (199, 146, 223),
    ]
    rgb_palette = [
        red,
        green,
        blue,
    ]
    halloween_palette = [
        violet,
        orange,
    ]
    ukraine_palette = [
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
    uva_palette = [
        blue,
        orange
    ]
    venezuala_palette = [
        yellow,
        yellow,
        yellow,
        yellow,
        yellow,
        blue,
        blue,
        blue,
        blue,
        blue,
        blue,
        red,
        red,
        red,
        red,
        red,
    ]

    palettes = [
        usa_palette,
        halloween_palette,
        rgb_palette,
        rainbow_palette,
    ]


    @classmethod
    def get_random_palette(cls):
        return cls.palettes[random.randint(0, len(cls.palettes) - 1)]
