import cv2
import numpy as np

win_name = 'scan'
img = cv2.imread('../img/paper.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)
draw = img.copy()

# Gray scale change and canny edge
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)     # noise reduction
edged = cv2.Canny(gray, 75, 200)            # Canny edge detection
cv2.imshow(win_name, edged)
cv2.waitKey(0)

# find contour
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
# Draw every contours
cv2.drawContours(draw, cnts, -1, (0,255,0))
cv2.imshow(win_name, draw)
cv2.waitKey(0)

# 영역 크기순으로 정렬
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
for c in cnts:
    # 영역이 가장 큰 contour부터 근사 contour 단순화
    peri = cv2.arcLength(c, True)   # perimeter
    # 둘레 길이의 0.02 근사 값으로 근사화
    vertices = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(vertices) == 4:      # 근사한 꼭짓점이 4개면 중지
        break
pts = vertices.reshape(4, 2)        # N x 1 x 2배열을 4 x 2 크기로 조정
for x,y in pts:
    cv2.circle(draw, (x,y), 10, (0,255,0), -1)      #green circle
cv2.imshow(win_name, draw)
cv2.waitKey(0)
merged = np.hstack((img, draw))

# 좌표 상하좌우 찾기
sm = pts.sum(axis=1)                # 4쌍의 각각 x+y 계산
diff = np.diff(pts, axis = 1)       # 4쌍의 각각 x-y 계산

topLeft = pts[np.argmin(sm)]        # x+y가 가장 작은 값이 좌상단 좌표
bottomRight = pts[np.argmax(sm)]    # x+y가 가장 큰 값이 좌하단 좌표
topRight = pts[np.argmin(diff)]     # x-y가 가장 작은 값이 우상단 좌표
bottomLeft = pts[np.argmax(diff)]   # x-y가 가장 큰 값이 좌하단 좌표

# 변환 전 4개 좌표
pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

# 변환 후 영상에 사용할 서류의 폭과 높이 계산
w1 = abs(bottomRight[0] - bottomLeft[0])    # 상단 좌우 좌표 간의 거리
w2 = abs(topRight[0] - topLeft[0])          # 하단 좌우 좌표 간의 거리
h1 = abs(topRight[1] - bottomRight[1])      # 우측 상하 좌표 간의 거리
h2 = abs(topLeft[1] - bottomLeft[1])        # 좌측 상하 좌표 간의 거리
width = max([w1, w2])                       # 두 좌우 거리 간의 최대 값이 서류의 폭
height = max([h1, h2])                      # 두 상하 거리 간의 최대 값이 서류의 높이

# 변환 후 4개의 좌표
pts2 = np.float32([[0,0], [width-1,0], [width-1,height-1], [0,height-1]])

# 변환행렬 계산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, mtrx, (width, height))
cv2.imshow(win_name, result)
cv2.waitKey(0)
cv2.destroyAllWindows()