import pygame


class Mouse:
    def __init__(self, event):
        self.event = event
        self.click = False

    def click_check(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
        return self.click


class Keyboard:
    def __init__(self, event):
        self.event = event

    def arrow_keys(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_LEFT:
                print('l')
            if self.event.key == pygame.K_RIGHT:
                print('r')
            if self.event.key == pygame.K_UP:
                pass
            if self.event.key == pygame.K_DOWN:
                pass
