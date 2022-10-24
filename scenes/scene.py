import time

from displays.display import Display


class Scene:
    def __init__(self, display: Display, seconds_between_renders: float = 0.0):
        self.display = display
        self.next_scene = self

        self.seconds_between_renders = seconds_between_renders
        self.next_render = time.time()

    # D-Pad handlers

    def on_d_zero(self): pass
    def on_d_up(self): pass
    def on_d_down(self): pass
    def on_d_left(self): pass
    def on_d_right(self): pass

    # Button handlers

    def on_a_down(self): pass
    def on_a_up(self): pass

    def on_b_down(self): pass
    def on_b_up(self): pass

    def on_x_down(self): pass
    def on_x_up(self): pass

    def on_y_down(self): pass
    def on_y_up(self): pass

    def render(self):
        current_time = time.time()
        if self.next_render > current_time:
            return self.next_scene

        self.update()
        self.display.render()

        self.next_render = current_time + self.seconds_between_renders

        return self.next_scene

    def update(self):
        pass
