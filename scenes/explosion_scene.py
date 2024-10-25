from .animation_scene import AnimationScene


class ExplosionScene(AnimationScene):
    frame_image_names = [
        'explosion/frame1',
        'explosion/frame2',
        'explosion/frame3',
        'explosion/frame4',
        'explosion/frame5',
        'explosion/frame6',
        'explosion/frame7',
        'explosion/frame8',
        'explosion/frame9',
        'explosion/frame10',
    ]

    def __init__(self, display, next_scene=None):
        super(ExplosionScene, self).__init__(
            display,
            seconds_between_renders=0.1,
            frame_image_names=self.frame_image_names,
            completed_scene=next_scene,
        )
