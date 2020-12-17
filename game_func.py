import time

import pygame
from Steve import use_totem
from game_stats import GameStats
from launcher import die

game_stats = GameStats()


def check_events(steve, start_rec, screen, my_font, hard, ele_time):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move steve right
                steve.RF = True
            if event.key == pygame.K_LEFT:
                # move steve left
                steve.LF = True
            if event.key == pygame.K_p:
                pygame.mouse.set_visible(True)
                steve.LF = False
                steve.RF = False
                p1 = time.time()
                breaking = False
                while True:
                    if breaking:
                        break
                    screen.fill((0, 0, 0))
                    text = my_font.render("暂停", True, (255, 255, 255))
                    screen.blit(text, (500, 260))
                    e = pygame.event.get()
                    for ev in e:
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_p:
                                pygame.mouse.set_visible(False)
                                p2 = time.time()
                                start_rec += p2 - p1
                                breaking = True
                        elif ev.type == pygame.QUIT:
                            exit()
                    pygame.display.flip()
                time.sleep(1)
            if event.key == pygame.K_SPACE and steve.cool_down <= 0 and steve.magic >= int(hard / 3 + 1) * 40:
                steve.kick = True
                ka = int(hard / 5) + 1
                steve.kicking = 2 * ka
                steve.kick_start = time.time()
                ele_time += 1
                steve.magic -= int(hard / 3 + 1) * 40
                game_stats.mg_tick = time.time()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # stop moving right
                steve.RF = False
            if event.key == pygame.K_LEFT:
                # stop moving left
                steve.LF = False
    return start_rec, ele_time


def update_screen(screen, steve, tnts, sb, h1, h2, h3, cool_down, magic, hard, heal):
    screen.fill((255, 255, 255))

    # blit steve
    steve.blitme()
    
    # blit all tnts
    for tnt in tnts.sprites():
        tnt.blitme()

    # blit heal instruction
    h1.blitme()
    h2.blitme()
    h3.blitme()

    # blit scoreboard
    sb.blitme()

    # blit cool_down
    cool_down.blitme_c()
    cool_down.blitme_a()

    # blit magic
    magic.blitme(steve.magic, hard, heal)

    font = pygame.font.SysFont(None, 20)
    mxm = hard * 50
    if mxm < 100:
        mxm = 100
    word_img = font.render(f"{steve.magic}/{mxm}  +{(int(0.2 * hard) + 1) * 2}/s", True, (0, 100, 255))
    if heal != 0:
        screen.blit(word_img, (0, 83))
    else:
        screen.blit(word_img, (0, 25))

    # update screen
    pygame.display.flip()


def check_tnt_c_steve(tnts, steve, heal, tnt_num, screen, score, hard):
    if pygame.sprite.spritecollideany(steve, tnts):
        if steve.kick is False:
            heal -= 1
            use_totem(screen, steve, heal)
            for tnt in tnts:
                tnts.remove(tnt)
                explode_img = pygame.image.load("explosion.png")
                img = pygame.transform.scale(explode_img, (180, 180))
                screen.blit(img, (tnt.rect.x, tnt.rect.y))
                pygame.display.flip()
                time.sleep(0.1)
                tnt_num = 0
        else:
            for tnt in tnts:
                if tnt.rect.colliderect(steve):
                    tnts.remove(tnt)
                    tnt_num -= 1
                    score += hard * 2
                    break
    return heal, tnt_num, score


def check_die(heal, score, hard, ele_time, start_rec, now_rec):
    if heal < 0:
        pygame.quit()
        return die(score, hard, ele_time, start_rec, now_rec)
    return None


def check_kick(steve, hard):
    if steve.kick:
        if steve.kicking <= 0:
            steve.kick = False
            ncd = 16 - hard
            if ncd < 3:
                ncd = 3
            steve.cool_down = ncd
            steve.kick_start = None
        else:
            pass
    else:
        pass


def kick_minus(steve):
    if steve.kick:
        if time.time() - steve.kick_start >= 1:
            steve.kicking -= 1
            steve.kick_start = time.time()
    if time.time() - game_stats.tick >= 1:
        steve.cool_down -= 1
        game_stats.tick = time.time()


def speed_check(steve, hard) -> int:
    original_speed = 0.6 + (0.4 + ((hard - 1) * 0.4 + 0.4) * hard / 2)
    if steve.kick:
        steve.speed = original_speed * 1.5
    else:
        steve.speed = original_speed
    return steve.speed


def magic_return(magic: int, hard: int) -> int:
    max_magic = hard * 50
    if max_magic < 100:
        max_magic = 100
    if time.time() - game_stats.mg_tick >= 0.2 and magic < max_magic:
        magic += int(0.2 * hard) + 1
        game_stats.mg_tick = time.time()
        if magic > max_magic:
            magic = max_magic
    return magic
