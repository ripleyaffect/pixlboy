import random

from .scene import Scene
from .explosion_scene import ExplosionScene
from .score_scene import ScoreScene
from colors import Colors

class FlappyScene(Scene):
    def __init__(self, display, seconds_between_renders: float = 0.12):
        super(FlappyScene, self).__init__(display, seconds_between_renders)

        self.bird_x = 3
        self.bird_y = 8
        self.pipes = [Pipe(self.display.width, 4)]
        self.score = 0
        self.flapping = False

    def on_a_down(self):
        self.bird_y = min(self.bird_y + 3, 15)

    # def on_a_up(self):
    #     self.flapping = False

    def update(self):
        self.bird_y = max(self.bird_y - 1, -1)
        if self.bird_y < 0:
            self.next_scene = ExplosionScene(self.display, next_scene=ScoreScene(self.display, self.score))

        # Remove off-screen pipes
        removed_pipe = False
        new_pipes = []
        for pipe in self.pipes:
            pipe.x -= 1
            if pipe.x < 0:
                removed_pipe = True
                continue
            elif pipe.x == self.bird_x:
                if pipe.collides_with(self.bird_y):
                    self.next_scene = ExplosionScene(self.display, next_scene=ScoreScene(self.display, self.score))
                    return
                # Spawn next pipe
                new_pipes.append(Pipe(
                    self.display.width - 1,
                    self.get_pipe_gap_y(),
                    self.get_pipe_gap_height()
                ))
            new_pipes.append(pipe)

        # Add new pipe
        if removed_pipe:
            self.score += 1


        self.pipes = new_pipes

        # if self.bird.x > self.pipe.x + self.pipe.width:
        #     self.score += 1
        #     self.pipe = Pipe(self.display.width, self.display.height, self.display)

        self.display.set_pixels(self.to_pixels())

    def to_pixels(self):
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        # Draw bird
        pixels[self.bird_y][3] = Colors.yellow

        # Draw pipes
        for pipe in self.pipes:
            for y in range(self.display.height):
                if pipe.gap_y <= y <= pipe.gap_y + pipe.gap_height:
                    continue
                pixels[y][pipe.x] = Colors.green

        return pixels

    def get_pipe_gap_y(self):
        min = 6
        if self.score > 5:
            min = 5
        if self.score > 10:
            min = 4
        if self.score > 15:
            min = 3

        max = 10
        if self.score > 5:
            max = 11
        if self.score > 10:
            max = 12
        if self.score > 15:
            max = 13

        return random.randint(min, max)

    def get_pipe_gap_height(self):
        min = 4
        if self.score > 5:
            min = 3
        if self.score > 10:
            min = 2
        if self.score > 15:
            min = 1

        max = 6
        if self.score > 5:
            max = 5
        if self.score > 10:
            max = 4

        return random.randint(min, max)


class Pipe:
    def __init__(self, x, gap_y, gap_height=3):
        self.x = x
        self.gap_y = gap_y
        self.gap_height = gap_height

    def collides_with(self, bird_y):
        return self.x == 3 and not self.gap_y <= bird_y <= self.gap_y + self.gap_height
