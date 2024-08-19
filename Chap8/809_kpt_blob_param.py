import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blob 검출 필터 parameter
params = cv2.SimpleBlobDetector_Params()

# 경계값 조정
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5
# 면적 필터를 켜고 최소 값 지정
params.filterByArea = True
params.minArea = 200

# color 블록 비율, 원형 비율 필터 옵션 끄기
params.filterByColor = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByCircularity = False

# filter parameter로 blob 검출기 생성
detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(gray)
img_draw = cv2.drawKeypoints(img, keypoints, None, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blob with Params", img_draw)
cv2.waitKey(0)