import pygame


class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def set_framerate(self, framerate):
        self.clock.tick(framerate)