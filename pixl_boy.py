import random

import pygame
import sys

import events
from displays.display import Display
from input import Gamepad
from scenes import ConwayScene, ImageScene, BarVizScene
from scenes.menu_scene import MenuScene


class PixlBoy:
    def __init__(self, display: Display, use_gamepad: bool = False):
        # Set up externals
        self.display = display
        self.use_gamepad = use_gamepad

        if self.use_gamepad:
            self.gamepad = Gamepad()

        self.menu_scene = MenuScene(self.display)
        self.scene = ImageScene(self.display, image_name='test')

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == events.GO_TO_MENU:
                self.go_to_menu()
            elif self.use_gamepad:
                self.gamepad.process_event(event, self.scene)
