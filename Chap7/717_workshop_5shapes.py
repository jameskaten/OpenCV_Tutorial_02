import cv2
import numpy as np

img = cv2.imread('../img/5shapes.jpg')
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# find contour
contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
for contour in contours:
    # 각 컨투어에 근사 컨투어로 단순화
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    # 꼭짓점의 개수
    vertices = len(approx)
    print("vertices: ", vertices)

    # center position
    mmt = cv2.moments(contour)
    cx, cy = int(mmt['m10']/mmt['m00']), int(mmt['m01']/mmt['m00'])

    name = "Unkown"
    if vertices == 3:   # 3 is a triangle
        name = "Trangle"
        color = (0,255,0)
    elif vertices == 4:
        x,y,w,h = cv2.boundingRect(contour)
        if abs(w-h) <= 3:
            name = 'Square'
            color = (0,125,125)
        else:
            name = 'Rectangle'
            color = (0,0,255)
    elif vertices == 10:
        name = 'Star'
        color = (255,255,0)
    elif vertices >= 15:
        name = 'Circle'
        color = (0,255,255)
    # Draw contour
    cv2.drawContours(img2, [contour], -1, color, -1)
    # Name
    cv2.putText(img2, name, (cx-50, cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100,100,100), 1)

cv2.imshow('Input Shapes', img)
cv2.imshow('Recognizing Shapes', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()