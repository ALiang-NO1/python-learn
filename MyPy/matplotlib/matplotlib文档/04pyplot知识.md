# TL；DR
- Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。
- Pyplot 是常用的绘图模块，能很方便让用户绘制 2D 图表。
- Pyplot 包含一系列绘图函数的相关函数，每个函数会对当前的图像进行一些修改，例如：给图像加上标记，生新的图像，在图像中产生新的绘图区域等等。

# plot函数
plot() 函数是绘制二维图形的最基本函数，它可以绘制点和线
> plot([x], y, [fmt], *, data=None, **kwargs)# 画单条线
> plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)# 画多条线

## 参数说明
- x, y：点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。
- fmt：可选，定义基本格式（如颜色、标记和线条样式）。例如 o:r，o 表示实心圆标记，: 表示虚线，r 表示颜色为红色。
- **kwargs：可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。

```py
>>> plot(x, y)        # 创建 y 中数据与 x 中对应值的二维线图，使用默认样式
>>> plot(x, y, 'bo')  # 创建 y 中数据与 x 中对应值的二维线图，使用蓝色实心圈绘制
>>> plot(y)           # x 的值为 0..N-1
>>> plot(y, 'r+')     # 使用红色 + 号
```

### fmt参数说明
- 颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。
- 线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
- 标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。
```py
rng=np.random.RandomState(0)
for marker in ['o','.','x','+','^','v','<','>','s','d']:
    plt.plot(rng.rand(5), rng.rand(5), marker, label='marker=%s' % marker)
plt.legend(numpoints=1)
plt.xlim(0)
```

### 标记大小与颜色
- markersize，简写为 ms：定义标记的大小。
- markerfacecolor，简写为 mfc：定义标记内部的颜色。
- markeredgecolor，简写为 mec：定义标记边框的颜色。

如果我们只想绘制两个坐标点，而不是一条线，可以使用 o 参数，表示一个实心圈的标记：
```py
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, marker='o', ms=10, mec='r')  # 绘制坐标 (1, 3) 和 (8, 10) 的两个点
plt.show()
```
我们也可以绘制任意数量的点，只需**确保两个轴上的点数相同**即可。


### 线类型
线的类型可以使用 linestyle 参数来定义，简写为 ls
```py
plt.plot(ypoints, linestyle = 'dotted')
plt.plot(ypoints, ls = '-.')
```

### 线颜色
线的颜色可以使用 color 参数来定义，简写为 c。
```py
plt.plot(ypoints, color = 'r')
plt.plot(ypoints, c = '#8FBC8F')
plt.plot(ypoints, c = 'SeaGreen')
```

### 线宽度
线的宽度可以使用 linewidth 参数来定义，简写为 lw，值可以是浮点数，如：1、2.0、5.67 等。


# Matplotlib 轴标签和标题
- 我们可以使用 xlabel() 和 ylabel() 方法来设置 x 轴和 y 轴的标签。
```py
plt.xlabel("x - label")
plt.ylabel("y - label")
```

- 我们可以使用 title() 方法来设置标题。
```py
plt.title("RUNOOB TEST TITLE")
```

## 图形中文显示
Matplotlib 默认情况不支持中文，这里我们使用思源黑体，思源黑体是 Adobe 与 Google 推出的一款开源字体。
- 官网：https://source.typekit.com/source-han-serif/cn/
- GitHub 地址：https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese
- 网盘下载: https://pan.baidu.com/s/14cRhgYvvYotVIFkRVd71fQ。

## 自定义字体
```py
# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径，size 参数设置字体大小
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf", size=18)
font1 = {'color':'blue','size':20}
font2 = {'color':'darkred','size':15}
x = np.arange(1,11)
y =  2  * x +  5

# fontdict 可以使用 css 来设置字体样式
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1, fontdict = font1)
 
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.plot(x,y)
plt.show()
```

## 添加 loc 参数设置文字位置
值可以为 left|right|center(默认)
```py
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1, fontdict = font1, loc="left")
plt.xlabel("x 轴", fontproperties=zhfont1, loc="left")
plt.ylabel("y 轴", fontproperties=zhfont1, loc="top")
```


# Matplotlib 网格线
我们可以使用 pyplot 中的 grid() 方法来设置图表中的网格线。
> matplotlib.pyplot.grid(b=None, which='major', axis='both', )

## 参数说明
- b：可选，默认为 None，可以设置布尔值，true 为显示网格线，false 为不显示，如果设置 **kwargs 参数，则值为 true。
- which：可选，可选值有 'major'、'minor' 和 'both'，默认为 'major'，表示应用更改的网格线。
- axis：可选，设置显示哪个方向的网格线，可以是取 'both'（默认），'x' 或 'y'，分别表示两个方向，x 轴方向或 y 轴方向。- 
- **kwargs：可选，设置网格样式，可以是 color='r', linestyle='-' 和 linewidth=2，分别表示网格线的颜色，样式和宽度。
```plt.grid(axis='x') # 设置 y 就在轴方向显示网格线```

添加一个简单的网格线，并设置网格线的样式，格式如下：
> grid(color = 'color', linestyle = 'linestyle', linewidth = number)

## 线样式参数说明：
- color：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。
- linestyle：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
- linewidth：设置线的宽度，可以设置一个数字。


# Matplotlib 绘制多图
我们可以使用 pyplot 中的 subplot() 和 subplots() 方法来绘制多个子图。

subpot() 方法在绘图时需要指定位置，subplots() 方法可以一次生成多个，在调用时只需要调用生成对象的 ax 即可。

> subplot(nrows, ncols, index, **kwargs)
> subplot(pos, **kwargs)
> subplot(**kwargs)
> subplot(ax)
以上函数将整个绘图区域分成 nrows 行和 ncols 列，然后从左到右，从上到下的顺序对每个子区域进行编号 1...N ，左上的子区域的编号为 1、右下的区域编号为 N，编号可以通过参数 index 来设置。

设置 numRows ＝ 1，numCols ＝ 2，就是将图表绘制成 1x2 的图片区域, 对应的坐标为：(1, 1), (1, 2)
plotNum ＝ 1, 表示的坐标为(1, 1), 即第一行第一列的子图。
plotNum ＝ 2, 表示的坐标为(1, 2), 即第一行第二列的子图。

```py
#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

#plot 3:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("plot 3")

#plot 4:
x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("plot 4")

plt.suptitle("RUNOOB subplot Test")
plt.show()
```

## subplots()
> subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)

- nrows：默认为 1，设置图表的行数。
- ncols：默认为 1，设置图表的列数。
- sharex、sharey：设置 x、y 轴是否共享属性，默认为 false，可设置为 'none'、'all'、'row' 或 'col'。 
  + False 或 none 每个子图的 x 轴或 y 轴都是独立的，
  + True 或 'all'：所有子图共享 x 轴或 y 轴，
  + 'row' 设置每个子图行共享一个 x 轴或 y 轴，
  + 'col'：设置每个子图列共享一个 x 轴或 y 轴。
- squeeze：布尔值，默认为 True，表示额外的维度从返回的 Axes(轴)对象中挤出，
  + 对于 N*1 或 1*N 个子图，返回一个 1 维数组，
  + 对于 N*M，N>1 和 M>1 返回一个 2 维数组。
  + 如果设置为 False，则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1。
- subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
- gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
- **fig_kw：把详细的关键字参数传给 figure() 函数。

```py
# 创建一些测试数据 -- 图1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 创建一个画像和子图 -- 图2
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# 创建两个子图 -- 图3
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# 创建四个子图 -- 图4
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# 共享 x 轴
plt.subplots(2, 2, sharex='col')

# 共享 y 轴
plt.subplots(2, 2, sharey='row')

# 共享 x 轴和 y 轴
plt.subplots(2, 2, sharex='all', sharey='all')

# 这个也是共享 x 轴和 y 轴
plt.subplots(2, 2, sharex=True, sharey=True)

# 创建10 张图，已经存在的则删除
fig, ax = plt.subplots(num=10, clear=True)

plt.show()
```


# Matplotlib 散点图
我们可以使用 pyplot 中的 scatter() 方法来绘制散点图。
> scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

## 参数说明
- x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。
- s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
- c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
- marker：点的样式，默认小圆圈 'o'。
- cmap：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。
- norm：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。
- vmin，vmax：：亮度设置，在 norm 参数存在时会忽略。
- alpha：：透明度设置，0-1 之间，默认 None，即不透明。
- linewidths：：标记点的长度。
- edgecolors：：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。
- plotnonfinite：：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。
- **kwargs：：其他参数。

```py
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
plt.scatter(x, y)
plt.show()
```

## 设置尺寸
sizes = np.array([20,50,100,200,500,1000,60,90])置标记尺寸
```plt.scatter(x, y, s=sizes)```

## 设置标记颜色
```py
colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
plt.scatter(x, y, c=colors)
```

## 绘制两组散点图
```py
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
```

## 随机散点图
```py
# 随机数生成器的种子
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 设置颜色及透明度
plt.title("RUNOOB Scatter Test") # 设置标题
plt.show()
```

## 颜色条 Colormap
- Matplotlib 模块提供了很多可用的颜色条。
- 颜色条就像一个颜色列表，其中每种颜色都有一个范围从 0 到 100 的值。
- 设置颜色条需要使用 cmap 参数，默认值为 'viridis'，之后颜色值设置为 0 到 100 的数组。
```py
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')  # 或者afmhot_r等
plt.colorbar()  # 显示颜色条
plt.show()
```


# Matplotlib 柱形图
我们可以使用 pyplot 中的 bar() 方法来绘制柱形图。
> matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)

## 参数说明：
- x：浮点型数组，柱形图的 x 轴数据。
- height：浮点型数组，柱形图的高度。
- width：浮点型数组，柱形图的宽度。
- bottom：浮点型数组，底座的 y 坐标，默认 0。
- align：柱形图与 x 坐标的对齐方式，
  + 'center' 以 x 位置为中心，这是默认值。 
  + 'edge'：将柱形图的左边缘与 x 位置对齐
  + 要对齐右边缘的条形，可以传递负数的宽度值及 align='edge'。
- **kwargs：：其他参数。

```py
x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])
plt.bar(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"])
plt.show()
```

## 横线柱状图
垂直方向的柱形图可以使用 barh() 方法来设置
```plt.barh(x,y)```

## 设置柱子宽度
设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height
```plt.bar(x, y, width = 0.1)```


# Matplotlib 饼图
我们可以使用 pyplot 中的 pie() 方法来绘制散点图。
> matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]

## 参数说明：
- x：浮点型数组，表示每个扇形的面积。
- explode：数组，表示各个扇形之间的间隔，默认值为0。
- labels：列表，各个扇形的标签，默认值为 None。
- colors：数组，表示各个扇形的颜色，默认值为 None。
- autopct：设置饼图内各个扇形百分比显示格式，%d%% 整数百分比，%0.1f 一位小数， %0.1f%% 一位小数百分比， %0.2f%% 两位小数百分比。
- labeldistance：标签标记的绘制位置，相对于半径的比例，默认值为 1.1，如 <1则绘制在饼图内侧。
- pctdistance：：类似于 labeldistance，指定 autopct 的位置刻度，默认值为 0.6。
- shadow：：布尔值 True 或 False，设置饼图的阴影，默认为 False，不设置阴影。
- radius：：设置饼图的半径，默认为 1。
- startangle：：起始绘制饼图的角度，默认为从 x 轴正方向逆时针画起，如设定 =90 则从 y 轴正方向画起。
- counterclock：布尔值，设置指针方向，默认为 True，即逆时针，False 为顺时针。
- wedgeprops ：字典类型，默认值 None。参数字典传递给 wedge 对象用来画一个饼图。例如：wedgeprops={'linewidth':5} 设置 wedge 线宽为5。
- textprops ：字典类型，默认值为：None。传递给 text 对象的字典参数，用于设置标签（labels）和比例文字的格式。
- center ：浮点类型的列表，默认值：(0,0)。用于设置图标中心位置。
- frame ：布尔类型，默认值：False。如果是 True，绘制带有表的轴框架。
- rotatelabels ：布尔类型，默认为 False。如果为 True，旋转每个 label 到指定的角度。

```py
y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%', # 格式化输出百分比
       )
plt.title("RUNOOB Pie Test")
plt.show()
```
**注意**：默认情况下，第一个扇形的绘制是从 x 轴开始并逆时针移动
