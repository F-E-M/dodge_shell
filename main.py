# hole project
# type <python-project main.py>
# version <1.3.0-beta-I> <snapshot>
# online version <1.3-beta-I>
# status <ok> <online>
# ==========project from Infinity-Energy=========
import time
import pygame
import pygame.locals
import game_func as gf
from settings import Settings
from Steve import Steve, Health
from pygame.sprite import Group
from tnt import TNT
from launcher import *
from scoreboard import Scoreboard, CoolDown
from game_stats import GameStats
from ctypes import windll
import random


def run_game(piano, frame):
    # init game
    hard = 1
    clock = pygame.time.Clock()
    set_window_pos = windll.user32.SetWindowPos
    pygame.init()
    settings = Settings()
    gs = GameStats()
    gs.reset()
    my_font = pygame.font.SysFont("kaiti", 100)
    tnts = Group()

    # init window
    screen = pygame.display.set_mode((settings.width, settings.height))
    set_window_pos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)
    screen_rect = screen.get_rect()
    icon = pygame.image.load("icon.ico")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("dodge tnt")

    # init player
    steve = Steve(screen, skin)

    # heal instruction
    h1 = Health(screen, 1)
    h2 = Health(screen, 2)
    h3 = Health(screen, 3)
    t1 = time.time()
    start_rec = t1
    tnt_num = 0

    pygame.mouse.set_visible(False)
    heal = 3
    # main loop
    while True:
        clock.tick(frame)
        h1.update(heal)
        h2.update(heal)
        h3.update(heal)
        t2 = time.time()
        nowrec = t2
        nhard = int((nowrec + 20 - start_rec) / (20 + int(hard / 2)))
        if nhard > hard:
            hard = nhard
        tntw = int(nowrec + 70 - start_rec) / (hard * 41)
        steve_tnt = False
        if random.randint(0, 4) == 0:
            steve_tnt = True
        sb = Scoreboard(screen, gs, hard)
        cool_down = CoolDown(screen, steve)
        steve.speed = hard * 1.3
        if t2 - t1 > tntw:
            if tnt_num <= 4:
                tnt_num += 1
                new_tnt = TNT(screen)
                new_tnt.speed += hard * 0.6
                if steve_tnt:
                    new_tnt.rect.centerx = steve.rect.centerx
                tnts.add(new_tnt)
                hard -= 1
                t1 = t2

        start_rec = gf.check_events(steve, start_rec, screen, my_font, piano)
        steve.update()

        tnts.update()
        gf.kick_minus(steve)
        gf.check_kick(steve)
        ctcsl = gf.check_tnt_c_steve(tnts, steve, heal, tnt_num, screen, gs.score, hard)
        heal = ctcsl[0]
        tnt_num = ctcsl[1]
        gs.score = ctcsl[2]
        con = gf.check_die(heal, gs.score, hard)
        if con:
            run_game(pianos, frame)
        for tnt in tnts.copy():
            if tnt.rect.top >= screen_rect.bottom:
                tnt_num -= 1
                tnts.remove(tnt)
                gs.score += hard
        gf.update_screen(screen, steve, tnts, sb, h1, h2, h3, cool_down)


data_for_game = launcher()
pianos = data_for_game[0]
skin = data_for_game[1]
frame = data_for_game[2]

run_game(pianos, frame)
