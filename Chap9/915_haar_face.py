import numpy as np
import cv2

# face cascade classifier
face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')
# eye detect
eye_cascade = cv2.CascadeClassifier('../data/haarcascade_eye.xml')
# image read and gray scale
img = cv2.imread('../img/children.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face
faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    # rectangle
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    # face area roi
    roi = gray[y:y+h, x:x+w]
    # eye
    eyes = eye_cascade.detectMultiScale(roi)
    # rectangle
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img[y:y+h, x:x+w], (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyWindow()