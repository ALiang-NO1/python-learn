import pygame

class Ship:
    def __init__(self, screen, ai_settings):
        """初始化飞船及其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.image = pygame.transform.smoothscale(self.image, (40, 60))
        self.rect = self.image.get_rect()   # 获取飞船的外界矩形
        self.screen_rect = self.screen.get_rect()     # 获取屏幕的矩形区
        # 每艘飞船都放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx    # 飞船矩形中央就是屏幕矩形中央
        self.rect.bottom = self.screen_rect.bottom      # 飞船矩形的底就是屏幕的底

        self.center = float(self.rect.centerx)      # 在center中储存飞船的中心位置

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:      # 右移动为True，飞船未超出右边界
            self.center += self.ai_settings.ship_speed_factor   # 飞船x坐标加上左右移速
        if self.moving_left and self.rect.left > 0:     # 左移为True且未超出屏幕左边
            self.center -= self.ai_settings.ship_speed_factor   # 飞船x坐标减去左右移速

        self.rect.centerx = self.center     # 将飞船初始x位置调整为移动后的位置

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕中央显示"""
        self.center = self.screen_rect.centerx