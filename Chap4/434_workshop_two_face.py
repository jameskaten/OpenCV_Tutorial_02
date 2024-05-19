import cv2
import numpy as np

# 영상의 15%를 알파 블렌딩의 범위로 지정
alpha_width_rate = 15

img_face = cv2.imread('../img/man_face.jpg')
img_skull = cv2.imread('../img/skull.jpg')

#입력 영상과 같은 크기의 결과 영상 준비
img_comp = np.zeros_like(img_face)

# coordinate
height, width = img_face.shape[:2]
middle = width//2
alpha_width = width * alpha_width_rate // 100  #blending 범위
start = middle - alpha_width//2
step = 100/alpha_width

# 입력 영상의 절반씩 복사해서 결과 영상에 합성
img_comp[:, :middle, :] = img_face[:, :middle, :].copy()
img_comp[:, middle:, :] = img_skull[:, middle:, :].copy()
cv2.imshow('half', img_comp)

# 알파 값을 바꾸면서 앞라 블렌딩 적용
for i in range(alpha_width+1):
    alpha = (100 - step * i) / 100
    beta = 1 - alpha
    # alpha blending
    img_comp[:, start+i] = img_face[:, start+i] * \
        alpha + img_skull[:, start+i] * beta
    print(i, alpha, beta)

cv2.imshow('half skull', img_comp)
cv2.waitKey()
cv2.destroyAllWindows()