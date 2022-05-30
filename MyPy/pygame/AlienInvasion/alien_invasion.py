import pygame as pg
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import Gamestats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    """初始化游戏游戏并创建一个游戏对象"""
    pg.init()   # 初始化背景设置
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   # 创建屏幕显示窗口
    pg.display.set_caption('Alien Invasion')
    # 创建play按钮
    play_button = Button(ai_settings, screen, 'Play')
    # 创建一个用于储存游戏信息的事例,并创建记分牌
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)    # 创建一艘飞船
    bullets = Group()   # 创建一个用于管理子弹的编组
    aliens = Group()      # 创建一个外星人编组
    gf.create_fleet(ai_settings, screen, ship, aliens)    # 创建一群外星人

    # 开始游戏循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()