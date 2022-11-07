import pygame
from scales import Scale


class Play:
    def __init__(self, screen):
        self.screen = screen
        self.button = None

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()
        self.x, self.y = 0, 0

    def set(self):
        self.load()
        self.scale()
        self.position()
        img, position = self.create_button()

        return img, position

    def load(self):
        self.button = pygame.image.load('medias/play_btn.png').convert_alpha()

    def scale(self):
        self.button = pygame.transform.scale(self.button, (int(self.button.get_width() * self.rx), int(self.button.get_height() * self.ry)))

    def position(self):
        self.x = 10*self.rx
        self.y = self.screen.get_height() - self.button.get_height() - (1*self.rx)

    def create_button(self):
        rect = self.button.get_rect()
        rect.topleft = (self.x, self.y)
        return self.button, (rect.x, rect.y)


class Load:
    def __init__(self, screen):
        self.screen = screen
        self.button = None

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()
        self.x, self.y = 0, 0

    def set(self):
        self.load()
        self.scale()
        self.position()
        img, position = self.create_button()

        return img, position

    def load(self):
        self.button = pygame.image.load('medias/load_btn.png').convert_alpha()

    def scale(self):
        self.button = pygame.transform.scale(self.button, (int(self.button.get_width() * self.rx), int(self.button.get_height() * self.ry)))

    def position(self):
        self.x = 32*self.rx
        self.y = self.screen.get_height() - self.button.get_height() - (1*self.rx)

    def create_button(self):
        rect = self.button.get_rect()
        rect.topleft = (self.x, self.y)
        return self.button, (rect.x, rect.y)


class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.button = None

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()
        self.x, self.y = 0, 0

    def set(self):
        self.load()
        self.scale()
        self.position()
        img, position = self.create_button()

        return img, position

    def load(self):
        self.button = pygame.image.load('medias/settings_btn.png').convert_alpha()

    def scale(self):
        self.button = pygame.transform.scale(self.button, (int(self.button.get_width() * self.rx), int(self.button.get_height() * self.ry)))

    def position(self):
        self.x = 55*self.rx
        self.y = self.screen.get_height() - self.button.get_height() - (1*self.rx)

    def create_button(self):
        rect = self.button.get_rect()
        rect.topleft = (self.x, self.y)
        return self.button, (rect.x, rect.y)


class Exit:
    def __init__(self, screen):
        self.screen = screen
        self.button = None

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()
        self.x, self.y = 0, 0

    def set(self):
        self.load()
        self.scale()
        self.position()
        img, position = self.create_button()

        return img, position

    def load(self):
        self.button = pygame.image.load('medias/exit_btn.png').convert_alpha()

    def scale(self):
        self.button = pygame.transform.scale(self.button, (int(self.button.get_width() * self.rx), int(self.button.get_height() * self.ry)))

    def position(self):
        self.x = 91*self.rx
        self.y = self.screen.get_height() - self.button.get_height() - (1*self.rx)

    def create_button(self):
        rect = self.button.get_rect()
        rect.topleft = (self.x, self.y)
        return self.button, (rect.x, rect.y)

