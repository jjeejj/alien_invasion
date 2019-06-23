import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
# from alien import Alien
# from bullet import Bullet
import game_function as gf
from game_stats import GameStats

def run_ganme():

    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heght))
    pygame.display.set_caption('Alien invastion')
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    # bullet = Bullet(ai_settings, screen, ship)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星群组
    aliens = Group()
    # 创建外星人人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 开始游戏
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            # 子弹
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            # 外星人
            gf.update_aliens(ai_settings, screen, aliens, bullets, ship, stats)
            gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_ganme()