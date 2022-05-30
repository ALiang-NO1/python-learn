import cv2
import numpy as np


def wait():
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread("1.jpg")

# OpenCV中图像矩阵的顺序是B、G、R。可以直接通过坐标位置访问和操作图像像素
numb = img[50, 100]
print("图片坐标对应值：", numb)

img[50, 100] = (0, 0, 255)
cv2.imshow("img1", img)
print('修改img[50, 100]后的图片')
wait()

# 分开访问图像某一通道像素值
img[0:100, 100:200, 0] = 255
img[100:200, 200:300, 1] = 255
img[200:300, 300:400, 2] = 255

cv2.imshow("img2", img)
print('分别设置img像素通道值后的图片')
wait()

# 更改图像某一矩形区域的像素值
img[0:50, 1:100] = (0, 0, 255)

cv2.imshow("img3", img)
print('更改某一矩形区域值后的图片')
wait()

# 图像三通道分离和合并
b, g, r = cv2.split(img)

# b = cv2.split(img)[0]
# g = cv2.split(img)[1]
# r = cv2.split(img)[2]

merged = cv2.merge([b, g, r])

cv2.imshow("Blue", b)
print('红色通道')
wait()
cv2.imshow("Green", g)
print('绿色通道')
wait()
cv2.imshow("Red", r)
print('蓝色通道')
wait()
cv2.imshow("Merged", merged)
print('通道融合的图片')
wait()