import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船发射的子弹进行管理"""
    def __init__(self, ai_setting, screen, ship):
        """在飞船的位置建立一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        # (0,0)处设置子弹矩形，再设置其正确位置
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        self.top = float(self.rect.y)    # 储存用小数表示的飞船的位置
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullt_speed_factor

    def update(self, *args):
        """向上移动子弹"""
        self.top -= self.speed_factor      # 更新表示子弹的最小数值
        self.rect.top = self.top    # 更新表示子弹的矩形位置
        print(self.rect.top)

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
