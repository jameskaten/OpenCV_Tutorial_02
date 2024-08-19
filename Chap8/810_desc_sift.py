import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT 추출기 생성
sift = cv2.xfeatures2d.SIFT_create()
# 키포인트 검출과 서술자 계산
keypoints, descriptor = sift.detectAndCompute(gray, None)
print('keypoint:', len(keypoints), 'descriptor:', descriptor.shape)
print(descriptor)

# draw keypoints
img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()

# =================================================================
# Error: AttributeError: module 'cv2' has no attribute 'xfeatures2d'
# Try 1: pip install opencv-contrib-python
# Try 2: pip install opencv-python==3.4.2.17
# Try 3: pip install opencv-contrib-python==3.4.2.17  --> Working 
