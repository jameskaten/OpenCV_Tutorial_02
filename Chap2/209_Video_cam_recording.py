import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():      # Initialization
    file_path = './record.avi'
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # encoding format
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    out = cv2.VideoWriter(file_path, fourcc, fps, size)
    while True:
        ret, frame = cap.read()   # read next frame
        if ret:
            cv2.imshow('camera-recording', frame)
            out.write(frame)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
    out.release()
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
