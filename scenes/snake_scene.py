import random
import time

from colors import Colors
from events import Events
from .explosion_scene import ExplosionScene
from .score_scene import ScoreScene
from .scene import Scene

class Snake:
    def __init__(self, nodes: list[(int, int)]):
        self.nodes = nodes
        self.head = nodes[0]
        self.tail = nodes[-1]

    def move(self, new_head: (int, int), add_node: bool = False):
        if add_node:
            self.nodes = [new_head] + self.nodes
        else:
            self.nodes = [new_head] + self.nodes[:-1]


class SnakeScene(Scene):
    UP_DIRECTION = (0, 1)
    DOWN_DIRECTION = (0, -1)
    LEFT_DIRECTION = (-1, 0)
    RIGHT_DIRECTION = (1, 0)

    def __init__(self, display, seconds_between_renders: float = 0.12):
        super(SnakeScene, self).__init__(display, seconds_between_renders)

        self.score = 0

        # Place the head at the center of the screen
        head = (display.width // 2, display.height // 2)
        t_1 = (head[0] - 1, head[1])
        t_2 = (head[0] - 2, head[1])
        self.snake = Snake([head, t_1, t_2])

        self.direction = self.RIGHT_DIRECTION
        self.next_direction = self.RIGHT_DIRECTION

        self.apple = (1, 1)
        self.place_apple()

    def on_d_up(self):
        if self.direction != self.DOWN_DIRECTION:
            self.next_direction = self.UP_DIRECTION

    def on_d_down(self):
        if self.direction != self.UP_DIRECTION:
            self.next_direction = self.DOWN_DIRECTION

    def on_d_left(self):
        if self.direction != self.RIGHT_DIRECTION:
            self.next_direction = self.LEFT_DIRECTION

    def on_d_right(self):
        if self.direction != self.LEFT_DIRECTION:
            self.next_direction = self.RIGHT_DIRECTION

    def update(self):
        # Update and move in the next direction
        self.direction = self.next_direction
        next_head = (
            self.snake.nodes[0][0] + self.direction[0],
            self.snake.nodes[0][1] + self.direction[1]
        )
        got_apple = next_head == self.apple

        self.snake.move(next_head, got_apple)

        if got_apple:
            self.score += 1
            self.place_apple()

        # Lose if head is out of bounds or hit body
        head = self.snake.nodes[0]
        if (
                head[0] < 0 or
                head[1] < 0 or
                head[0] >= self.display.width or
                head[1] >= self.display.height or
                len([val for val in self.snake.nodes[1:] if self.snake.nodes[0] == val]) > 0
        ):
            self.next_scene = ExplosionScene(self.display, next_scene=ScoreScene(self.display, self.score))
            return

        self.display.set_pixels(self.to_pixels())

    def place_apple(self):
        self.apple = (
            random.randint(0, self.display.width - 1),
            random.randint(0, self.display.height - 1),
        )
        while self.apple in self.snake.nodes:
            self.apple = (
                random.randint(0, self.display.width - 1),
                random.randint(0, self.display.height - 1),
            )

    def to_pixels(self):
        # Initialize all pixels to zero
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        # Overwrite pixels with the snake
        for node in self.snake.nodes:
            pixels[node[1]][node[0]] = Colors.white

        pixels[self.apple[1]][self.apple[0]] = Colors.violet

        return pixels
