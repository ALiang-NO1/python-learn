class Settings:
    """储存《外星人入侵》的所有设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     # 初始化背景色，(R, G, B)，此处为浅灰色
        self.ship_speed_factor = 1.5    # 飞船的速度
        self.ship_limit = 3     # 飞船数量限制
        self.ship_image_path = 'images/ship.bmp'  # 飞船图片路径
        self.alien_speed_factor =1      # 外星人的速度限制
        self.fleet_drop_speed = 10      # 外星人下落速度
        self.fleet_direction = 1    # 用数字表示外星人方向

        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60   # 深灰
        self.bullets_allowed = 3    # 限制子弹的个数

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置,外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)