import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading a gray scale
img = cv2.imread("../img/yate.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

# equalize manually
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) #Histogram calc
cdf = hist.cumsum()         # cumulative histogram
cdf_m = np.ma.masked_equal(cdf, 0)          # 0 인 값을 NaN으로 제거
cdf_m = (cdf_m - cdf_m.min()) / (rows * cols) * 255     #equalize histogram
cdf = np.ma.filled(cdf_m, 0).astype('uint8')        #NaN을 다시 0으로 환원
img2 = cdf[img]         # mapping histogram as pixel

# OpenCV API로 equalize 적용
img3 = cv2.equalizeHist(img)

# Calc equalize histogram
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

# result
cv2.imshow('Before', img)
cv2.imshow('Manual', img2)
cv2.imshow('cv2.equalizeHist()', img3)
hists = {'Before':hist, 'Manual':hist2, 'cv2.equalizeHist()':hist3}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1,3,i+1)
    plt.title(k)
    plt.plot(v)

plt.show()
