import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gray scale
img = cv2.imread('../img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)

# boundary 130
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
# 경계값을 지정하지 않고 오츠의 알고리즘 선택
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold: ', t)

imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()

