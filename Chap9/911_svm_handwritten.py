import cv2
import numpy as np
import mnist
import svm_mnist_hog_train

# 훈련해서 저장한 SVM 객체 읽기
svm = cv2.ml.SVM_load('./svm_mnist.xml')
# 인식한 손글씨 이미지 읽기
image = cv2.imread('../img/4027.png')
cv2.imshow("image", image)
cv2.waitKey(0)

# 인식할 이미지를 gray scale로 변환 및 thresdhold
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
_, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 최외곽 컨투어만 찾기
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, \
                               cv2.CHAIN_APPROX_SIMPLE)[-2:]
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    # 외접 사각형의 크기가 너무 작은것은 제외
    if w >= 5 and h >= 25:
        # 숫자 영역만 roi로 확보하고 사각형 그리기
        roi = gray[y:y + h, x:x + w]
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1)
        # test data type
        px20 = mnist.digit2data(roi, False)
        # 기울어진 숫자를 바로 세우기
        deskewed = svm_mnist_hog_train.deskew(px20)
        # 인식할 숫자에 대한 HOG 디스크립터 계산
        hogdata = svm_mnist_hog_train.hogDesc.compute(deskewed)
        testData = np.float32(hogdata).reshape(-1, hogdata.shape[0])
        # result
        ret, result = svm.predict(testData)
        cv2.putText(image, "%d"%result[0], (x, y+155), \
                    cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),2)
        cv2.imshow("image", image)
        cv2.waitKey(0)
cv2.destroyWindow()
