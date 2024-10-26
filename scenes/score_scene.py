from colors import Colors

from .scene import Scene
from events import Events


class ScoreScene(Scene):
    def __init__(self, display, score: int):
        super(ScoreScene, self).__init__(display, 1.0)

        self.score = score

    def on_a_down(self):
        Events.go_to_menu()

    def update(self):
        self.display.set_pixels(self.to_pixels())

    def to_pixels(self):
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        tens = self.score // 10
        ones = self.score % 10

        # Draw score
        pixels = self.draw_number(tens, 1, 4, pixels)
        pixels = self.draw_number(ones, 7, 4, pixels)

        return pixels

    def draw_number(self, value: int, x: int, y: int, pixels: list[list[int]]):
        number = NUMBERS[value]
        for (i, row) in enumerate(number):
            for (j, pixel) in enumerate(row):
                if pixel == '*':
                    pixels[y + i][x + j] = Colors.white

        return pixels


ZERO = [
    '        ',
    '  ****  ',
    '  *  *  ',
    '  *  *  ',
    '  *  *  ',
    '  *  *  ',
    '  ****  ',
    '        ',
]

ONE = [
    '        ',
    '  **    ',
    '   *    ',
    '   *    ',
    '   *    ',
    '   *    ',
    '  ***   ',
    '        ',
]
ONE.reverse()

TWO = [
    '        ',
    '  ****  ',
    '  *  *  ',
    '     *  ',
    '  ****  ',
    '  *     ',
    '  ****  ',
    '        ',
]
TWO.reverse()

THREE = [
    '        ',
    '  ****  ',
    '     *  ',
    '   ***  ',
    '     *  ',
    '     *  ',
    '  ****  ',
    '        ',
]
THREE.reverse()

FOUR = [
    '        ',
    '  *  *  ',
    '  *  *  ',
    '  *  *  ',
    '  ***** ',
    '     *  ',
    '     *  ',
    '        ',
]
FOUR.reverse()

FIVE = [
    '        ',
    '  ****  ',
    '  *     ',
    '  ****  ',
    '     *  ',
    '     *  ',
    '  ****  ',
    '        ',
]
FIVE.reverse()

SIX = [
    '        ',
    '  ****  ',
    '  *     ',
    '  ****  ',
    '  *  *  ',
    '  *  *  ',
    '  ****  ',
    '        ',
]
SIX.reverse()

SEVEN = [
    '        ',
    '  ****  ',
    '     *  ',
    '    *   ',
    '   *    ',
    '   *    ',
    '   *    ',
    '        ',
]
SEVEN.reverse()

EIGHT = [
    '        ',
    '  ****  ',
    '  *  *  ',
    '  ****  ',
    '  *  *  ',
    '  *  *  ',
    '  ****  ',
    '        ',
]
EIGHT.reverse()

NINE = [
    '        ',
    '  ****  ',
    '  *  *  ',
    '  ****  ',
    '     *  ',
    '     *  ',
    '  ****  ',
    '        ',
]
NINE.reverse()


NUMBERS = [
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
]

class CountScene(ScoreScene):
    def __init__(self, display):
        super(CountScene, self).__init__(display, 0)

    def update(self):
        self.score += 1
        self.display.set_pixels(self.to_pixels())
