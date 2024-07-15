import cv2
import numpy as np
import time

img = cv2.imread('../img/JYPark.jpg')
rows, cols = img.shape[:2]

# 뒤집기 변환행렬로 생성
st = time.time()
mflip = np.float32([[-1,0,cols-1], [0,-1,rows-1]])  # transform matrix
fliped1 = cv2.warpAffine(img, mflip, (cols, rows))
print('matrix:', time.time()-st)

# remap 함수로 뒤집기 구현
st2 = time.time()
mapy, mapx = np.indices((rows, cols), dtype=np.float32)     # mapping matrix initialization
mapx = cols - mapx -1       # 뒤집기 연산
mapy = rows - mapy -1       # 뒤집기 연산
fliped2 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
print('remap:', time.time()-st2)

# Result
cv2.imshow('origin', img)
cv2.imshow('fliped1', fliped1)
cv2.imshow('fliped2', fliped2)
cv2.waitKey()
cv2.destroyAllWindows()


