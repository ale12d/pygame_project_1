import pygame
from main_menu.main import Menu


class ApplicationController:
    def __init__(self):
        self.app_name = 'game1'

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.app_name)
        screen = pygame.display.set_mode((800, 600))

        # show menu / .set call all menu views and controllers
        menu = Menu(screen)
        menu.set()
