import pygame


class Mouse:
    def __init__(self, event):
        self.event = event
        self.click = False

    def click_check(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
        return self.click
