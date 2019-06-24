# 设置类
class Settings():
    '''保存设置信息'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        self.screen_width = 850
        self.screen_heght = 600
        self.bg_color = (230, 230, 230)
        # 玩家飞船数量设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # 外星人设置
        ## 外星人移动速度
        self.fleet_drop_speed = 5

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.fleet_direction = 1 # 1表示向右移，为-1表示向左移
        self.ship_speed_factor = 5.3 # 移动步长
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 1

    def increase_speedO(self):
        '''提高速度设置'''
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale