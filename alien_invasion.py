import sys
import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_ganme():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heght))
    pygame.display.set_caption('Alien invastion')
    ship = Ship(screen)
    # 设置背景颜色
    # bg_color = (230, 230, 230)

    # 开始游戏
    while True:
        # 监听键盘和鼠标事件
        gf.check_events()
        
        gf.update_screen(ai_settings, screen, ship)

run_ganme()