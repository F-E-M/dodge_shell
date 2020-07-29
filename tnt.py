import pygame
from pygame.sprite import Sprite
import random


class TNT(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("tnt.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(132, 1130)
        self.rect.top = self.screen_rect.top
        self.y = float(self.rect.y)
        self.speed = 0.4

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
