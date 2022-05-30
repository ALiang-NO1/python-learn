import cv2

img = cv2.imread("1.jpg")
cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# 在图上画形状
x, y, w, h = 0, 0, 40, 50
cv2.rectangle(img, (x, y, x+w, x+h), color=(255, 0, 0), thickness=2)
cv2.circle(img, center=(120, 120), radius=70, thickness=2, color=(0, 255, 0))
cv2.imshow('draw_img', img)
cv2.waitKey(0)

cv2.waitKey()
cv2.destroyAllWindows()