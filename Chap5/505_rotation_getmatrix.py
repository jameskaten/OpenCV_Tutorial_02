import cv2
import numpy as np

img = cv2.imread("../img/fish.jpg")
rows,cols = img.shape[0:2]

# rotation matrix
# axis: center, angle:45, scale:0.5
m45 = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5)
# axis: center, angle:90, scale:1.5
m90 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1.5)

# rotation matrix
img45 = cv2.warpAffine(img, m45, (cols, rows))
img90 = cv2.warpAffine(img, m90, (cols, rows))

cv2.imshow("original", img)
cv2.imshow("r45", img45)
cv2.imshow("r90", img90)
cv2.waitKey(0)
cv2.destroyAllWindows()
