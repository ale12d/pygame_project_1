import pygame


class SoundGlobal:
    def __init__(self, sound):
        self.click_sound_path = "sounds/audio/click_sound.wav"
        self.sound = sound

    def click_sound(self):
        if self.sound:
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.click_sound_path))
