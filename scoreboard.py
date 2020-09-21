import pygame


class Scoreboard:
    def __init__(self, screen, stats, hard):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats
        self.color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.score_image = None
        self.lv_image = None
        self.score_rect = None
        self.lv_rect = None
        self.hard = hard
        self.prep_score()
        self.prep_lv()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_lv(self):
        self.lv_image = self.font.render(str(self.hard), True, self.color)
        self.lv_rect = self.lv_image.get_rect()
        self.lv_rect.right = self.score_rect.right
        self.lv_rect.top = self.score_rect.bottom + 10

    def blitme(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lv_image, self.lv_rect)


class CoolDown:
    def __init__(self, screen, steve):
        self.font = pygame.font.SysFont(None, 48)
        self.screen = screen
        self.steve = steve
        self.cool_down = self.steve.cool_down
        self.act = str(self.steve.kicking)
        self.cool_image = None
        self.cool_rect = None
        self.act_image = None
        self.act_rect = None
        self.color_c = (0, 0, 255)
        self.color_a = (255, 0, 0)
        if self.cool_down is not None:
            self.cool_down = str(self.cool_down)
        self.prep_cool()
        self.prep_act()

    def prep_cool(self):
        self.cool_image = self.font.render(self.cool_down, True, self.color_c)
        self.cool_rect = self.cool_image.get_rect()
        self.cool_rect.centerx = self.steve.rect.centerx
        self.cool_rect.bottom = self.steve.rect.top - 40

    def prep_act(self):
        self.act_image = self.font.render(self.act, True, self.color_a)
        self.act_rect = self.act_image.get_rect()
        self.act_rect.centerx = self.steve.rect.centerx
        self.act_rect.bottom = self.steve.rect.top - 40

    def blitme_c(self):
        if self.cool_down is None or int(self.cool_down) <= 0:
            pass
        else:
            self.screen.blit(self.cool_image, self.cool_rect)

    def blitme_a(self):
        if int(self.act) <= 0:
            pass
        else:
            self.screen.blit(self.act_image, self.act_rect)


class Magic:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (0, 100, 255)
        self.mg_img = None
        self.mg_rect = None
        self.font = pygame.font.SysFont(None, 48)

    def prep_display(self, magic):
        magic = str(magic)
        self.mg_img = self.font.render(magic, True, self.color)
        self.mg_rect = self.mg_img.get_rect()
        self.mg_rect.left = self.screen_rect.left
        self.mg_rect.top = 73

    def blitme(self):
        self.screen.blit(self.mg_img, self.mg_rect)
