# 使用函数绘制matplotlib的图表组成元素

## 函数axhline()——绘制平行于x轴的水平参考线调用签名：plt.axhline(y=0.0,c="r",ls="--",lw=2)
- y：水平参考线的出发点。
- c：参考线的线条颜色。

## 函数axvspan()——绘制垂直于x轴的参考区域调用签名：plt.axvspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)。
- xmin：参考区域的起始位置。
- xmax：参考区域的终止位置。
- facecolor：参考区域的填充颜色。
- alpha：参考区域的填充颜色的透明度。
```plt.axvspan(xmin=4.0,xmax=6.0,facecolor="y",alpha=0.3)```

## 函数annotate()——添加图形内容细节的指向型注释文本调用签名：
plt.annotate(string,xy=(np.pi/2,1.0),xytext=((np.pi/2)+0.15,1.5),weight="bold",
color="b", arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b"))。
- string：图形内容的注释文本。
- xy：被注释图形内容的位置坐标。
- xytext：注释文本的位置坐标。
- weight：注释文本的字体粗细风格。
- color：注释文本的字体颜色。
- arrowprops：指示被注释内容的箭头的属性字典。

> plt.annotate("maximum",xy=(np.pi/2, 1.0),xytext=((np.pi/2)+1.0, .8),weight="bold",
>    color="b",arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b"))

## 函数text()——添加图形内容细节的无指向型注释文本
调用签名：plt.text(x,y,string,weight="bold",color="b")。
- x：注释文本内容所在位置的横坐标。
- y：注释文本内容所在位置的纵坐标。
- string：注释文本内容。

## 函数title()——添加图形内容的标题

## 函数legend()——标示不同图形的文本标签图例
调用签名：plt.legend(loc="lower left")。
- loc：图例在图中的地理位置。

# 使用统计函数绘制简单图形

## 函数bar()——用于绘制柱状图
调用签名：plt.bar(x,y)。
- x：标示在x轴上的定性数据的类别。
- y：每种定性数据的类别的数量。

## 函数barh()——用于绘制条形图
调用签名：plt.barh(x,y)。
- x：标示在y轴上的定型数据的类别。
- y：每种定性数据的类别的数量。

## 函数hist()——用于绘制直方图
调用签名：plt.hist(x)。
- x：在x轴上绘制箱体的定量数据输入值。

## 函数pie()——用于绘制饼图
调用签名：plt.pie(x)。
- x：定性数据的不同类别的百分比。

## 函数polar()——用于绘制极线图
调用签名：plt.polar(theta,r)。
- theta：每个标记所在射线与极径的夹角。
- r：每个标记到原点的距离。

## 函数scatter()——用于绘制气泡图
调用签名：plt.scatter(x,y)。
 - x:x轴上的数值。
 - y:y轴上的数值。
 - s：散点标记的大小。
 - c：散点标记的颜色。
 - cmap：将浮点数映射成颜色的颜色映射表。

## 函数stem()——用于绘制棉棒图
调用签名：plt.stem(x,y)。
- x：指定棉棒的x轴基线上的位置。
- y：绘制棉棒的长度。
- linefmt：棉棒的样式。
- markerfmt：棉棒末端的样式。
- basefmt：指定基线的样式。

## 函数boxplot()——用于绘制箱线图
调用签名：plt.boxplot(x)。
- x：绘制箱线图的输入数据。

## 函数errorbar()——用于绘制误差棒图
调用签名：plt.errorbar(x,y,yerr=a,xerr=b)。
- x：数据点的水平位置。
- y：数据点的垂直位置。
- yerr:y轴方向的数据点的误差计算方法。
- xerr:x轴方向的数据点的误差计算方法。
