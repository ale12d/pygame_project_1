import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        screen.fill((48, 96, 130))
        play_img = pygame.image.load('medias/play_btn.png').convert_alpha()
        load_img = pygame.image.load('medias/load_btn.png').convert_alpha()
        settings_img = pygame.image.load('medias/settings_btn.png').convert_alpha()
        exit_img = pygame.image.load('medias/exit_btn.png').convert_alpha()

        rx = screen_width / 1152
        play_img = pygame.transform.scale(play_img, (int(play_img.get_width() * rx), int(play_img.get_height() * rx)))
        load_img = pygame.transform.scale(load_img, (int(load_img.get_width() * rx), int(load_img.get_height() * rx)))
        settings_img = pygame.transform.scale(settings_img, (int(settings_img.get_width() * rx), int(settings_img.get_height() * rx)))
        exit_img = pygame.transform.scale(exit_img, (int(exit_img.get_width() * rx), int(exit_img.get_height() * rx)))

        play_button = MainMenu.button(self, screen, (0, screen_height-play_img.get_height()), play_img)
        load_button = MainMenu.button(self, screen, (play_img.get_width()+13, screen_height-play_img.get_height()), load_img)
        settings_button = MainMenu.button(self, screen, ((screen_width-exit_img.get_width()-settings_img.get_width()-11), screen_height-play_img.get_height()), settings_img)
        exit_button = MainMenu.button(self, screen, ((screen_width-exit_img.get_width()), screen_height-play_img.get_height()), exit_img)

        return play_button, load_button, settings_button, exit_button

    def button(self, screen, position, img):
        width = img.get_width()
        height = img.get_height()
        img = pygame.transform.scale(img, (int(width), int(height)))
        rect = img.get_rect()
        rect.topleft = position
        return screen.blit(img, (rect.x, rect.y))

class LoadMenu:
    def __init__(self):
        pass


class SettingsMenu:
    def __init__(self):
        pass

    def display(self, screen):
        resolution_button = MainMenu.button(self, screen, (25, 100), "resolution")

        return resolution_button
