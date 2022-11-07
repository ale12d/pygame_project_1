import pygame


class Sound:
    def __init__(self):
        self.click_sound_path = "sounds/click_sound.wav"

    def click_sound(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound(self.click_sound_path))
