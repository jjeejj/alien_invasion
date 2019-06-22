# 设置类
class Settings():
    '''保存设置信息'''
    def __init__(self):
        self.screen_width = 350
        self.screen_heght = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 5.3 # 移动步长

        # 子弹设置
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
