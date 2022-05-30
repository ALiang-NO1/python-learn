# TL��DR
- Pyplot �� Matplotlib ���ӿ⣬�ṩ�˺� MATLAB ���ƵĻ�ͼ API��
- Pyplot �ǳ��õĻ�ͼģ�飬�ܷܺ������û����� 2D ͼ��
- Pyplot ����һϵ�л�ͼ��������غ�����ÿ��������Ե�ǰ��ͼ�����һЩ�޸ģ����磺��ͼ����ϱ�ǣ����µ�ͼ����ͼ���в����µĻ�ͼ����ȵȡ�

# plot����
plot() �����ǻ��ƶ�άͼ�ε�����������������Ի��Ƶ����
> plot([x], y, [fmt], *, data=None, **kwargs)# ��������
> plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)# ��������

## ����˵��
- x, y������ߵĽڵ㣬x Ϊ x �����ݣ�y Ϊ y �����ݣ����ݿ����б�����顣
- fmt����ѡ�����������ʽ������ɫ����Ǻ�������ʽ�������� o:r��o ��ʾʵ��Բ��ǣ�: ��ʾ���ߣ�r ��ʾ��ɫΪ��ɫ��
- **kwargs����ѡ�����ڶ�άƽ��ͼ�ϣ�����ָ�����ԣ����ǩ���ߵĿ�ȵȡ�

```py
>>> plot(x, y)        # ���� y �������� x �ж�Ӧֵ�Ķ�ά��ͼ��ʹ��Ĭ����ʽ
>>> plot(x, y, 'bo')  # ���� y �������� x �ж�Ӧֵ�Ķ�ά��ͼ��ʹ����ɫʵ��Ȧ����
>>> plot(y)           # x ��ֵΪ 0..N-1
>>> plot(y, 'r+')     # ʹ�ú�ɫ + ��
```

### fmt����˵��
- ��ɫ�ַ���'b' ��ɫ��'m' ���ɫ��'g' ��ɫ��'y' ��ɫ��'r' ��ɫ��'k' ��ɫ��'w' ��ɫ��'c' ����ɫ��'#008000' RGB ��ɫ�������������߲�ָ����ɫʱ�����Զ�ѡ��ͬ��ɫ��
- ���Ͳ�����'�\' ʵ�ߣ�'�\�\' �����ߣ�'�\.' �㻮�ߣ�':' ���ߡ�
- ����ַ���'.' ���ǣ�',' ���ر��(��С��)��'o' ʵ��Ȧ��ǣ�'v' �����Ǳ�ǣ�'^' �����Ǳ�ǣ�'>' �����Ǳ�ǣ�'<' �����Ǳ��...�ȵȡ�
```py
rng=np.random.RandomState(0)
for marker in ['o','.','x','+','^','v','<','>','s','d']:
    plt.plot(rng.rand(5), rng.rand(5), marker, label='marker=%s' % marker)
plt.legend(numpoints=1)
plt.xlim(0)
```

### ��Ǵ�С����ɫ
- markersize����дΪ ms�������ǵĴ�С��
- markerfacecolor����дΪ mfc���������ڲ�����ɫ��
- markeredgecolor����дΪ mec�������Ǳ߿����ɫ��

�������ֻ�������������㣬������һ���ߣ�����ʹ�� o ��������ʾһ��ʵ��Ȧ�ı�ǣ�
```py
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, marker='o', ms=10, mec='r')  # �������� (1, 3) �� (8, 10) ��������
plt.show()
```
����Ҳ���Ի������������ĵ㣬ֻ��**ȷ���������ϵĵ�����ͬ**���ɡ�


### ������
�ߵ����Ϳ���ʹ�� linestyle ���������壬��дΪ ls
```py
plt.plot(ypoints, linestyle = 'dotted')
plt.plot(ypoints, ls = '-.')
```

### ����ɫ
�ߵ���ɫ����ʹ�� color ���������壬��дΪ c��
```py
plt.plot(ypoints, color = 'r')
plt.plot(ypoints, c = '#8FBC8F')
plt.plot(ypoints, c = 'SeaGreen')
```

### �߿��
�ߵĿ�ȿ���ʹ�� linewidth ���������壬��дΪ lw��ֵ�����Ǹ��������磺1��2.0��5.67 �ȡ�


# Matplotlib ���ǩ�ͱ���
- ���ǿ���ʹ�� xlabel() �� ylabel() ���������� x ��� y ��ı�ǩ��
```py
plt.xlabel("x - label")
plt.ylabel("y - label")
```

- ���ǿ���ʹ�� title() ���������ñ��⡣
```py
plt.title("RUNOOB TEST TITLE")
```

## ͼ��������ʾ
Matplotlib Ĭ�������֧�����ģ���������ʹ��˼Դ���壬˼Դ������ Adobe �� Google �Ƴ���һ�Դ���塣
- ������https://source.typekit.com/source-han-serif/cn/
- GitHub ��ַ��https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese
- ��������: https://pan.baidu.com/s/14cRhgYvvYotVIFkRVd71fQ��

## �Զ�������
```py
# fname Ϊ �����ص������·����ע�� SourceHanSansSC-Bold.otf �����·����size �������������С
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf", size=18)
font1 = {'color':'blue','size':20}
font2 = {'color':'darkred','size':15}
x = np.arange(1,11)
y =  2  * x +  5

# fontdict ����ʹ�� css ������������ʽ
plt.title("����̳� - ����", fontproperties=zhfont1, fontdict = font1)
 
# fontproperties ����������ʾ��fontsize ���������С
plt.xlabel("x ��", fontproperties=zhfont1)
plt.ylabel("y ��", fontproperties=zhfont1)
plt.plot(x,y)
plt.show()
```

## ��� loc ������������λ��
ֵ����Ϊ left|right|center(Ĭ��)
```py
plt.title("����̳� - ����", fontproperties=zhfont1, fontdict = font1, loc="left")
plt.xlabel("x ��", fontproperties=zhfont1, loc="left")
plt.ylabel("y ��", fontproperties=zhfont1, loc="top")
```


# Matplotlib ������
���ǿ���ʹ�� pyplot �е� grid() ����������ͼ���е������ߡ�
> matplotlib.pyplot.grid(b=None, which='major', axis='both', )

## ����˵��
- b����ѡ��Ĭ��Ϊ None���������ò���ֵ��true Ϊ��ʾ�����ߣ�false Ϊ����ʾ��������� **kwargs ��������ֵΪ true��
- which����ѡ����ѡֵ�� 'major'��'minor' �� 'both'��Ĭ��Ϊ 'major'����ʾӦ�ø��ĵ������ߡ�
- axis����ѡ��������ʾ�ĸ�����������ߣ�������ȡ 'both'��Ĭ�ϣ���'x' �� 'y'���ֱ��ʾ��������x �᷽��� y �᷽��- 
- **kwargs����ѡ������������ʽ�������� color='r', linestyle='-' �� linewidth=2���ֱ��ʾ�����ߵ���ɫ����ʽ�Ϳ�ȡ�
```plt.grid(axis='x') # ���� y �����᷽����ʾ������```

���һ���򵥵������ߣ������������ߵ���ʽ����ʽ���£�
> grid(color = 'color', linestyle = 'linestyle', linewidth = number)

## ����ʽ����˵����
- color��'b' ��ɫ��'m' ���ɫ��'g' ��ɫ��'y' ��ɫ��'r' ��ɫ��'k' ��ɫ��'w' ��ɫ��'c' ����ɫ��'#008000' RGB ��ɫ������
- linestyle��'�\' ʵ�ߣ�'�\�\' �����ߣ�'�\.' �㻮�ߣ�':' ���ߡ�
- linewidth�������ߵĿ�ȣ���������һ�����֡�


# Matplotlib ���ƶ�ͼ
���ǿ���ʹ�� pyplot �е� subplot() �� subplots() ���������ƶ����ͼ��

subpot() �����ڻ�ͼʱ��Ҫָ��λ�ã�subplots() ��������һ�����ɶ�����ڵ���ʱֻ��Ҫ�������ɶ���� ax ���ɡ�

> subplot(nrows, ncols, index, **kwargs)
> subplot(pos, **kwargs)
> subplot(**kwargs)
> subplot(ax)
���Ϻ�����������ͼ����ֳ� nrows �к� ncols �У�Ȼ������ң����ϵ��µ�˳���ÿ����������б�� 1...N �����ϵ�������ı��Ϊ 1�����µ�������Ϊ N����ſ���ͨ������ index �����á�

���� numRows �� 1��numCols �� 2�����ǽ�ͼ����Ƴ� 1x2 ��ͼƬ����, ��Ӧ������Ϊ��(1, 1), (1, 2)
plotNum �� 1, ��ʾ������Ϊ(1, 1), ����һ�е�һ�е���ͼ��
plotNum �� 2, ��ʾ������Ϊ(1, 2), ����һ�еڶ��е���ͼ��

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

- nrows��Ĭ��Ϊ 1������ͼ���������
- ncols��Ĭ��Ϊ 1������ͼ���������
- sharex��sharey������ x��y ���Ƿ������ԣ�Ĭ��Ϊ false��������Ϊ 'none'��'all'��'row' �� 'col'�� 
  + False �� none ÿ����ͼ�� x ��� y �ᶼ�Ƕ����ģ�
  + True �� 'all'��������ͼ���� x ��� y �ᣬ
  + 'row' ����ÿ����ͼ�й���һ�� x ��� y �ᣬ
  + 'col'������ÿ����ͼ�й���һ�� x ��� y �ᡣ
- squeeze������ֵ��Ĭ��Ϊ True����ʾ�����ά�ȴӷ��ص� Axes(��)�����м�����
  + ���� N*1 �� 1*N ����ͼ������һ�� 1 ά���飬
  + ���� N*M��N>1 �� M>1 ����һ�� 2 ά���顣
  + �������Ϊ False���򲻽��м�ѹ����������һ��Ԫ��Ϊ Axes ʵ����2ά���飬��ʹ��������1x1��
- subplot_kw����ѡ���ֵ����͡����ֵ�Ĺؼ��ִ��ݸ� add_subplot() ������ÿ����ͼ��
- gridspec_kw����ѡ���ֵ����͡����ֵ�Ĺؼ��ִ��ݸ� GridSpec ���캯��������ͼ����������(grid)��
- **fig_kw������ϸ�Ĺؼ��ֲ������� figure() ������

```py
# ����һЩ�������� -- ͼ1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# ����һ���������ͼ -- ͼ2
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# ����������ͼ -- ͼ3
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# �����ĸ���ͼ -- ͼ4
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# ���� x ��
plt.subplots(2, 2, sharex='col')

# ���� y ��
plt.subplots(2, 2, sharey='row')

# ���� x ��� y ��
plt.subplots(2, 2, sharex='all', sharey='all')

# ���Ҳ�ǹ��� x ��� y ��
plt.subplots(2, 2, sharex=True, sharey=True)

# ����10 ��ͼ���Ѿ����ڵ���ɾ��
fig, ax = plt.subplots(num=10, clear=True)

plt.show()
```


# Matplotlib ɢ��ͼ
���ǿ���ʹ�� pyplot �е� scatter() ����������ɢ��ͼ��
> scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

## ����˵��
- x��y��������ͬ�����飬Ҳ�������Ǽ�������ɢ��ͼ�����ݵ㣬�������ݡ�
- s����Ĵ�С��Ĭ�� 20��Ҳ�����Ǹ����飬����ÿ������Ϊ��Ӧ��Ĵ�С��
- c�������ɫ��Ĭ����ɫ 'b'��Ҳ�����Ǹ� RGB �� RGBA ��ά�����顣
- marker�������ʽ��Ĭ��СԲȦ 'o'��
- cmap��Colormap��Ĭ�� None������������һ�� colormap �����֣�ֻ�� c ��һ�������������ʱ��ʹ�á����û���������� image.cmap��
- norm��Normalize��Ĭ�� None������������ 0-1 ֮�䣬ֻ�� c ��һ���������������ʱ��ʹ�á�
- vmin��vmax�����������ã��� norm ��������ʱ����ԡ�
- alpha����͸�������ã�0-1 ֮�䣬Ĭ�� None������͸����
- linewidths������ǵ�ĳ��ȡ�
- edgecolors������ɫ����ɫ���У�Ĭ��Ϊ 'face'����ѡֵ�� 'face', 'none', None��
- plotnonfinite��������ֵ�������Ƿ�ʹ�÷��޶��� c ( inf, -inf �� nan) ���Ƶ㡣
- **kwargs��������������

```py
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
plt.scatter(x, y)
plt.show()
```

## ���óߴ�
sizes = np.array([20,50,100,200,500,1000,60,90])�ñ�ǳߴ�
```plt.scatter(x, y, s=sizes)```

## ���ñ����ɫ
```py
colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
plt.scatter(x, y, c=colors)
```

## ��������ɢ��ͼ
```py
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
```

## ���ɢ��ͼ
```py
# �����������������
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5) # ������ɫ��͸����
plt.title("RUNOOB Scatter Test") # ���ñ���
plt.show()
```

## ��ɫ�� Colormap
- Matplotlib ģ���ṩ�˺ܶ���õ���ɫ����
- ��ɫ������һ����ɫ�б�����ÿ����ɫ����һ����Χ�� 0 �� 100 ��ֵ��
- ������ɫ����Ҫʹ�� cmap ������Ĭ��ֵΪ 'viridis'��֮����ɫֵ����Ϊ 0 �� 100 �����顣
```py
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')  # ����afmhot_r��
plt.colorbar()  # ��ʾ��ɫ��
plt.show()
```


# Matplotlib ����ͼ
���ǿ���ʹ�� pyplot �е� bar() ��������������ͼ��
> matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)

## ����˵����
- x�����������飬����ͼ�� x �����ݡ�
- height�����������飬����ͼ�ĸ߶ȡ�
- width�����������飬����ͼ�Ŀ�ȡ�
- bottom�����������飬������ y ���꣬Ĭ�� 0��
- align������ͼ�� x ����Ķ��뷽ʽ��
  + 'center' �� x λ��Ϊ���ģ�����Ĭ��ֵ�� 
  + 'edge'��������ͼ�����Ե�� x λ�ö���
  + Ҫ�����ұ�Ե�����Σ����Դ��ݸ����Ŀ��ֵ�� align='edge'��
- **kwargs��������������

```py
x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])
plt.bar(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"])
plt.show()
```

## ������״ͼ
��ֱ���������ͼ����ʹ�� barh() ����������
```plt.barh(x,y)```

## �������ӿ��
��������ͼ��ȣ�bar() ����ʹ�� width ���ã�barh() ����ʹ�� height ���� height
```plt.bar(x, y, width = 0.1)```


# Matplotlib ��ͼ
���ǿ���ʹ�� pyplot �е� pie() ����������ɢ��ͼ��
> matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]

## ����˵����
- x�����������飬��ʾÿ�����ε������
- explode�����飬��ʾ��������֮��ļ����Ĭ��ֵΪ0��
- labels���б��������εı�ǩ��Ĭ��ֵΪ None��
- colors�����飬��ʾ�������ε���ɫ��Ĭ��ֵΪ None��
- autopct�����ñ�ͼ�ڸ������ΰٷֱ���ʾ��ʽ��%d%% �����ٷֱȣ�%0.1f һλС���� %0.1f%% һλС���ٷֱȣ� %0.2f%% ��λС���ٷֱȡ�
- labeldistance����ǩ��ǵĻ���λ�ã�����ڰ뾶�ı�����Ĭ��ֵΪ 1.1���� <1������ڱ�ͼ�ڲࡣ
- pctdistance���������� labeldistance��ָ�� autopct ��λ�ÿ̶ȣ�Ĭ��ֵΪ 0.6��
- shadow��������ֵ True �� False�����ñ�ͼ����Ӱ��Ĭ��Ϊ False����������Ӱ��
- radius�������ñ�ͼ�İ뾶��Ĭ��Ϊ 1��
- startangle������ʼ���Ʊ�ͼ�ĽǶȣ�Ĭ��Ϊ�� x ����������ʱ�뻭�����趨 =90 ��� y ����������
- counterclock������ֵ������ָ�뷽��Ĭ��Ϊ True������ʱ�룬False Ϊ˳ʱ�롣
- wedgeprops ���ֵ����ͣ�Ĭ��ֵ None�������ֵ䴫�ݸ� wedge ����������һ����ͼ�����磺wedgeprops={'linewidth':5} ���� wedge �߿�Ϊ5��
- textprops ���ֵ����ͣ�Ĭ��ֵΪ��None�����ݸ� text ������ֵ�������������ñ�ǩ��labels���ͱ������ֵĸ�ʽ��
- center ���������͵��б�Ĭ��ֵ��(0,0)����������ͼ������λ�á�
- frame ���������ͣ�Ĭ��ֵ��False������� True�����ƴ��б�����ܡ�
- rotatelabels ���������ͣ�Ĭ��Ϊ False�����Ϊ True����תÿ�� label ��ָ���ĽǶȡ�

```py
y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A','B','C','D'], # ���ñ�ͼ��ǩ
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # ���ñ�ͼ��ɫ
        explode=(0, 0.2, 0, 0), # �ڶ�����ͻ����ʾ��ֵԽ�󣬾�������ԽԶ
        autopct='%.2f%%', # ��ʽ������ٷֱ�
       )
plt.title("RUNOOB Pie Test")
plt.show()
```
**ע��**��Ĭ������£���һ�����εĻ����Ǵ� x �Ὺʼ����ʱ���ƶ�
