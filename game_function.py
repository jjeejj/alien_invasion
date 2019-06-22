# 飞船动作的函数
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # # 按键
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # 按键松开
            check_keyup_events(event, ship)

'''键盘按下事件处理'''
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += ship.move_step # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # ship.rect.centerx -= ship.move_step # 飞船向左移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

'''键盘抬起事件处理'''
def check_keyup_events(event, ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitem()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组 bullets 中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
