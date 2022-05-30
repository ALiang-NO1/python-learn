import cv2
import numpy as np

img = cv2.imread("1.jpg")
cv2.imshow('img', img)
imgGrey = cv2.imread("1.jpg", 0)
cv2.imshow('灰图', imgGrey)

# ---------------图片宽、高、通道数获取----------
print("彩图shape：", img.shape)      # （图像高（图像矩阵的行数）、宽（图像矩阵的列数）和通道数）
print("灰图shape：", imgGrey.shape)

# ---------------图像像素数目和图像数据类型的获取----------
print("图片尺寸：", img.size)
print("图片类型：", img.dtype)

# --------------- 生成指定大小的空图像----------
imgZero = np.zeros(img.shape, np.uint8)
cv2.imshow("imgZero", imgZero)

imgFix = np.zeros((300, 500, 3), np.uint8)
cv2.imshow("imgFix", imgFix)

cv2.waitKey()
cv2.destroyAllWindows()