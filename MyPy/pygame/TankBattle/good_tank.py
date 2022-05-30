# 我方坦克
class HeroTank(BaseTank):
    def __init__(self, left, top):
        super().__init__(left, top)

    # 我方坦克碰撞敌方坦克
    def myTank_hit_enemyTank(self):
        for enemyTank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                self.stay()
