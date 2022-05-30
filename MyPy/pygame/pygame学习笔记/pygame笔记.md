## 初始化
### 主循环
 - 处理事件
 - 更新游戏状态
 - 绘制游戏状态到屏幕上
handle events -> update game state -> draw screen -> handle events

## 绘制图形
Pygame的坐标原点（0，0）点位于左上角，X轴自左向右，Y轴自上向下，单位为像素。
### 绘图方法
 - pygame.draw.line(Surface, color, start_pos, end_pos, width)此方法用于绘制一条线段
 - pygame.draw.aaline(Surface, color, start_pos, end_pos, blend)此方法用于绘制一条抗锯齿的线
 - pygame.draw.lines(Surface, color, closed, pointlist, width)此方法用于绘制一条折线
 - pygame.draw.rect(Surface, color, Rect)此方法用于绘制一个矩形
 - pygame.draw.rect(Surface, color, Rect, width)此方法用于绘制一个矩形框
 - pygame.draw.ellipse(Surface, color, Rect)此方法用于绘制一个椭圆
 - pygame.draw.ellipse(Surface, color, Rect, width)此方法用于绘制一个椭圆框
 - pygame.draw.polygon(Surface, color, pointlist, width)此方法用于绘制一个多边形
 - pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width)此方法用于绘制一条弧线
 - pygame.draw.circle(Surface, color, Rect, radius)此方法用于绘制一个圆

## 动画
### 视觉暂留
人类眼睛的特殊生理结构，当所看画面的帧率高于24的时候，就会认为是连贯的，此现象称之为 视觉暂留
帧率（Frame rate）是用于测量显示帧数的量度，所谓的测量单位为每秒显示帧数(Frames per Second，简称：FPS）
一般来说30fps是可以接受的，但是将性能提升至60fps则可以明显提升交互感和逼真感，但是一般来说超过75fps一般就不容易察觉到有明显的流畅度提升了。

### 实现动画主要用到的方法
 - pygame.image.load(filename)加载一张图片
 - pygame.Surface.blit(source, dest, area=None, special_flags = 0)将图片绘制到屏幕相应坐标上（后面两个参数默认，可以不传）
 - pygame.time.Clock()获得pygame的时钟
 - pygame.time.Clock.tick(FPS)设置pygame时钟的间隔时间

## 绘制文字
Pygame提供了 .ttf 字体文件。
### 方法
pygame.font.Font(filename, size)
 - filename：字体文件的文件名；
 - size：字体的高height，单位为像素；

pygame.font.Font.render(text, antialias, color, background=None)
 - text：要显示的文字；
 - antialias： 是否抗锯齿；
 - color：字体颜色；
 - background：背景颜色（可选参数）；

.get_rect()
 - 获得一个对象的rect，以便于设置其坐标位置

## 播放音频
在Pygame里播放音频有两个方法，一个用来播放特效声音，一个用来播放背景音乐

### pygame.mixer.Sound(filename)
该方法返回一个Sound对象，调用它的.play( )方法，即可播放较短的音频文件（比如玩家受到伤害、收集到金币等）；

## pygame.mixer.music.load(filename)
该方法用来加载背景音乐，之后调用pygame.mixer.music.play( )方法就可以播放背景音乐（Pygame只允许加载一个背景音乐在同一个时刻）

## 事件
----|----|----

事件 | 产生途径 | 参数
QUIT|	用户按下关闭按钮|	none
ACTIVEEVENT	    | Pygame被激活或者隐藏	| gain, state
KEYDOWN	        | 键盘被按下	        | unicode, key, mod
KEYUP	        | 键盘被放开	        | key, mod
MOUSEMOTION	    | 鼠标移动	        | pos, rel, buttons
MOUSEBUTTONDOWN	| 鼠标按下	        | pos, button
MOUSEBUTTONUP	| 鼠标放开	        | pos, button
VIDEORESIZE	    | Pygame窗口缩放	    | size, w, h

### 



