## Figure
```py
fig=plt.figures()  # 没有轴的空图形
fig,ax=plt.figures()  # 单轴，一个图形
fig,axs=plt.subplots(2,2)  # 2x2排布的一个图形
```

## 面向对象接口（object-oriented）
创建Matplotlib两种方式：
1. 直接创建图形和轴，也称为面向对象类型（OO），主要用于非交互绘图（函数和脚本）
2. 使用pylot函数自动创建和管理图形和轴，用于交互绘图，如Jupter notebook
```py
x = np.linspace(0, 2, 100)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
```

## 自定义绘图函数
```py
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
```

## 后端
- 前端：面向用户的代码（绘图代码）；
- 后端：幕后作艰苦工作来制作图形。
  * 有用户界面后端（用于PyQt/PySide PyGobject Tkinter wxPython MacOS/Cocoa）也叫交互式后端；
  * 制作图像文件的硬拷贝后端（PNG SVG PDF PS）也叫非交互式后端。
### 配置后端方法
1. rcParams['backend']参数中的matplotlibrc文档
2. MPLBACKEND环境变量
3. matplotlib.use()（优先配置）

## 线条样式:color colorstyle
```py
plt.plot(x,np.sin(x),color='red'|'g'|'0.75'|'#000'|(0,0,0)|'chartreuse',colorste=solid|dashed|dasnhot|dotted)
```

## 坐标轴范围:xlim ylim axis
```py
plt.xlim(-1,11) | ax.set_xlim()
plt.ylim(-1.5,-1.5)
// 坐标轴反向
plt.xlim(10,0)
plt.ylim(1.2,-1.2)
// 快速设置坐标轴
plt.axis([-1,11,-1.5,1.5])
```

## 坐标轴间距:axis
```py
plt.axis('tight'|'equal')
```

## 线条图例：legend
```py
plt.plot(x,np.sin(x),'-g',label='sin(x)') | ax.set_xlabel()
plt.plot(y,np.cos(x),':b',label='cos(x)')
plt.legend(numpoints=1)
```

## 通过ax.set()一次性设置所有属性
```py
ax=plt.ases()
ax.plot(x,np.sin(x))
ax.set(xlim=(0,10), ylim=(-2,2), xlabel='x', ylabel='sin(x)', title='Plot')
```

## plt.style
```py
plt.style.use('seaborn-whitegrid')
```

## 鸢尾花数据:sklearn
```py
from sklearn.datasets import load_iris
iris=load_iris()
featurns=iris.data.T
plt.scatter(featurns[0], featurns[1], alpha=0.2, s=100*featurns[3], c=iris.target, cmap='viridis')  # 花萼的长宽，s:花瓣的大小，c:花瓣颜色
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
```

## 基础误差条：errorbar
```py
x=np.linespace(0, 10, 50)
dy = 0.8
y=np.sin(x) + dy*np.random.randn(50)
plt.errorbar(x,y,yerr=dy,fmt='.k', elinewidth=3, capsize=0)  # xerr:水平误差条
```

## 密度和轮廓图
```py
def f(x,y): return np.sin(x)**10 + np.cos(10+y*x)*np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y=np.meshgrid(x, y)
Z = f(X, Y)
# 轮廓图
plt.contour(X, Y, Z, colors='black', cmap='RdGy')  # 虚线表示负值，RdGy表示线条颜色（Red-Gray)
# 填充数值区域
plt.contourf(X, Y, Z, cmap='RdGy'); plt.colorbar()
# 图像显示连续颜色
# 结合轮廓图和图像
contours=plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=0)  # 数值标签

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar(); plt.axis(aspect='image')
```
- plt.imshow()不接受 x 和 y 网格值作为参数，因此你需要手动指定extent参数[xmin, xmax, ymin, ymax]来设置图表的数据范围。
- plt.imshow()使用的是默认的图像坐标，即左上角坐标点是原点，而不是通常图表的左下角坐标点。这可以通过设置origin参数来设置。
- plt.imshow()会自动根据输入数据调整坐标轴的比例；这可以通过参数来设置，例如，plt.axis(aspect='image')能让 x 和 y 轴的单位一致。

## 直方图，分桶和密度
```py
plt.hist(data, bins=30, density=True, alpha=.5, histtype='stepfilled', color='steelblue', edgecolor='none')
x1=np.random.normal(0,0,8,1000)
x2=np.random.normal(-2,1,1000)
x3=np.random.normal(3,2,1000)
kwargs=dict(histtype='stepfilled', alpha=.3, density=True, bins=30)
plt.hist(x1, **kwargs)
```


## 
```py

```


## 
```py

```


## 
```py

```


## 
```py

```


## 
```py

```


## 
```py

```


## 
```py

```


## 
```py

```


