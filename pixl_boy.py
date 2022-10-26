import pygame
import sys

import events
from displays.display import Display
from events import Events
from inputs import Gamepad, Keyboard
from scenes.menu_scene import MenuScene


class PixlBoy:
    def __init__(self, display: Display, input):
        # Set up externals
        self.display = display
        self.input = input

        # Initialize the scene
        self.menu_scene = MenuScene(self.display)
        self.scene = self.menu_scene

    def run(self):
        while True:
            self.process_events()
            self.scene = self.scene.render()

    def go_to_menu(self):
        self.menu_scene.next_scene = self.menu_scene
        self.go_to_scene(self.menu_scene)
        self.menu_scene.update_display()

    def go_to_scene(self, scene):
        self.scene = scene

    def process_events(self):
        if Events.go_to_menu_requested:
            self.go_to_menu()
            Events.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == events.GO_TO_MENU:
                self.go_to_menu()
            else:
                self.input.process_event(event, self.scene)
