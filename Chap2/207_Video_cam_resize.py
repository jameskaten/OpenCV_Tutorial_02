import cv2

cap = cv2.VideoCapture(0)       # connect #0 camera
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Original width: %d, height:%d", (width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)      # resize
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)     # resize
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resized width: %d, height: %d" %(width, height))

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
