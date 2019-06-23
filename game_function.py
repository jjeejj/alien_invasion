# 飞船动作的函数
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

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
    elif event.key == pygame.K_q: # q键退出
        sys.exit()

'''键盘抬起事件处理'''
def check_keyup_events(event, ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets, aliens):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitem()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets, aliens, ai_settings, screen, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    # 检查是否击中外星人
    check_bullet_alien_collisions(ai_settings, screen, aliens, bullets, ship)

def check_bullet_alien_collisions(ai_settings, screen, aliens, bullets, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 判断是否还存在外星人，不存在就重新创建
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组 bullets 中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    '''计算每行可容纳多少个外星人'''
    print('alien_width', alien_width)
    print('ai_settings.screen_width', ai_settings.screen_width)
    # 屏幕可用的宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 外星人的最大数据
    number_aliens_x = int(available_space_x / (2 * alien_width))
    print('number_aliens_x', number_aliens_x)
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = ai_settings.screen_heght - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''''创建一个外星人并将其放在当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_number * 2 * alien_width
    alien.y = alien.rect.height + row_number * 2 * alien.rect.height
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    '''创建外星人人群'''
    # 创建一个外星人，并计算一行可以容纳几个，外星人的间距为外行星的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, alien_width, ship.rect.height)

    for row_number in  range(number_rows):
        # 创建一行外星人，并放到行指定的位置
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    '''有外星人到达边缘时采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变它们的方向'''
    for alien in aliens.sprites():
        alien.y += ai_settings.fleet_drop_speed
        alien.rect.y = alien.y
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, aliens, bullets, ship, stats):
    '''更新外星人群中所有外星人的位置'''
    # 外星人检查
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检查是否碰撞了
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, aliens, bullets, ship)
    check_aliens_bottom(ai_settings, screen, aliens, bullets, stats, ship)
            

def check_aliens_bottom(ai_settings, screen, aliens, bullets, stats, ship):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
             ship_hit(ai_settings, screen, stats, aliens, bullets, ship)

def ship_hit(ai_settings, screen, stats, aliens, bullets, ship):
    if stats.ships_left > 0:
        stats.ships_left -=1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        sleep(2)
    else:
        stats.game_active = False
        print('game over')

