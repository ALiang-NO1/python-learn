# 爆炸类
class Explode:
    def __init__(self, tank):
        # 爆炸的位置由坦克决定
        self.rect = tank.rect
        self.images = [
            pygame.image.load('tank_img/blast0.gif'),
            pygame.image.load('tank_img/blast1.gif'),
            pygame.image.load('tank_img/blast2.gif'),
            pygame.image.load('tank_img/blast3.gif'),
            pygame.image.load('tank_img/blast4.gif'),
            pygame.image.load('tank_img/blast5.gif'),
            pygame.image.load('tank_img/blast6.gif'),
            pygame.image.load('tank_img/blast7.gif')
        ]
        self.step = 0
        self.image = self.images[self.step]
        self.live = True

    # 加载爆炸类
    def displayExplode(self):
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.step += 1
            MainGame.window.blit(self.image, self.rect)
        else:
            self.live = False
            self.step = 0
