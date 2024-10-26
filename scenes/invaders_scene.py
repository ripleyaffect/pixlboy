from colors import Colors

from .scene import Scene


class InvadersScene(Scene):
    def __init__(self, display):
        super(InvadersScene, self).__init__(display, 0.12)

        self.health = 16
        self.player = Player(7, 1)
        self.bullets = []
        self.invaders = []

        self.player_move_x = 0
        self.score = 0

    def on_d_right(self):
        self.player.x = min(self.player.x + 1, 15)

    def on_d_left(self):
        self.player.x = max(self.player.x - 1, 0)

    def on_a_down(self):
        self.bullets.append(Bullet(self.player.x, self.player.y + 1))

    def update(self):
        for bullet in self.bullets:
            bullet.y += 1
            for invader in self.invaders:
                if bullet.x == invader.x and bullet.y == invader.y:
                    invader.hit = True

        self.bullets = [b for b in self.bullets if b.y < 16]

        added_score = 0
        for invader in self.invaders:
            if invader.hit:
                added_score += 1
                continue
            invader.tick()
        self.score += added_score

        self.invaders = [i for i in self.invaders if not i.hit]

        self.display.set_pixels(self.to_pixels())

    def to_pixels(self):
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        # Draw player
        pixels[self.player.y][self.player.x] = Colors.white

        return pixels

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Bullet:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Invader:
    def __init__(self, x: int, y: int, move_ticks: int = 5):
        self.x = x
        self.y = y
        self.ticks_to_move = move_ticks
        self.hit = False

    def tick(self):
        self.ticks_to_move -= 1
        if self.ticks_to_move <= 0:
            self.move()

    def move():
        self.y -= 1
