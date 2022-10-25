import pygame

GO_TO_MENU = 1001


class Events:
    go_to_menu_requested = False
    
    @staticmethod
    def go_to_menu():
        go_to_menu_requested = True
