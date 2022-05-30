# 定义一个精灵类
class BaseItem(Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
