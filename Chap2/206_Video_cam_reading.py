import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():      # Initialization
    while True:
        ret, img = cap.read()   # read next frame
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
