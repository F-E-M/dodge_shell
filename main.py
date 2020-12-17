# ===========project from github organization "F-E-M"==========
# code by Infinity-Energy
# art by Infinity-Energy, Felixqwq
# test by Infinity-Energy
# ==========Thanks==========
# "Liangyin" Studios provided pre-development support
# The "Xes coding community" provides initial code hosting support

# imports
import time
import sys
import pygame
import pygame.locals
import game_func as gf
from settings import Settings
from Steve import Steve, Health
from pygame.sprite import Group
from tnt import TNT
from launcher import *
from scoreboard import Scoreboard, CoolDown, Magic
from game_stats import GameStats
import random


def run_game(frame, set_music):
    # init game
    hard = 1
    ele_time = 0
    clock = pygame.time.Clock()
    pygame.init()
    settings = Settings()
    gs = GameStats()
    gs.reset()
    if sys.platform == "win32" or sys.platform == "cygwin":
        my_font = pygame.font.SysFont("kaiti", 100)
    else:
        my_font = pygame.font.SysFont("kaitif", 100)
    tnts = Group()

    # init bgm
    if set_music is not None:
        pygame.mixer.music.load(f"game_music/background/{set_music}")
        pygame.mixer.music.play(-1)

    # init window
    screen = pygame.display.set_mode((settings.width, settings.height))
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
    magic = Magic(screen)
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
        nhard = int((nowrec + 20 - start_rec) / (19 + int(hard / 2)))
        if nhard > hard:
            hard = nhard
        tntw = int(nowrec + 140 - start_rec) / (hard * 80)
        steve_tnt = False
        if random.randint(1, 10) == 5:
            steve_tnt = True
        sb = Scoreboard(screen, gs, hard)
        cool_down = CoolDown(screen, steve)
        steve.speed = hard * 0.5
        if t2 - t1 > tntw:
            if tnt_num < 10:
                tnt_num += 1
                new_tnt = TNT(screen)
                new_tnt.speed += hard * 0.1
                if steve_tnt:
                    new_tnt.rect.centerx = steve.rect.centerx
                tnts.add(new_tnt)
                t1 = t2

        func_return = gf.check_events(steve, start_rec, screen, my_font, hard, ele_time)
        start_rec = func_return[0]
        ele_time = func_return[1]
        steve.update()

        tnts.update()
        gf.kick_minus(steve)
        gf.check_kick(steve, hard)
        steve.magic = gf.magic_return(steve.magic, hard)
        steve.speed = gf.speed_check(steve, hard)
        ctcsl = gf.check_tnt_c_steve(tnts, steve, heal, tnt_num, screen, gs.score, hard, steve.magic)
        heal = ctcsl[0]
        tnt_num = ctcsl[1]
        gs.score = ctcsl[2]
        steve.magic = ctcsl[3]
        gf.check_die(heal, gs.score, hard, ele_time, start_rec, nowrec)
        for tnt in tnts.copy():
            if tnt.rect.top >= screen_rect.bottom:
                tnt_num -= 1
                tnts.remove(tnt)
                gs.score += hard
        gf.update_screen(screen, steve, tnts, sb, h1, h2, h3, cool_down, magic, hard, heal)


data_for_game = launcher()
skin = data_for_game[0]
frame = data_for_game[1]
set_music = data_for_game[2]

run_game(frame, set_music)
