import cv2
import numpy as np

img = cv2.imread('../img/hand.jpg')
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#Find contour
contours, heiarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
cntr = contours[0]
cv2.drawContours(img, [cntr], -1, (0,255,0),1)

# 볼록 선체 찾기 (좌표 기준)와 그리기
hull = cv2.convexHull(cntr)
cv2.drawContours(img2, [hull], -1, (0,255,0), 1)
#볼록 선체 만족 여부 확인
print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))

#볼록 선체 찾기 (인덱스 기준)
hull2 = cv2.convexHull(cntr, returnPoints=False)
#볼록 선체 결함 찾기
defects = cv2.convexityDefects(cntr, hull2)
# confex contour defect 순회
for i in range(defects.shape[0]):
    startP, endP, farthestP, distance = defects[i, 0]
    # 가장 먼 지점의 좌표 구하기
    farthest = tuple(cntr[farthestP][0])
    # 거리를 부동 소수점으로 변환
    dist = distance/256.0
    if dist > 1:
        cv2.circle(img2, farthest, 3, (0,0,255), -1)

cv2.imshow('contour', img)
cv2.imshow('convex hull', img2)
cv2.waitKey()
cv2.destroyAllWindows()