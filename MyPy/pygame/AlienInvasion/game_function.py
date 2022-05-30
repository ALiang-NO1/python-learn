import sys, pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x, mouse_y):
    """玩家点击Plah按钮开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置计分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keyup_event(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_right = False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有到限制，就发射一颗颗子弹"""
    # 创建新子弹，并加入到编组bullets中
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕上的图像"""
    screen.fill(ai_settings.bg_color)   # 让屏幕填充背景颜色
    # 飞船和外星人后面重绘所有子弹
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()  # 不断刷新屏幕
    # 循环子弹组里面的元素，进行绘制 为空时不执行
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #显示得分
    sb.show_score()
    #如果游戏处于非活跃状态，就显示Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 显示最新屏幕，擦拭旧屏幕
    pygame.display.flip()
    # print('1')


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置， 并删除已经消失的子弹"""
    bullets.update()  # 更新子弹的位置
    # 删除已经消失的子弹
    for bullet in bullets.spites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应外星人和子弹的碰撞"""
    # 检查是否有子弹击中外星人，如果是，则删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
    check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人,加快游戏进度节奏
        bullets.empty()
        ai_settings.increase_speed()

    # 提高等级
    stats.level += 1
    sb.prep_level()

    create_fleet(ai_settings, screen, ship, aliens)

def update_ship(ship):
    ship.update()

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_apace_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_apace_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty(); bullets.empty()
        # 创建一群新外星人并将飞船放到飞船放到底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """检查是否有外星人到达屏幕边缘"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom <= screen_rect.bottom:
            # 像飞船被撞一样处理
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break


def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """检查是否有外星人到达屏幕边缘，然后更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
        print('Ship hit!!!')
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了新的最高纪录"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()