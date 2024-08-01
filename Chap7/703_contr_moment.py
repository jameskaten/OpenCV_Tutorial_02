import cv2
import numpy as np

img = cv2.imread("../img/shapes.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Binary scale
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
# Find contour
contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

for c in contours:
    mmt = cv2.moments(c)
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01'] / mmt['m00'])
    # area
    a = mmt['m00']
    # contour length
    l = cv2.arcLength(c, True)
    # Yello point
    cv2.circle(img, (cx, cy), 5, (0, 255, 255), -1)
    cv2.putText(img, "A:%.2f"%a, (cx, cy+20), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255)) #중심점 근처에 너비 그리기
    cv2.putText(img, "L:%.2f"%l, tuple(c[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))  # 시작점에 길이 그리기
    print("area:%.2f"%cv2.contourArea(c, False))

cv2.imshow('center', img)
cv2.waitKey(0)
cv2.destroyAllWindows()