import pygame


class SoundGlobal:
    def __init__(self):
        self.click_sound_path = "sounds/audio/click_sound.wav"

    def click_sound(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound(self.click_sound_path))
