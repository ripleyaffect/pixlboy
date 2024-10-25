import pygame

from events import Events


class Keyboard:
    W_KEY = 119
    A_KEY = 97
    S_KEY = 115
    D_KEY = 100
    SPACE_KEY = 32
    ESC_KEY = 27

    def process_event(self, event, scene):
        if event.type == pygame.KEYDOWN:
            if event.key == self.W_KEY: scene.on_d_up()
            elif event.key == self.S_KEY: scene.on_d_down()
            elif event.key == self.A_KEY: scene.on_d_left()
            elif event.key == self.D_KEY: scene.on_d_right()
            elif event.key == self.SPACE_KEY: scene.on_a_down()
            elif event.key == self.ESC_KEY: Events.go_to_menu()
        elif event.type == pygame.KEYUP:
            if event.key == self.SPACE_KEY: scene.on_a_up()
