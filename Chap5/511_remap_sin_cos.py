import cv2
import numpy as np

l = 20  #wave length
amp = 15    # amplitude

img = cv2.imread('../img/taekwonv1.jpg')
rows,cols = img.shape[:2]

# 초기 매핑 배열 생성
mapy, mapx = np.indices((rows,cols), dtype=np.float32)

# sin, cos함수를 이용한 변형 매핑 연산
sinx = mapx + amp * np.sin(mapy/l)
cosy = mapy + amp * np.cos(mapx/l)

# 영상 remapping
img_sinx=cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR)   # x축만 sin곡선 적용
img_cosy=cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR)   # y 축만 cos곡선 적용

# x, y축 모두 sin, cos곡선 적용 및 외곽 영역 보정
img_both=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, \
                   None, cv2.BORDER_REPLICATE)

cv2.imshow('origin', img)
cv2.imshow('sin x', img_sinx)
cv2.imshow('cos y', img_cosy)
cv2.imshow('sin cos', img_both)

cv2.waitKey()
cv2.destroyAllWindows()