# PIL(PIL （Python Imaging Library）方法

## 图片操作
```python
from PIL import ImageGrab, Image

# 图片裁剪与粘贴
im = ImageGrab.grab((0,0,800,200))  # 截取屏幕指定区域的图像，（左，上，右，下）
im = ImageGrab.grab()  # 不带参数表示全屏幕截图

box = (120, 194, 220, 294)  # 定义裁剪区域
region = im.crop(box)  # 裁剪，从图像中提取矩形
region = region.transpose(Image.ROTATE_180)
im.paste(region,box)  # 粘贴回原图

# 缩放
im = im.resize((100,100))  # 参数表示图像的新尺寸，分别表示宽度和高度

# 拆分和合并
r, g, b = im.split()
im = Image.merge('RGB', (b, g, r))

# 点变换
im = im.point(lambda i: i * 1.2)
# 处理单个波段
rgb = im.split()
r = rgb[0].point(lambda i: i > 100 and 250)
g = rgb[1].point(lambda i: i * 1.2)
rgb[2].paste(g, None, r)
im = Image.merge(im.mode, rgb)

# 使用ImageSequence迭代器类
from PIL import ImageSequence, TarIO
for frame in ImageSequence.Iterator(im):
    pass

# 二进制读取文件
import io
im = Image.open(io.Bytes('buffer'))
# 从tar档案中读取
fp = TarIO.TarIO("Tests/images/hopper.tar", "hopper.jpg")
im = Image.open(fp)

# 在草稿模式下阅读
im.draft('L', (100, 200))
```

## 色彩处理
```python
from PIL import Image, ImageFilter, ImageEnhance

#原始图像
image = Image.open('lena.jpg')
print(imgage.info)  # 处理程序将属性添加到 info 属性，但在保存图像时忽略它
image.show()

#亮度增强
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
image_brightened.show()

#色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
image_colored.show()

#对比度增强
enh_con = ImageEnhance.Contrast(image)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
image_contrasted.show()

#锐度增强
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.show()

im = Image.open('bt1.jpg')
# 高斯模糊
im.filter(ImageFilter.GaussianBlur)
# 普通模糊
im.filter(ImageFilter.BLUR)
# 边缘增强
im.filter(ImageFilter.EDGE_ENHANCE)
# 找到边缘
im.filter(ImageFilter.FIND_EDGES)
# 浮雕
im.filter(ImageFilter.EMBOSS)
# 轮廓
im.filter(ImageFilter.CONTOUR)
# 锐化
im.filter(ImageFilter.SHARPEN)
# 平滑
im.filter(ImageFilter.SMOOTH)
# 细节
im.filter(ImageFilter.DETAIL)

## 旋转 
out = im.rotate(45)                              # 逆时针旋转 45 度角。
out = im.transpose(Image.FLIP_LEFT_RIGHT)        # 左右对换。
out = im.transpose(Image.FLIP_TOP_BOTTOM)        # 上下对换。
out = im.transpose(Image.ROTATE_90)              # 旋转 90 度角。
out = im.transpose(Image.ROTATE_180)             # 旋转 180 度角。
out = im.transpose(Image.ROTATE_270)             # 旋转 270 度角。
```
# PIL图片知识
python图像库处理 栅格图像; 也就是说，像素数据的矩形。

1. format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；size属性是一个tuple，表示图像的宽和高（单位为像素）；
mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为prepress图像。
2. 如果文件不能打开，则抛出IOError异常。

除非确实需要，否则库不会解码或加载栅格数据。打开文件时，将读取文件头以确定文件格式，并提取解码文件所需的模式、大小和其他属性等内容，但稍后才会处理其余文件。
```python
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass
```

## 波段
图像可以由一个或多个数据带组成。python图像库允许您在一个图像中存储多个波段，前提是它们都具有相同的尺寸和深度。
把每个像素想象成每个波段有一个值通常是有用的。要获取图像中带区的编号和名称，请使用 getbands() 方法。

## 模式
convert() 是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：
- 1 （1位黑白像素，每字节存储一个像素）
- L （8位像素，黑白）
- P （8位像素，使用调色板映射到任何其他模式）
- RGB （3x8位像素，真彩色）
- RGBA （4x8位像素，带透明蒙版的真彩色）
- CMYK （4x8位像素，分色）
- YCbCr （3x8位像素，彩色视频格式），请注意，这是指jpeg，而不是ITU-R BT.2020标准。
- LAB （3x8位像素，L*A*B颜色空间）
- HSV （3x8位像素、色调、饱和度、值颜色空间）
- I （32位有符号整数像素）
- F （32位浮点像素）

PIL还为一些特殊模式提供有限的支持，包括：
- LA （L和阿尔法）
- PA （P与阿尔法）
- RGBX （带填充的真彩色）
- RGBa （带预乘alpha的真彩色）
- La （L带预乘α）
- I;16 （16位无符号整数像素）
- I;16L （16位小端无符号整数像素）
- I;16B （16位大端无符号整数像素）
- I;16N （16位本机端无符号整数像素）
- BGR;15 （15位反转真彩色）
- BGR;16 （16位反转真彩色）
- BGR;24 （24位反转真彩色）
- BGR;32 （32位反转真彩色）

## 过滤器
PIL.Image.NEAREST
从输入图像中选取一个最近的像素。忽略所有其他输入像素。

PIL.Image.BOX
源图像的每个像素贡献给具有相同权重的目标图像的一个像素。因为上标相当于 NEAREST . 此筛选器只能与 resize() 和 thumbnail() 方法。

PIL.Image.BILINEAR
要调整大小，请使用可能有助于输出值的所有像素上的线性插值计算输出像素值。对于其他转换，使用输入图像中2x2环境上的线性插值。

PIL.Image.HAMMING
生成的图像比 BILINEAR 在地方层面上没有错位 BOX . 此筛选器只能与 resize() 和 thumbnail() 方法。

PIL.Image.BICUBIC
要调整大小，请使用可能有助于输出值的所有像素上的三次插值来计算输出像素值。对于其他转换，使用输入图像中4x4环境上的三次插值。

PIL.Image.LANCZOS
对所有可能有助于输出值的像素使用高质量Lanczos过滤器（截断的sinc）计算输出像素值。此筛选器只能与 resize() 和 thumbnail() 方法。

# 模块
## Image
1. new(mode,size,color=0) 创建新图像

2. formarray(obj,mode=None)
从导出数组接口的对象（使用缓冲区协议）创建图像内存。如果 obj 不是连续的，则调用tobytes方法并 frombuffer() 使用。
```py
im=Image.open('bt1.jpg')
a=np.asarray(im)
print(a)
Image.fromarray(a).show()
```

