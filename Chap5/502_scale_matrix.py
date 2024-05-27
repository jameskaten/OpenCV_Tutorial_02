import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
height, width = img.shape[:2]

# 0.5x scale
m_small = np.float32([[0.5, 0, 0],
                      [0, 0.5, 0]])
# 2x scale
m_big = np.float32([[2, 0, 0],
                    [0, 2, 0]])

# 보간법없이 확대, 축소
dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
dst2 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)))

# 보간법 적용한 확대/축소
dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)),\
                      None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)), \
                      None, cv2.INTER_CUBIC)

# Result
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.imshow("small INTER_AREA", dst3)
cv2.imshow("big INTER_CUBIC", dst4)
cv2.waitKey()
cv2.destroyAllWindows()
