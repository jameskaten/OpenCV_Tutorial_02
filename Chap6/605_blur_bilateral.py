import cv2
import numpy as np

img = cv2.imread('../img/gaussian_noise.jpg')

# Gaussian filter
blur1 = cv2.GaussianBlur(img, (5,5), 0)

# Bilateral filter
blur2 = cv2.bilateralFilter(img, 5, 75, 75)

merged = np.hstack((img, blur1, blur2))
cv2.imshow('bilateral', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()