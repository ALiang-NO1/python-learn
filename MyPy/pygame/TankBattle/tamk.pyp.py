# 坦克父类
class BaseTank(BaseItem):
    # 定义类属性，所有坦克对象高和宽都是一样
    width = 60
    height = 60

    def __init__(self, left, top):
        self.direction = 'U'  # 坦克的方向默认向上
        # 存放图片的字典
        self.images = {
            'U': pygame.image.load('tank_img/p1tankU.gif'),
            'D': pygame.image.load('tank_img/p1tankD.gif'),
            'L': pygame.image.load('tank_img/p1tankL.gif'),
            'R': pygame.image.load('tank_img/p1tankR.gif')
        }
        self.image = self.images[self.direction]  # 坦克的图片由方向决定
        self.speed = 5  # 坦克的速度
        self.rect = self.image.get_rect()
        # 设置放置的位置
        self.rect.left = left
        self.rect.top = top
        self.stop = True  # 坦克是否停止
        self.live = True  # 决定坦克是否消灭了

        # 保持原来的位置
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 射击方法
    def shot(self):
        return Bullet(self)

    # 坦克的移动
    def move(self):
        # 保持原来的状态
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        # 判断坦克的移动方向
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WINDOW_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < WINDOW_WIDTH:
                self.rect.left += self.speed

    # 加载坦克
    def displayTank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image, self.rect)

    # 撞墙处理
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(wall, self):
                self.stay()

    # 处理位置不变
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
