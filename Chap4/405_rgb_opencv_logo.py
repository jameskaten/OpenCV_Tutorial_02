import cv2
import numpy as np

img = cv2.imread('../img/OpenCV_logo_black.png')
bgr = cv2.imread('../img/OpenCV_logo_black.png', cv2.IMREAD_COLOR)
# IMREAD_UNCHANGED Option
bgra = cv2.imread('../img/OpenCV_logo_black.png', cv2.IMREAD_UNCHANGED)

# image shapes by option
print("default: ", img.shape, "color: ", bgr.shape, "unchanged: ", bgra.shape)

cv2.imshow('bgr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('alpha', bgra[:,:,3])
cv2.waitKey(0)
cv2.destroyAllWindows()
