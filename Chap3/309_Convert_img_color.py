import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img/Chris01.jpg')

plt.imshow(img[:,:,::-1])
plt.xticks([])      # Remove ticks
plt.yticks([])
plt.show()