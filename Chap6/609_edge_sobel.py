import cv2
import numpy as np

img = cv2.imread("../img/sudoku.png")

# sobel kernel
gx_k = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gy_k = np.array([[-1.-2.-1],[0,0,0],[1,2,1]])
#sobel filter
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# sobel API edge detection
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)

merged1 = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
merged2 = np.hstack((img, sobelx, sobely, sobelx+sobely))
merged = np.vstack((merged1, merged2))
cv2.imshow('sobel', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
