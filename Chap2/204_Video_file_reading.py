import cv2

video_file = "../img/Angela.mp4"

cap = cv2.VideoCapture(video_file)          # video capture object
if cap.isOpened():      # Initialization
    while True:
        ret, img = cap.read()   # read next frame, ret: reading True/False
        if ret:                 # reading successful? 
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
