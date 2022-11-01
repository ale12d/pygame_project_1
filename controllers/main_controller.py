import pygame
from sys import exit


class ApplicationController:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 400))

    def start(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                ApplicationController.quit(self, event)
                pygame.display.update()

    def quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
