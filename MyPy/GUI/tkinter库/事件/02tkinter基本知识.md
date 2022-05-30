## （控件）
1. Button 按钮。类似标签,但提供额外的功能,例如鼠标掠过、按下、释放以及键盘操作/事件
2. Canvas 画布。提供绘图功能(直线、椭圆、多边形、矩形) ;可以包含图形或位图
3. Checkbutton 选择按钮。一组方框,可以选择其中的任意个(类似 HTML 中的 checkbox)
4. Entry 文本框。单行文字域,用来收集键盘输入(类似 HTML 中的 text)
5. Frame 框架。包含其他组件的纯容器
6. Label 标签。用来显示文字或图片
7. Listbox 列表框。一个选项列表,用户可以从中选择
8. Menu 菜单。点下菜单按钮后弹出的一个选项列表,用户可以从中选择
9. Menubutton 菜单按钮。用来包含菜单的组件(有下拉式、层叠式等等)
10. Message 消息框。类似于标签,但可以显示多行文本
11. Radiobutton 单选按钮。一组按钮,其中只有一个可被“按下” (类似 HTML 中的 radio)
12. Scale 进度条。线性“滑块”组件,可设定起始值和结束值,会显示当前位置的精确值
13. Scrollbar 滚动条。对其支持的组件(文本域、画布、列表框、文本框)提供滚动功能
14. Text 文本域。 多行文字区域,可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)
15. Toplevel 顶级。类似框架,但提供一个独立的窗口容器。
17. 其他：Combobox:下拉列表；Progressbar：进度条；Treeview 表格操作
**注意** 在Tkinter中窗口部件类没有分级；所有的窗口部件类在树中都是兄弟。

如果你在按钮中显示文本，那么这些选项将以文本的单位为定义按钮的尺寸。如果你替而代之显示图像，那么按钮的尺寸将是像素（或其它的屏幕单位）。

Button窗口部件支持标准的Tkinter窗口部件接口，加上下面的方法：
- flash()：频繁重画按钮，使其在活动和普通样式下切换。
- invoke()：调用与按钮相关联的命令。

下面的方法与你实现自己的按钮绑定有关：tkButtonDown(), tkButtonEnter(), tkButtonInvoke(), tkButtonLeave(), tkButtonUp()
这些方法可以用在定制事件绑定中，所有这些方法接收0个或多个形参。

Button窗口部件支持下面的选项：

activebackground, activeforeground
类型：颜色；
说明：当按钮被激活时所使用的颜色。

anchor
类型：常量；
说明：控制按钮上内容的位置。使用N, NE, E, SE, S, SW, W, NW, or CENTER这些值之一。默认值是CENTER。

background (bg), foreground (fg)
类型：颜色；
说明：按钮的颜色。默认值与特定平台相关。

bitmap
类型：位图；
说明：显示在窗口部件中的位图。如果image选项被指定了，则这个选项被忽略。下面的位图在所有平台上都有效：
error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, 和 warning.

后面附加的位图仅在 Macintosh 上有效：document, stationery, edition, application, accessory, folder, pfolder,
trash, floppy, ramdisk, cdrom, preferences, querydoc, stop, note, 和 caution.

你也可以从一个XBM文件中装载位图。只需要在XBM文件名前加一个前缀@,例如"@sample.xbm"。

borderwidth (bd)
类型：整数；
说明：按钮边框的宽度。默认值与特定平台相关。但通常是1或2像素。

command
类型：回调；
说明：当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对像。

cursor
类型：光标；
说明：当鼠标移动到按钮上时所显示的光标。

default
类型：常量；
说明：如果设置了，则按钮为默认按钮。注意这个语法在Tk 8.0b2中已改变。

disabledforeground
类型：颜色；
说明：当按钮无效时的颜色。

font
类型：字体；
说明：按钮所使用的字体。按钮只能包含一种字体的文本。

highlightbackground, highlightcolor
类型：颜色；
说明：控制焦点所在的高亮边框的颜色。当窗口部件获得焦点的时候，边框为highlightcolor所指定的颜色。
    否则边框为highlightbackground所指定的颜色。默认值由系统所定。

highlightthickness
类型：距离；
说明：控制焦点所在的高亮边框的宽度。默认值通常是1或2像素。

image
类型：图像；
说明：在部件中显示的图像。如果指定，则text和bitmap选项将被忽略。

justify
类型：常量；
说明：定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER。

padx, pady
类型：距离；
说明：指定文本或图像与按钮边框的间距。

relief
类型：常量；
说明：边框的装饰。通常按钮按下时是凹陷的，否则凸起。另外的可能取值有GROOVE, RIDGE, 和 FLAT。

state
类型：常量；
说明：按钮的状态：NORMAL, ACTIVE 或 DISABLED。默认值为NORMAL。

takefocus
类型：标志；
说明：表明用户可以Tab键来将焦点移到这个按钮上。默认值是一个空字符串，意思是如果按钮有按键绑定的话，它可以通过所绑定的按键来获得焦点。

text
类型：字符串；
说明：显示在按钮中的文本。文本可以是多行。如果bitmaps或image选项被使用，则text选项被忽略。

textvariable
类型：变量；
说明：与按钮相关的Tk变量（通常是一个字符串变量）。如果这个变量的值改变，那么按钮上的文本相应更新。

underline
类型：整数；
说明：在文本标签中哪个字符加下划线。默认值为1，意思是没有字符加下划线。

width, height
类型：距离；
说明：按钮的尺寸。如果按钮显示文本，尺寸使用文本的单位。如果按钮显示图像，尺寸以像素为单位（或屏幕的单位）。如果尺寸没指定，它将根据按钮的内容来计算。

wraplength
类型：距离；
说明：确定一个按钮的文本何时调整为多行。它以屏幕的单位为单位。默认不调整。

Geometry(几何学)与mixins
一、实施 mixins
通过root窗口和窗口部件类，Misc类被用作mixin。它提供了大量的Tk和窗口相关服务，这些服务对所有Tkinter核心窗口部件者有效。
Wm类通过root窗口和顶级窗口部件类被用作mixin。通过委托它提供了窗口管理服务。

二、使用委托像这样简化你的应用程序代码：一旦你有一窗口部件，你能够使用这个窗口部件的实例的方法访问Tkinter的所有部分。
Grid,Pack,Place这些类通过窗口部件类被用作mixins。通过委托，它们也提供了访问不同几何管理的支持。
下面是Geometry Mixins的列表及说明：
Grid：grid几何管理器允许你通过在一个二维网格中组织窗口部件来创建一个类似表的版面。
Pack：pack几何管理器通过在一个帧中把窗口部件包装到一个父部件中来创建一个版面。
Place：place几何管理器让你显式将一个窗口部件放到给定的位置。

## 颜色名
- Tkinter 包括一个颜色数据库，它将颜色名映射到相应的RGB值。这个数据库包括了通常的名称如：Red, Green, Blue, Yellow, 和 LightBlue，也可使用外来的如Moccasin，PeachPuff等等。
- 在X window系统上，颜色名由X server定义。你能够找到一个名为xrgb.txt的文件，它包含了一个由颜色名和相应RGB值组成的列表。在Windows和Macintosh系统上，颜色名表内建于Tk中。
- 颜色名是大小写不敏感的。许多颜色名词与词之间有无格都有效。例如"lightblue", "light blue", 和"Light Blue"都是同一颜色。

- 在Windows下，你可以使用Windows系统颜色（用户可以通过控制面板来改变这些颜色）：
> SystemActiveBorder, SystemActiveCaption, SystemAppWorkspace, SystemBackground,
> SystemButtonFace, SystemButtonHighlight, SystemButtonShadow, SystemButtonText,
> SystemCaptionText, SystemDisabledText, SystemHighlight, SystemHighlightText,
> SystemInactiveBorder, SystemInactiveCaption, SystemInactiveCaptionText, SystemMenu,
> SystemMenuText, SystemScrollbar, SystemWindow, SystemWindowFrame, SystemWindowText。

- 如果你需要显式地指定颜色名，你可以使用如下格式的字符串：#RRGGBB。RR, GG, BB 分别是red,green和blue值的十六进制表示。
- 下面的例子演示了如何将一个颜色三元组转换为一个Tk颜色格式：
`tk_rgb = "#%02x%02x%02x" % (128, 192, 200)`
- 你可以使用窗口部件的winfo_rgb方法来将一个代表颜色的字符串（名字或RGB格式）转换为一个三元组：
> rgb = widget.winfo_rgb("red")  # widget = root.Tk()
> red, green, blue = rgb[0]/256, rgb[1]/256, rgb[2]/256
**注意** winfo_rgb返回16位的RGB值，范围在0~65535之间。要将它们映射到更通用的0~255范围内，你必须将每个值都除以256（或将它们向右移8位）。

## Frame
> w = Frame ( master, option, ... )
- master: 框架的父容器。
- options: 可选项，即该框架的可设置的属性。这些选项可以用键值的形式设置，并以逗号分隔：

bg: 框架背景颜色
bd: 框架的大小，默认为 2 个像素
cursor: 鼠标移动到框架时，光标的形状，可以设置为 arrow, circle, cross, plus 等。
height: 框架的高度，默认值是 0。
highlightbackground: 框架没有获得焦点时，高亮边框的颜色，默认由系统指定。
hlightcolor: 框架获得焦点时，高亮边框的颜色
highlightthickness: 指定高亮边框的宽度，默认值为 0不带高亮边框）
relief: 边框样式，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
width: 设置框架宽度，默认值是 0。
takefocus: 指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来），默认为 false。

## Menu
**一、属性**
- tearoff：分窗，0为在原窗，1为点击分为两个窗口
- bg,fg： 背景，前景
- borderwidth： 边框宽度
- font：  字体
- activebackgound： 鼠标划过时背景，同样有 activeforeground，activeborderwidth，disabledforeground
- cursor：当子菜单分离原窗时，鼠标在子菜单栏上的形状cursor="arrow" "circle" "clock" "cross" "dotbox" "exchange" "fleur" "heart" "man" "mouse" "pirate" "plus"等图形
- postcommand：点击菜单的回调函数
- selectcolor： 选中时背景色，add_checkbutton控件选中时，√的颜色
- takefocus：是否获取焦点
- title：当子菜单分离原窗时的标题
- relief： 当子菜单分离原窗时的3D效果，relief=RAISED,SUNKEN,FLAT,RIDGE,SOLID,GROOVE
**二、方法：**
- menu.add_cascade：  添加子菜单（menu参数为子菜单对像）
- menu.add_command：  添加命令（label参数为显示内容，command参数为响应函数）
- menu.add_separator：  添加分隔线
- menu.add_checkbutton： 添加确认按钮，与add_radiobutton用法相同，效果为：点击时打钩（variable参数决定绑定变量）
- delete： 删除

## progressbar
> Progressbar(父对像, options, ...)
- length	进度条的长度，默认是100像素
- mode	可以有两种模式，下面作介绍
- maximum	进度条的最大值，默认是100像素
- name	进度条的名称，供程序参考引用
- orient	进度条的方向，可以是 HORIZONTAL(默认) 或者是 VERTICAL
- value	进度条的目前值
- variable	记录进度条目前的进度值
**mode参数：**
- determinate：一个指针会从起点移至终点，通常当我们知道所需工作时间时，可以使用此模式，这是默认模式
- indeterminate：一个指针会在起点和终点间来回移动，通常当我们不知道工作所需时间时，可以使用此模式

- start(interval)：每隔interval时间移动一次指针。interval的默认值是50ms，每次移动指针调用一次step(amount)。
    在step()方法内的amount参数意义就是增值量
- step(amount)：每次增加一次amount，默认值是1.0，在determinate模式下，指针不会超过maximum参数。
    在indeterminate模式下，当指针达到maximum参数值的前一格时，指针会回到起点
- stop()：停止start()运行

## label属性
text    label   fg  font    width   height  padx    pady    justify image   compound(bitmap=BitmapImage(file=))
## checkbutton属性
text    command onvalue offvalue    image   bitmap  bg  fg  font    height  relief  width   wraplength  variable
wraplength  selector    selectimage underline   bd  textvariable    padx    pady    justify
deselect()  flash()     invoke()
## 变量操作
1. tk 变量对象设置变量值：var2 = tk.StringVar(); var2.set((11, 22, 33, 44))
获取变量值：var2.get()
2. checkbutton 设置变量：cb.setvar('name', 2)
获取变量值：cb.getvar('name')
3. entry 获取输入框中的内容：entry.get()

## 菜单操作
- 主菜单：menubar = Menu(root)，添加菜单：add_command('菜单名')
- 下拉菜单：fmenu = Menu(menubar)，添加下拉菜单至主菜单：add_casecade(label='下拉', menu=fmenu)
    + 添加分割线：add_seperator()
    + 添加按钮：add_radiobutton()  add_checkbutton()
- 给主窗口添加菜单属性：root['menu'] = menubar
- 下拉选择菜单：m = optionmenu(root, v, 'op1', 'op2', 'op3'...)  m['width']=10，选择的值传给StringVar v

## 按钮样式
0   选项名称             'relief'
1   数据库查找的选项名称    'relief'
2   数据库查找的选项类     'Relief'
3   默认值               'raised'
4   当前值               'groove'
