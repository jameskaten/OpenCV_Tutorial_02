import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

img = cv2.imread("../img/man_face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# FACE Area
faces = detector(gray)
for rect in faces:
    x, y = rect.left(), rect.top()
    w, h = rect.right()-x, rect.bottom()-y
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)

    # face landmark
    shape = predictor(gray, rect)
    for i in range(68):
        part = shape.part(i)
        cv2.circle(img, (part.x, part.y), 2, (0,0,255), -1)
        cv2.putText(img, str(i), (part.x, part.y), cv2.FONT_HERSHEY_PLAIN, \
                    0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.imshow("face landmark", img)
cv2.waitKey(0)

