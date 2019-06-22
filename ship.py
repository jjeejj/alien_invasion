# 飞船类
import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('./images/ship.bmp')
        self.imgage_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新的飞船放到屏幕的底部
        self.imgage_rect.centerx = self.screen_rect.centerx
        self.imgage_rect.bottom = self.screen_rect.bottom

    def blitem(self):
        self.screen.blit(self.image, self.imgage_rect)