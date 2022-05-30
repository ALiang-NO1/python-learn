widget（部件）+event（事件的响应）
tkinter中的widget主要有Button（按钮）, Checkbutton（复选按钮）,Canvas（画布），Entry（条目）, Frame（框架）, Label（标签）,
LabelFrame（标签框架）, Listbox（列表框），menu（菜单），Menubutton（菜单按钮）,Message （消息），OptionMenu（选项菜单），
PanedWindow（中分栏窗口）, Radiobutton（单选按钮）, Scale（刻度条）, Scrollbar（滚动条），Spinbox（整数调节框），Text（文本框），
Combobox（下拉列表框）, Notebook（笔记本）, Progressbar（进度条）, Separator（分离器）, Sizegrip（尺寸调节器）, Treeview（树视图）

1.事件（event）：是指点击、按键等操作，在tkinter中，event是一个类，当某个事件发生时，生成一个event对象，不同类型的事件生成具有不同属性的event对象。
2.事件处理（event handler）：是指在捕获到事件后，程序自动执行的操作，是回调函数（recall function）。
3.事件绑定（event binding）：是当一个事件发生时程序能够做出响应。tkinter提供三种绑定方式：实例绑定bind（将某个事件处理绑定到某个组件上）、
类绑定bind_class（将某个事件处理绑定到某类组件上）、应用绑定bind_all（将某个事件处理绑定到所有组件上）。

在Tkinter中，事件的描述格式为：<[modifier-]-type[-detail]>，其中：
modifier：事件修饰符。如：Alt、Shit组合键和Double事件。
type：事件类型。如：按键（Key）、鼠标（Button/Motion/Enter/Leave/Relase）、Configure等。
detail：事件细节。如：鼠标左键（1）、鼠标中键（2）、鼠标右键（3）。

事件格式	            事件解释
---鼠标事件---------
<Button-1>	        鼠标点击（1-左键，2-中键，3-右键）
<Double-Button-1>	鼠标双击（1-左键，2-中键，3-右键）
<B1-Motion>	        鼠标拖动（1-左键，2-中键，3-右键）
<ButtonRelease-1>	鼠标按下之后释放（1-左键，2-中键，3-右键）
<Enter>	            鼠标进入控件范围（widget），不是键盘按键
<Leave>         	鼠标离开控件范围（widget）

------键盘事件--------
<Key>/<KeyPress>	任意键盘按键（键值会以char的格式放入event对象）
<Return>       <Cancel>       <BackSpace>       <Tab>       <Shift_L>       <Control_L>       <Alt_L>
<Left>           <Up>          <Down>       <Right>       <Delete>       <F1>       <F2>       <Home>
组件事件
Active	    当组件的状态从“未激活”变为“激活”的时候触发该事件
Button      当用户点击鼠标按键的时候触发该事件
detail      部分指定是具体用哪个键：<Button-1>鼠标左键，<Button-2>鼠标中键（滚轮点击），<Button-3>鼠标右键，
<Button-4>  滚轮上滚（Linux），<Button-5>滚轮下滚（Linux）
ButtonRelease   当用户释放鼠标按键的时候触发该事件，在大多数情况下，比Button要更好使用，因为如果当用户不小心按下鼠标键，
                用户可以将鼠标移出组件再释放鼠标，从而避免不小心触发事件
Configure	当组件的尺寸改变的时候触发该事件（窗口管理器触发的重绘事件，当你调整组件的尺寸或者移动应用程序，组件会和窗口一样被重绘）
Deactivate  当组件的状态从“激活”变为“未激活”的时候触发该事件
Destroy     当组件被销毁时触发该事件
Enter       当鼠标指针进入组件的时候触发该事件。注意：不是用户按下回车键（回车键是Return<Key-Return>）
Expose	    当窗口或组件的某部分不再被覆盖的时候触发该事件
FocusIn     当组件获得焦点的时候触发该事件。用户可以用Tab键将焦点转移到该组件上（需要该组件的takefocus选项为True）
            你也可以调用focus_set()方法使该组件获得焦点
FocusOut	当组件失去焦点的时候触发该事件
KeyPress    当用户按下键盘按键的时候触发该事件
detail      可以指定具体的按键，例如<KeyPress-H>表示当大写字母H被按下的时候触发该事件
KeyPress    可以缩写为Key
KeyRelease	当用户释放键盘按键的时候触发该事件
Leave	    当鼠标指针离开组件的时候触发该事件
Map         当组件被映射的时候触发该事件，意思是在应用程序中显示该组件的时候，例如调用get()方法
Motion      当鼠标在组件内移动的时候触发该事件
MouseWheel  当鼠标滚轮滚动的时候触发该事件，目前该事件仅支持Windows和Mac系统
Unmap       当组件被取消映射的时候触发该事件，意思是在应用程序中不再显示该组件的时候，例如调用grid_remove()方法
Visibility	当应用程序至少有一部分在屏幕中是可见的时候触发该事件