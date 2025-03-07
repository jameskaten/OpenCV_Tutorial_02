import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# FAST 특징 검출기 생성
fast = cv2.FastFeatureDetector_create(50)
# key point
keypoints = fast.detect(gray, None)
# Draw key points
img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow('FAST', img)
cv2.waitKey()
cv2.destroyAllWindows()