import cv2
import numpy as np

img = cv2.imread('../img/shapes_donut.png')
img2 = np.zeros_like(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 연결된 요소 labeling
cnt, labels = cv2.connectedComponents(th)
#retval, labels, stats, cent = cv2.connectedComponentsWithStats(th)

# Label 개수만큼 순회
for i in range(cnt):
    img2[labels==i] = [int(j) for j in np.random.randint(0, 255, 3)]

cv2.imshow('origin', img)
cv2.imshow('labeled', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

