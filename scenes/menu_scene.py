from colors import Colors

from .bar_viz_scene import BarVizScene
from .conway_scene import ConwayScene
from .image_scene import ImageScene
from .snake_scene import SnakeScene
from .scene import Scene


class MenuScene(Scene):
    scenes = [
        SnakeScene,
        BarVizScene,
        ConwayScene,
        ImageScene,
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
        # Initialize all pixels to zero
        pixels = [
            [Colors.black for _ in range(self.display.width)]
            for _ in range(self.display.height)
        ]

        # Render the scene knobs
        scene_count = len(self.scenes)
        px_bt_knobs = self.display.width // (scene_count - 1)
        for (i, scene) in enumerate(self.scenes):
            pixels[0][i * px_bt_knobs] = Colors.white if self.active_scene_index == i else Colors.gray

        return pixels
