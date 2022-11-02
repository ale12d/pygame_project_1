import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen):
        play_button = MainMenu.button(self, screen, (25, 300), "play")
        load_button = MainMenu.button(self, screen, (225, 300), "load")
        option_button = MainMenu.button(self, screen, (425, 300), "option")
        quit_button = MainMenu.button(self, screen, (625, 300), "quit")

        return play_button, load_button, option_button, quit_button

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
