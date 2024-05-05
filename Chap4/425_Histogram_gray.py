import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../img/mountain.jpg")
cv2.imshow('img', img)

# draw histogram
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

print(hist.shape)               #shape(256,1)
print(hist.sum(), img.shape)    #총 합계와 이미지의 크기
plt.show()
