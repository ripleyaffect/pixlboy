import random

from colors import Colors
from game_types import Pixels
from .scene import Scene


class BarVizScene(Scene):
    palettes = Colors.palettes

    def __init__(
            self,
            display,
            seconds_between_renders: float = 0.1,
            initial_palette_index: int = 0
    ):
        super(BarVizScene, self).__init__(display, seconds_between_renders)

        self.bar_count = display.width
        self.max_height = display.height - 1

        self.bar_heights = [0 for _ in range(self.bar_count)]
        self.bar_height_targets = [random.randint(0, self.max_height) for _ in range(self.bar_count)]

        self.current_palette_index = initial_palette_index

        self.set_palette()

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
            [
                self.palette[i % self.palette_count] if y <= self.bar_heights[i] else Colors.black
                for i in range(self.bar_count)
            ]
            for y in range(len(self.bar_heights))
        ]

    def set_palette(self):
        self.palette = self.palettes[self.current_palette_index]
        self.palette_count = len(self.palette)

    def on_d_right(self):
        self.update_current_palette_index_by(1)

    def on_d_left(self):
        self.update_current_palette_index_by(-1)

    def update_current_palette_index_by(self, amount: int = 0):
        self.current_palette_index = (self.current_palette_index + amount) % len(self.palettes)
        self.set_palette()
        self.force_render()
