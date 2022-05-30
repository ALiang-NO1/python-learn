# 墙壁类
class Wall:
    def __init__(self, left, top):
        self.image = pygame.image.load('tank_img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hg = 100000000000000

    # 加载墙壁
    def displayWall(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)
