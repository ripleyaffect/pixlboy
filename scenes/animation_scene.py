from events import Events
from utils import ImageUtils
from .scene import Scene


class AnimationScene(Scene):
    def __init__(
            self,
            display,
            seconds_between_renders: float = 0.2,
            frame_image_names: list[str] = None,
            loop: bool = False
    ):
        super(AnimationScene, self).__init__(display, seconds_between_renders)

        # Default value for frames
        if frame_image_names is None:
            frame_image_names = ['test']

        self.current_frame_index = 0
        self.frame_image_names = frame_image_names
        self.frame_count = len(frame_image_names)

        self.loop = loop

        self.set_current_frame()

    def set_frame_image_names(self, new_frame_image_names: list[str]):
        self.current_frame_index = 0
        self.frame_image_names = new_frame_image_names
        self.frame_count = len(new_frame_image_names)

    def update(self):
        self.current_frame_index += 1
        if self.current_frame_index == self.frame_count:
            # We always return to menu after a non-looping animation
            if not self.loop:
                Events.go_to_menu()
                return
            # Loop back to start
            self.current_frame_index = 0
        self.set_current_frame()

    def set_current_frame(self):
        self.display.set_pixels(ImageUtils.get_pixels(self.frame_image_names[self.current_frame_index]))
