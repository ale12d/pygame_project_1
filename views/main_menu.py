import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen):
        play_img = pygame.image.load('medias/play_btn.png').convert_alpha()
        load_img = pygame.image.load('medias/load_btn.png').convert_alpha()
        settings_img = pygame.image.load('medias/settings_btn.png').convert_alpha()
        exit_img = pygame.image.load('medias/exit_btn.png').convert_alpha()
        play_button = MainMenu.button2(self, screen, (25, 600), play_img)
        load_button = MainMenu.button2(self, screen, (325, 600), load_img)
        settings_button = MainMenu.button2(self, screen, (625, 600), settings_img)
        exit_button = MainMenu.button2(self, screen, (1100, 600), exit_img)

        return play_button, load_button, settings_button, exit_button

    def button(self, screen, position, text):
        font = pygame.font.SysFont("Arial", 50)
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
        return screen.blit(text_render, (x, y))

    def button2(self, screen, position, img):
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
