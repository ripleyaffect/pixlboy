from utils import ImageUtils
from .scene import Scene


class ImageScene(Scene):
    def __init__(
            self,
            display,
            seconds_between_renders: float = 1.0,
            image_name: str = 'test',
    ):
        super(ImageScene, self).__init__(display, seconds_between_renders)

        self.pixels = ImageUtils.get_pixels(image_name)
        self.display.set_pixels(self.pixels)

    def update(self):
        self.display.set_pixels(self.pixels)
