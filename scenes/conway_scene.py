import random
import time

from colors import Colors
from game_types import Pixels, Color
from .scene import Scene


class ConwayScene(Scene):
    MINIMUM_ON = 15
    NEIGHBORS_DELTAS = [
        (-1,  1), (0,  1), (1,  1),
        (-1,  0),          (1,  0),
        (-1, -1), (0, -1), (1, -1),
    ]

    def __init__(
            self,
            display,
            seconds_between_renders: float = 0.5,
            off_color: Color = Colors.black,
            on_color: Color = Colors.violet,
            randomize: bool = True,
        ):
        super(ConwayScene, self).__init__(display, seconds_between_renders)

        self.width = display.width
        self.height = display.height

        self.grid = [
            [0 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        if randomize:
            self.randomize()

        self.on_color = on_color
        self.off_color = off_color

    def on_a_down(self):
        self.randomize()

    def update(self):
        self.step()
        self.display.set_pixels(self.to_pixels())

    def randomize(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = random.randint(0, 1)

    def step(self):
        # Keep the party going
        if (self.get_on_total_count() < self.MINIMUM_ON):
            self.randomize()

        next_grid = [
            [self.get_next(x, y) for x in range(self.width)]
            for y in range(self.height)
        ]
        self.grid = next_grid

    def get_next(self, x, y):
        on = self.grid[y][x]
        on_neighbor_count = self.get_on_neighbor_count(x, y)

        if on:
            if 2 <= on_neighbor_count <= 3:
                return 1
            return 0

        if on_neighbor_count == 3:
            return 1

        return 0

    def get_on_neighbor_count(self, x, y):
        return sum([
            self.grid[(y + delta[1]) % self.height][(x + delta[0]) % self.width]
            for delta in self.NEIGHBORS_DELTAS
        ])

    def get_on_total_count(self):
        return sum([
            sum(row)
            for row in self.grid
        ])

    def to_pixels(self) -> Pixels:
        return [
            [self.on_color if on else self.off_color for on in row]
            for row in self.grid
        ]
