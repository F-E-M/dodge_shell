import pygame
from time import sleep


class Steve:
    def __init__(self, screen, skin):
        self.screen = screen

        # load image and get rect
        self.image = pygame.image.load(f"skin/{skin}.png")
        self.image = pygame.transform.scale(self.image, (82, 163))
        self.kick_image = pygame.image.load(f"skin/{skin}_kick.png")
        self.kick_image = pygame.transform.scale(self.kick_image, (82, 163))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put steve in the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # put float in "center"
        self.center = float(self.rect.centerx)

        # moving flag
        self.RF = False
        self.LF = False

        # speed
        self.speed = None

        # kicking
        self.kick = False
        self.kicking = 0
        self.kick_start = None
        self.cool_down = 0

        # magic
        self.magic = 100

    def update(self):
        if self.RF and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.LF and self.rect.left > 0:
            self.center -= self.speed

        # update rect
        self.rect.centerx = self.center

    def blitme(self):
        if self.kick:
            self.screen.blit(self.kick_image, self.rect)
        else:
            self.screen.blit(self.image, self.rect)


class Health:
    def __init__(self, screen, position):
        self.screen = screen
        self.image = pygame.image.load("totem.png")
        self.image = pygame.transform.scale(self.image, (52, 63))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        if position == 1:
            self.rect.x = 0
            self.heal_num = 1
        elif position == 2:
            self.rect.x = 52
            self.heal_num = 2
        elif position == 3:
            self.rect.x = 104
            self.heal_num = 3
        self.ok = True

    def update(self, heal):
        if heal < self.heal_num:
            self.ok = False

    def blitme(self):
        if self.ok:
            self.screen.blit(self.image, self.rect)


def use_totem(screen, steve, heal):
    if heal >= 0:
        img = pygame.image.load("totem_using.jpg")
        img = pygame.transform.scale(img, (52, 63))
        rect = img.get_rect()
        rect.centerx = steve.rect.centerx
        rect.y = steve.rect.y - 90
        while rect.y > 0:
            screen.blit(img, rect)
            rect.y -= 1
            sleep(0.000003)
            pygame.display.flip()
