import random

from colors import Colors
from game_types import Pixels, Color
from .scene import Scene


class BarVizScene(Scene):
    def __init__(
            self,
            display,
            seconds_between_renders: float = 0.1,
            bg_color: Color = Colors.black,
            bar_color: Color = Colors.blue,

    ):
        super(BarVizScene, self).__init__(display, seconds_between_renders)

        self.bar_count = display.width
        self.max_height = display.height - 1

        self.bar_heights = [0 for _ in range(self.bar_count)]
        self.bar_height_targets = [random.randint(0, self.max_height) for _ in range(self.bar_count)]

        self.bg_color = bg_color
        self.bar_color = bar_color

    def update(self):
        # Step heights towards targets
        for i in range(self.bar_count):
            while self.bar_heights[i] == self.bar_height_targets[i]:
                self.bar_height_targets[i] = random.randint(0, self.max_height)

            # Pop up and slowly descend
            self.bar_heights[i] = (
                min(self.bar_heights[i] + 3, self.bar_height_targets[i])
                if self.bar_heights[i] < self.bar_height_targets[i]
                else self.bar_heights[i] - 1
            )

        self.display.set_pixels(self.to_pixels())

    def to_pixels(self) -> Pixels:
        return [
            [self.bar_color if i < height else self.bg_color for i in range(self.bar_count)]
            for height in self.bar_heights
        ]
