from game_types import Color


class Colors:
    MIN = 0
    MAX = 128

    black: Color = (MIN, MIN, MIN)
    gray: Color = (MAX // 2, MAX // 2, MAX // 2)
    white: Color = (MAX, MAX, MAX)

    red: Color = (MAX, 0, 0)
    green: Color = (0, MAX, 0)
    blue: Color = (0, 0, MAX)
