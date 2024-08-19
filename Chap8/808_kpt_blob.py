import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SimpleBlobDetector
detector = cv2.SimpleBlobDetector_create()
# KeyPoints
keypoints = detector.detect(gray)
# show red
img = cv2.drawKeypoints(img, keypoints, None, (0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blob", img)
cv2.waitKey(0)