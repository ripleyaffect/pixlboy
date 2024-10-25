from .animation_scene import AnimationScene


def get_frames(base, count):
    return [
        f'{base}/frame{i}' for i in range(1, count + 1)
    ]


# BACHELOR_FRAMES = get_frames('bachelor', 60)
PUMPKIN_FRAMES = get_frames('pumpkin', 11)
SMILE_FRAMES = get_frames('smiley', 20)
HEART_FRAMES = get_frames('heart', 10)
BEER_FRAMES = get_frames('beer', 34)


class EmojiScene(AnimationScene):
    emoji = [
        PUMPKIN_FRAMES,
        HEART_FRAMES,
        SMILE_FRAMES,
        BEER_FRAMES,
    ]

    def __init__(self, display, initial_emoji_index: int = 0):
        super(EmojiScene, self).__init__(
            display,
            seconds_between_renders=0.2,
            frame_image_names=self.emoji[initial_emoji_index],
            loop=True,
        )

        self.current_emoji_index = initial_emoji_index

    def on_d_right(self):
        self.update_current_emoji_index_by(1)

    def on_d_left(self):
        self.update_current_emoji_index_by(-1)

    def update_current_emoji_index_by(self, amount: int = 0):
        self.current_emoji_index = (self.current_emoji_index + amount) % len(self.emoji)
        self.set_frame_image_names(self.emoji[self.current_emoji_index])
        self.force_render()
