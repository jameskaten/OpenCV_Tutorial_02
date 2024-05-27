import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
rows,cols = img.shape[0:2]   # size of image

dx, dy = 100, 50        # pixel distance to move

# Translation matrix
mtrx = np.float32([[1, 0, dx],
                   [0, 1, dy]])
# Move
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

#탈락된 외곽 픽셀을 파란색으로 보정
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None,\
                      cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255,0,0))

# 탈락된 외곽 픽셀을 원본을 반사시켜서 보정
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, \
                      cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('original', img)
cv2.imshow('trans', dst)
cv2.imshow('BORDER_CONSTANT', dst2)
cv2.imshow('BORDER_REFLECT', dst3)
cv2.waitKey()
cv2.destroyAllWindows()