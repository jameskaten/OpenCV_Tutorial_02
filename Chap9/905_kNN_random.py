import cv2, numpy as np, matplotlib.pyplot as plt

# 0~200 사이의 무작위 수 50x2개 데이터 생성
red = np.random.randint(0, 110, (25, 2)).astype(np.float32)
blue = np.random.randint(90, 200, (25,2)).astype(np.float32)
trainData = np.vstack((red, blue))

# 50x1 label
labels = np.zeros((50,1), dtype=np.float32)     # 0: red triangle
labels[25:] = 1     # 1: blue rectangle

# 레이블 값 0과 같은 자리는 red, 1과 같은 자리는 blue로 분류해서 표시
plt.scatter(red[:, 0], red[:,1], 80, 'r', '^')  # red triangle
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 'o')     # green circle

# 0~200 사이의 새로운 무작위 수 생성
newcomer = np.random.randint(0,200,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')     # green circle

# kNN algorithm object
knn = cv2.ml.KNearest_create()
# train, 행 단위 샘플
knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)
# prediction
# ret, results = knn.predict(newcomer)
ret, results, neighbors, dist = knn.findNearest(newcomer, 3)    # K = 3

print('ret:%s, result:%s, neighbors:%s, distance:%s' \
      %(ret, results, neighbors, dist))
plt.annotate('red' if ret==0.0 else 'blue', xy=newcomer[0],\
             xytext=(newcomer[0]+1))
plt.show()

