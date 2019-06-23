# 飞船类
import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新的飞船放到屏幕的底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志位
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)
    
    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right:
            # 防止移动后跑到屏幕外面
            if self.rect.right + self.ai_settings.ship_speed_factor >= self.screen_rect.right:
                self.center = self.screen_rect.right - self.rect.width
            else:
                self.center += self.ai_settings.ship_speed_factor

        if self.moving_left:
            if self.rect.left - self.ai_settings.ship_speed_factor <= self.screen_rect.left:
                    self.center = self.screen_rect.left + self.rect.width
            else:
                self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    
    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
        self.rect.centerx = self.center

    def blitem(self):
        self.screen.blit(self.image, self.rect)