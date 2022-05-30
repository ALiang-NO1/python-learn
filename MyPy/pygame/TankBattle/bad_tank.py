# 敌方坦克
class EnemyTank(BaseTank):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top)
        self.images = {
            'U': pygame.image.load('tank_img/enemy1U.gif'),
            'D': pygame.image.load('tank_img/enemy1D.gif'),
            'L': pygame.image.load('tank_img/enemy1L.gif'),
            'R': pygame.image.load('tank_img/enemy1R.gif')
        }

        self.direction = self.RandomDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.step = 60
        self.enemy_flag = False

    # 坦克出生随机方向
    def RandomDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        else:
            return 'R'

    # 坦克随机移动
    def randomMove(self):
        if self.step < 0:
            self.direction = self.RandomDirection()
            self.step = 60
        else:
            self.move()
            self.step -= 1

    # 坦克射击
    def shot(self):
        num = random.randint(1, 100)
        if num < 4:
            return Bullet(self)

    # 敌方坦克碰撞我方坦克
    def enemyTank_hit_MyTank(self):
        for enemy in MainGame.EnemyTankList:
            if MainGame.my_tank and MainGame.my_tank.live:
                if pygame.sprite.collide_rect(MainGame.my_tank, enemy):
                    self.stay()
