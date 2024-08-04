import cv2
import numpy as np

img = cv2.imread('../img/lightning.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contour
contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
contr = contours[0]

# 감싸는 사각형
x,y,w,h = cv2.boundingRect(contr)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 3)

# 최소한의 사각형
rect = cv2.minAreaRect(contr)
box = cv2.boxPoints(rect)
box = np.int0(box)      # 정수로 변환
cv2.drawContours(img, [box], -1, (0,255,0), 3)

# 최소한의 원 표시
(x,y), radius = cv2.minEnclosingCircle(contr)
cv2.circle(img, (int(x), int(y)), int(radius), (255,0,0), 2)

#최소한의 삼각형 표시
ret, tri = cv2.minEnclosingTriangle(np.float32(contr))
cv2.polylines(img, [np.int32(tri)], True, (255,0,255), 2)

#최소한의 타원 표시
ellipse = cv2.fitEllipse(contr)
cv2.ellipse(img, ellipse, (0,255,255), 3)

# 중심점을 통과하는 직선 표시
[vx,vy,x,y] = cv2.fitLine(contr, cv2.DIST_L2,0,0.01,0.01)
cols,rows = img.shape[:2]
cv2.line(img, (0, int(0-x*(vy/vx) + y)), (cols-1, int((cols-x)*(vy/vx) + y)), (0,0,255),2)

cv2.imshow('Bound Fit shape', img)
cv2.waitKey(0)
cv2.destroyAllWindows()