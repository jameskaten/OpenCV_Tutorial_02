import cv2

img = cv2.imread('../img/Angela03.jpg')

# Gaussian image pyramid reduce
smaller = cv2.pyrDown(img)
# Gaussian image pyramid enlarge
bigger = cv2.pyrUp(img)

cv2.imshow('img', img)
cv2.imshow('pyrDown', smaller)
cv2.imshow('pyrUp', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()