import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../img/bright.jpg")
img_yuv = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)

# Equalize to brightness
img_eq = img_yuv.copy()
img_eq[:,:,0] = cv2.equalizeHist(img_eq[:,:,0])
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YUV2BGR)

# 밝기 채널에 대해서 CLAHE 적용
img_clahe = img_yuv.copy()
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8)) # CLAHE 생성
img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])    # CLAHE 작용
img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YUV2BGR)

# Result
cv2.imshow('Before', img)
cv2.imshow('CLAHE', img_clahe)
cv2.imshow('equalizeHist', img_eq)
cv2.waitKey()
cv2.destroyAllWindows()