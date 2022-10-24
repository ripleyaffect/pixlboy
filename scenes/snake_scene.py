import time

from colors import Colors
from events import Events
from .scene import Scene


class SnakeScene(Scene):
    starting_direction = (1, 0)

    def __init__(self, display, seconds_between_renders: float = 0.2):
        super(SnakeScene, self).__init__(display, seconds_between_renders)

        # Place the head at the center of the screen
        self.snake = [(display.width // 2, display.height // 2)]
        self.direction = self.starting_direction

    def on_d_up(self):
        self.direction = (0, 1)

    def on_d_down(self):
        self.direction = (0, -1)

    def on_d_left(self):
        self.direction = (-1, 0)

    def on_d_right(self):
        self.direction = (1, 0)

    def update(self):
        # Move the head in the current direction
        self.snake[0] = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        # Lose if head is out of bounds or hit body
        head = self.snake[0]
        if (
                head[0] < 0 or
                head[1] < 0 or
                head[0] >= self.display.width or
                head[1] >= self.display.height or
                len([val for val in self.snake[1:] if self.snake[0] == val]) > 0
        ):
            Events.go_to_menu()
            return

        self.display.set_pixels(self.to_pixels())

    def to_pixels(self):
        # Initialize all pixels to zero
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        # Overwrite pixels with the snake
        for part in self.snake:
            pixels[part[1]][part[0]] = Colors.white

        return pixels
