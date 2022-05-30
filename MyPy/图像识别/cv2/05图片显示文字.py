import cv2

img = cv2.imread("1.jpg")

cv2.putText(img, "Beauty", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (59,127, 0), 1)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

"""
putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

img： 图像
text：要输出的文本
org： 文字的起点坐标
fontFace： 字体
fontScale： 字体大小
color： 字体颜色
thickness： 字图加粗
"""