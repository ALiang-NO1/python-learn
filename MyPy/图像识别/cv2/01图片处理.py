import cv2 as cv

img = cv.imread("1.jpg")
# cv.imshow("img", img)   # 显示图片

# ----------设置图片大小，使图片一直显示---------
# resized_img = cv.resize(img, dsize=(300, 500))
# print(resized_img.shape)
# cv.imshow('resized_img', resized_img)
# while True:
#     if ord('q') == cv.waitKey(0):   # 按下q键关闭图片
#         break

# ----------使图片变灰-------------
grey_img = cv.cvtColor(img, code=cv.COLOR_BGR2grey)
# =cv2.imgread("1.jpg", 0)
cv.imshow('grey_img', img)
cv.waitKey(0)
# cv.imwrite("grey.jpg", grey_img)
cv.destroyAllWindows()
