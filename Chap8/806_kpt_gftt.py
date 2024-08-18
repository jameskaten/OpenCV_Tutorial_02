import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Good feature to trac
gftt = cv2.GFTTDetector_create()
# 키포인트 검출
keypoints = gftt.detect(gray, None)
# draw keypoints
img_draw = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow('GFTTDetector', img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()

