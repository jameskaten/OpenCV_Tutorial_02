import cv2
import numpy as np

target = cv2.imread('../img/4star.jpg')
shapes = cv2.imread('../img/shapestomatch.jpg')

targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
# Convert binary scale
ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)
# Find contour
cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
cntrs_shapes, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

# 각 도형과 매칭을 위한 반복문 -------------------------------------------------------------
matches = []
for contr in cntrs_shapes:
    match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
    # 해당 도형의 매칭 점수와 contour를 쌍으로 저장
    matches.append((match, contr))
    # 해당 도형의 컨투어 시작 지점에 매칭 점수 표시
    cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)

# 매칭 점수로 정렬
matches.sort(key=lambda x : x[0])
# 가장 적은 매칭 점수를 얻는 도형의 컨투어에 선 그리기
cv2.drawContours(shapes, [matches[0][1]], -1, (0,255,0), 3)
cv2.imshow('target', target)
cv2.imshow('Match Shape', shapes)
cv2.waitKey()
cv2.destroyAllWindows()