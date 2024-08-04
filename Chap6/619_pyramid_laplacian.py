import cv2
import numpy as np

img = cv2.imread('../img/taekwonv1.jpg')

smaller = cv2.pyrDown(img)
# bigger by Gaussian pyramid
bigger = cv2.pyrUp(smaller)

# 원본에서 확대한 영상 빼기
laplacian = cv2.subtract(img, bigger)
# 확대한 영상에 라플라시안 영상을 더해서 복원
restored = bigger + laplacian

merged = np.hstack((img, laplacian, bigger, restored))
cv2.imshow('Laplacian Pyramid', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
