import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("../img/man_chromakey.jpg")
# img1 = cv2.imread("../img/Angela01.jpg")
img2 = cv2.imread("../img/street.jpg")

# ROI location
height1, width1 = img1.shape[:2]
height2, width2 = img2.shape[:2]
x = (width2 - width1)//2
y = height2 - height1
w = x + width1
h = y + height1

# 10 pixel at the background
chromakey = img1[:10, :10, :]
offset = 20

# HSV conversion
hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# 큭로마 키 영역의 H 값에서 offset만큼 여유를 두어서 범위 지정
# offset 값은 여러 차례 시도 후 결정
chroma_h = hsv_chroma[:, :, 0]
lower = np.array([chroma_h.min() - offset, 100, 100])
upper = np.array([chroma_h.max() + offset, 255, 255])

# 마스크 생성 및 마스킹 후 합성
mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)
roi = img2[y:h, x:w]
fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
bg = cv2.bitwise_and(roi, roi, mask=mask)
img2[y:h, x:w] = fg + bg

# result
cv2.imshow('chromakey', img1)
cv2.imshow('added', img2)
cv2.waitKey()
cv2.destroyAllWindows()