import cv2

video_file = "../img/Angela.mp4"

cap = cv2.VideoCapture(video_file)
if cap.isOpened():      # Initialization
    fps = cap.get(cv2.CAP_PROP_FPS) # Frame number by second
    delay = int(1000/fps)           # delay time
    print("FPS: %f, Delay: %dms" %(fps, delay))

    while True:
        ret, img = cap.read()   # read next frame
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
