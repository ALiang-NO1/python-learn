import pygame, sys
from pygame.locals import QUIT

# 初始化pygame
pygame.init()
# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((500, 400))
# 设置窗口的标题
pygame.display.set_caption('Audio')
# 定义颜色
WHITE = (255, 255, 255)
# 设置背景
screen.fill(WHITE)

# 加载并播放一个特效音频文件
# sound = pygame.mixer.Sound('resources/bounce.ogg')
# sound.play()

# 加载背景音乐文件
pygame.mixer.music.load(r'E:\win10\Music\安琪拉.mp3')
# 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
pygame.mixer.music.play(-1, 0.0)

# 程序主循环
while True:
    # 获取事件
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == QUIT:
            # 停止播放背景音乐
            pygame.mixer.music.stop()
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()

    # 绘制屏幕内容
    pygame.display.update()
