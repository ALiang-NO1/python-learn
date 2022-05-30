# 游戏类
class MainGame:
    # 类属性
    window = None
    my_tank = None

    # 敌方坦克初始化
    EnemyTankList = []
    EnemyTankCount = 5

    # 存储我方子弹列表
    myBulleList = []
    # 存储敌方子弹的列表
    EnemyBulletList = []

    # 创建爆炸对象列表
    explodeList = []

    # 创建墙壁列表
    wallList = []

    # 游戏开始方法
    def start_game(self):
        # 初始化展示模块
        pygame.display.init()
        # 调用创建窗口的方法
        self.creat_window()
        # 设置游戏窗口标题
        pygame.display.set_caption('坦克大战')
        # 初始化我方坦克
        self.createMyTank()
        # 初始化敌方坦克
        self.creatEnemyTank()
        # 初始化墙壁
        self.creatWall()

        # 程序持续进行
        while True:
            # 更改背景颜色
            MainGame.window.fill(COLOR_GREEN)
            # 背景音乐

            # 获取事件
            self.getEvent()
            # 调用我方坦克进行显示
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    MainGame.my_tank.hitWall()
                    MainGame.my_tank.myTank_hit_enemyTank()
            else:
                del MainGame.my_tank
                MainGame.my_tank = None
            # 加载我方子弹
            self.biltMyBullet()
            # 显示敌方坦克
            self.biltEnemyTank()
            # 显示敌方子弹
            self.biltEnemyBullet()
            # 显示墙壁
            self.blitWall()
            # 显示爆炸效果
            self.blitExplode()

            self.put_more_enemytank()

            # 窗口持续刷新
            pygame.display.update()
            time.sleep(0.02)

    # 重复添加敌方坦克
    def put_more_enemytank(self):
        while len(MainGame.EnemyTankList) < 5:
            self.more()

    # 创建游戏窗口方法：
    def creat_window(self):
        if not MainGame.window:
            # 创建窗口
            MainGame.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        return MainGame.window

    # 创建我方坦克
    def createMyTank(self):
        MainGame.my_tank = HeroTank((WINDOW_WIDTH - HeroTank.width)/2, WINDOW_HEIGHT - HeroTank.height)
        music = Music('tank_img/start.wav')
        music.play()

    # 创建墙壁
    def creatWall(self):
        for i in range(60, WINDOW_WIDTH, 60):
            top = WINDOW_WIDTH // 3
            left = i
            wall = Wall(left, top)
            MainGame.wallList.append(wall)

    # 显示墙壁
    def blitWall(self):
        for b in MainGame.wallList:
            if b.live:
                b.displayWall()
            else:
                MainGame.wallList.remove(b)

    # 加载我方子弹
    def biltMyBullet(self):
        for bullet in MainGame.myBulleList:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
                bullet.myBullet_hit_enemy()
                bullet.wall_bullet()
            else:
                MainGame.myBulleList.remove(bullet)

    # 后续坦克的添加
    def more(self):
        top = 0
        for i in range(5 - len(MainGame.EnemyTankList)):
            left = random.randint(0, 750)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.EnemyTankList.append(enemy)

    # 创建敌方坦克
    def creatEnemyTank(self):
        top = 0
        for i in range(MainGame.EnemyTankCount):
            left = random.randint(0, 750)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.EnemyTankList.append(enemy)

    # 循环遍历显示敌方坦克
    def biltEnemyTank(self):
        for enemytank in MainGame.EnemyTankList:
            if enemytank.live:
                enemytank.displayTank()
                EnemyBullet = enemytank.shot()
                enemytank.randomMove()
                enemytank.hitWall()
                enemytank.enemyTank_hit_MyTank()

                # 存储敌方子弹
                if EnemyBullet:
                    MainGame.EnemyBulletList.append(EnemyBullet)
            else:
                MainGame.EnemyTankList.remove(enemytank)
                MainGame.EnemyTankCount -= 1

    # 加载敌方子弹
    def biltEnemyBullet(self):
        for bullet in MainGame.EnemyBulletList:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
                bullet.enemyBullet_hit_myTank()
                bullet.wall_bullet()

            else:
                MainGame.EnemyBulletList.remove(bullet)

    # 加载爆炸效果
    def blitExplode(self):
        for explode in MainGame.explodeList:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.explodeList.remove(explode)

    # 获取游戏中的所有事件
    def getEvent(self):
        # 获取游戏中的事件列表
        even_list = pygame.event.get()
        for e in even_list:
            # 点击窗口的叉号实现游戏结束
            if e.type == pygame.QUIT:
                sys.exit()

            # 通过上下左右键控制坦克的移动
            if e.type == pygame.KEYDOWN:
                if MainGame.my_tank and MainGame.my_tank.live:
                    if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.stop = False
                        print("按下向下的键，向下移动")
                    elif e.key == pygame.K_UP or e.key == pygame.K_w:
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.stop = False
                        print("按下向上的键，向上移动")
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        MainGame.my_tank.direction = 'L'
                        MainGame.my_tank.stop = False
                        print("按下向左的键，向左移动")
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.stop = False
                        print("按下向右的键，向右移动")

                    elif e.key == pygame.K_SPACE:
                        print('发射子弹')
                        # 创建我方子弹
                        if len(MainGame.myBulleList) < 10:
                            mybullet = Bullet(MainGame.my_tank)
                            MainGame.myBulleList.append(mybullet)

                            # 射击音效
                            Shot_music = Music('tank_img/fire.wav')
                            Shot_music.play()

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN or e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                        or e.key == pygame.K_w or e.key == pygame.K_s or e.key == pygame.K_a or e.key == pygame.K_d:
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = True
