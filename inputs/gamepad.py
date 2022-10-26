import pygame

from events import Events


class Gamepad:
    A_BUTTON = 1
    B_BUTTON = 2
    X_BUTTON = 0
    Y_BUTTON = 3
    START_BUTTON = 9

    def __init__(self, gamepad_id: int = 0):
        self.joystick = pygame.joystick.Joystick(gamepad_id)
        self.joystick.init()

    def process_event(self, event, scene):
        if event.type == pygame.JOYAXISMOTION:
            x = self.joystick.get_axis(0)
            # Up is negative, but we want it to be positive
            y = -self.joystick.get_axis(1)

            if y > 0.5: scene.on_d_up()
            elif y < -0.5: scene.on_d_down()
            elif x < -0.5: scene.on_d_left()
            elif x > 0.5: scene.on_d_right()
            else: scene.on_d_zero()

        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == self.A_BUTTON: scene.on_a_down()
            elif event.button == self.B_BUTTON: scene.on_b_down()
            elif event.button == self.X_BUTTON: scene.on_x_down()
            elif event.button == self.Y_BUTTON: scene.on_y_down()
            elif event.button == self.START_BUTTON: Events.go_to_menu()
        if event.type == pygame.JOYBUTTONUP:
            if event.button == self.A_BUTTON: scene.on_a_up()
            elif event.button == self.B_BUTTON: scene.on_b_up()
            elif event.button == self.X_BUTTON: scene.on_x_up()
            elif event.button == self.Y_BUTTON: scene.on_y_up()
