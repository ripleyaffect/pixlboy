import pygame

GO_TO_MENU = 1001


class Events:

    @staticmethod
    def go_to_menu():
        pygame.event.post(pygame.event.Event(GO_TO_MENU, {}))
