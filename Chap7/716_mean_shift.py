import cv2
import numpy as np

img =cv2.imread('../img/taekwonv1.jpg')
# Trackbar event
def onChange(x):
    # sp, sr, level 선택값 수집
    sp = cv2.getTrackbarPos('sp', 'img')
    sr = cv2.getTrackbarPos('sr', 'img')
    lv = cv2.getTrackbarPos('lv', 'img')

    # Moving average filter
    mean = cv2.pyrMeanShiftFiltering(img, sp, sr, None, lv)
    cv2.imshow('img', np.hstack((img, mean)))

cv2.imshow('img', np.hstack((img, img)))
# Trackbar event
cv2.createTrackbar('sp', 'img', 0, 100, onChange)
cv2.createTrackbar('sr', 'img', 0, 100, onChange)
cv2.createTrackbar('lv', 'img', 0, 5, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()