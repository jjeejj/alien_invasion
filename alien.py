# 外星人类
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图片，并设置rect属性
        self.image = pygame.image.load('./images/alien.bmp')
        # self.image_rect = self.image.get_rect()
        # self.image_scale = pygame.transform.scale(self.image, 
        #     (self.image_rect.width / 2, self.image_rect.height / 2 ))
        self.rect = self.image.get_rect()
        # self.rect.width = self.image_rect.width / 2
        # self.rect.height = self.image_rect.height / 2 

        # 设置每个外星人初始都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 保存外星人准确的位置
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        '''更新在屏幕上坐标'''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回 True'''
        if self.rect.right >= self.ai_settings.screen_width:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
        
    def blitem(self):
        '''在屏幕上绘制'''
        self.screen.blit(self.image, self.rect)

