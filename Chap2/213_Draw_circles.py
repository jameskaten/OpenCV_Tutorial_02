# This file draws circles and ellipses

import cv2

img = cv2.imread('../img/blank_500.jpg')

# center(150, 150), radius 100
cv2.circle(img, (150, 150), 100, (255,0,0))
# center(300, 150), radius 70
cv2.circle(img, (300, 150), 70, (0,255,0), 5)
# center(50, 300), radius 50, rotation 0, 0-360deg
cv2.ellipse(img, (50, 300), (50,50), 0,0, 360, (0,0,255))
#center(150, 300), lower half circle
cv2.ellipse(img, (150, 300), (50,50), 0, 0, 180, (255,0,0))
#center(200, 300) top half circle
cv2.ellipse(img, (200, 300), (50,50), 0, 181, 360, (0,0,255))

#center(325, 300) radius(75, 50) ellipse
cv2.ellipse(img, (325,300), (75,50), 0, 0, 360, (0,255,0))
#center(450,300), radius(50, 75) ellipse
cv2.ellipse(img, (450,300), (50,75), 0, 0, 360, (255, 0, 255))

#center(50,425), radius(50,75), rotation15
cv2.ellipse(img, (50,425), (50,75), 15, 0, 360, (0,0,0))
#ceneter(200,425), radius(50,75), rotation45
cv2.ellipse(img,(200,425), (50,75), 45, 0, 360, (0,0,0))

#center(350,425), 45 rotation
cv2.ellipse(img, (350,425), (50,75), 45, 0, 180, (0,0,255))
#center(400,425), 45 rotation half
cv2.ellipse(img, (400,425), (50,75), 45, 181, 360, (255,0,0))

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()