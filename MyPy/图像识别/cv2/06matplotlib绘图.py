import cv2
# 添加中文字体支持
from matplotlib.font_manager import FontProperties
from pylab import *

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

im = cv2.imread('1.jpg')
# 显示原始图像
fig = plt.figure()
subplot(121)
plt.gray()

im2 = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  # OpenCV采用BGR排列顺序,需要转换一下.
imshow(im2)
title(u'彩色图', fontproperties=font)
axis('off')

# 显示灰度化图像
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
plt.subplot(122)
plt.gray()
imshow(gray)
title(u'灰度图', fontproperties=font)
axis('off')
show()
