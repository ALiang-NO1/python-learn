# 子弹类
class Bullet(BaseItem):
    def __init__(self, tank):
        self.image = pygame.image.load('tank_img/tankmissile.gif')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        # 根据坦克方向，生成子弹位置
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2

        # 子弹的速度
        self.speed = 6
        # 子弹状态
        self.live = True

    # 加载子弹
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)

    # 子弹的移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WINDOW_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WINDOW_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False

    # 我方子弹击中敌方坦克
    def myBullet_hit_enemy(self):
        for enemytank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(enemytank, self):
                enemytank.live = False
                self.live = False

                # 创建爆炸对象
                explode = Explode(enemytank)
                MainGame.explodeList.append(explode)

    # 敌方坦克击中我方坦克
    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                MainGame.my_tank.live = False
                self.live = False

                # 创建爆炸对象
                explode = Explode(MainGame.my_tank)
                MainGame.explodeList.append(explode)

    # 射击墙壁
    def wall_bullet(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(wall, self):
                wall.hg -= 1
                self.live = False
                if wall.hg <= 0:
                    wall.live = False
