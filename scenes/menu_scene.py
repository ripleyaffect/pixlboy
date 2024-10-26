from colors import Colors
from utils import ImageUtils

from .bar_viz_scene import BarVizScene
from .conway_scene import ConwayScene
from .emoji_scene import EmojiScene
from .snake_scene import SnakeScene
from .flappy_scene import FlappyScene
from .score_scene import CountScene
from .scene import Scene


class MenuScene(Scene):
    scenes = [
        SnakeScene,
        FlappyScene,
        BarVizScene,
        EmojiScene,
        ConwayScene,
    ]
    scene_image_names = [
        'snake',
        'flappy',
        'bars',
        'emoji',
        'conway',
    ]

    active_scene_index = 0

    def __init__(self, display):
        super(MenuScene, self).__init__(display)

        self.scene_count = len(self.scenes)

        self.update_display()

    def on_d_left(self):
        self.active_scene_index = (self.active_scene_index - 1) % self.scene_count
        self.update_display()

    def on_d_right(self):
        self.active_scene_index = (self.active_scene_index + 1) % self.scene_count
        self.update_display()

    def on_a_down(self):
        self.next_scene = self.scenes[self.active_scene_index](self.display)
        self.update_display()

    def update_display(self):
        #return
        self.display.set_pixels(self.to_pixels())

    def to_pixels(self):
        # Initialize pixels to the current scene image
        pixels = ImageUtils.get_pixels(f'programs/{self.scene_image_names[self.active_scene_index]}')

        # Render the scene knobs
        scene_count = len(self.scenes)
        px_bt_knobs = self.display.width // (scene_count - 1) - 1

        for (i, scene) in enumerate(self.scenes):
            pixels[0][1 + i * px_bt_knobs] = Colors.violet if self.active_scene_index == i else Colors.gray

        return pixels
