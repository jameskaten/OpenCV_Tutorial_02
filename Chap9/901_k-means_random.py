import numpy as np, cv2
import matplotlib.pyplot as plt

# 0~150 random number,
a = np.random.randint(0, 150, (25, 2))
# 128~255
b = np.random.randint(128, 255, (25, 2))
# combine a and b
data = np.vstack((a, b)).astype(np.float32)
# stop
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# AVERAGE CLUSTERING
ret,label,center=cv2.kmeans(data,2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Result by label
red = data[label.ravel()==0]
blue = data[label.ravel()==1]

# plt
plt.scatter(red[:,0], red[:,1], c='r')
plt.scatter(blue[:,0], blue[:,1], c='b')
# center
plt.scatter(center[0,0], center[0,1], s=100, c='r', marker='s')
plt.scatter(center[1,0], center[1,1], s=100, c='b', marker='s')
plt.show()
