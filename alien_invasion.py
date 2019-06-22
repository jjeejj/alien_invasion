import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
# from bullet import Bullet
import game_function as gf

def run_ganme():

    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heght))
    pygame.display.set_caption('Alien invastion')
    ship = Ship(ai_settings, screen)
#     bullet = Bullet(ai_settings, screen, ship)
    '''创建一个用于存储子弹的编组'''
    bullets = Group()

    # 开始游戏
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # 子弹
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_ganme()