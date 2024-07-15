import cv2
import numpy as np

img = cv2.imread('../img/sudoku.png')

# differential kernel
gx_kernel = np.array([[-1, 1]])
gy_kernel = np.array([[-1], [1]])

# filter
edge_gx = cv2.filter2D(img, -1, gx_kernel)
edge_gy = cv2.filter2D(img, -1, gy_kernel)

# Result
merged = np.hstack((img, edge_gx, edge_gy))
cv2.imshow('edge', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()