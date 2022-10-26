import pygame

GO_TO_MENU = 1001


class Events:
    go_to_menu_requested = False
    
    @classmethod
    def go_to_menu(cls):
        cls.go_to_menu_requested = True

    @classmethod
    def clear(cls):
        cls.go_to_menu_requested = False
