import numpy as np
import cv2

img = cv2.imread('../img/yate.jpg')

# color scale from BGR to YUV
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# YUV 컬러 스케일의 첫 번째 채널에 대해서 equalize 적용
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# 컬러 스케일을 YUV에서 BGR로 변경
img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Before', img)
cv2.imshow('After', img2)
cv2.waitKey()
cv2.destroyAllWindows()