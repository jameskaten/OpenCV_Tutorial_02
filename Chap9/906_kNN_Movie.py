import cv2
import numpy as np
import matplotlib.pyplot as plt

# 0~99 random value 25x2
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# trainDatat[0]:kick, trainData[1]:kiss, kick > kiss ? 1: 0
responses = (trainData[:, 0] > trainData[:,1]).astype(np.float32)
# 0: action : 1romantic
action = trainData[responses==0]
romantic = trainData[responses==1]
# action은 blue triangle, romantic: red circle
plt.scatter(action[:,0],action[:,1],80,'b','^', label='action')
plt.scatter(romantic[:,0],romantic[:,1],80,'r','o',label="romantic")
# new data, 0~99 random numbers 1x2, green rectangle
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],200,'g','s',label="new")

# Knearest algorithm creation and train
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

ret, results, neighbors, dist = knn.findNearest(newcomer, 3)    #K = 3
print("ret:%s, result:%s, neighbors:%s, dist:%s" \
      %(ret, results, neighbors, dist))

# new result arrow
anno_x, anno_y = newcomer.ravel()
label = "action" if results ==0 else "romantic"
plt.annotate(label, xy=(anno_x + 1, anno_y+1), \
             xytext=(anno_x+5, anno_y+10), arrowprops={'color':'black'})
plt.xlabel('kiss')
plt.ylabel('kick')
plt.legend(loc="upper right")
plt.show()