import numpy as np, cv2

cap = cv2.VideoCapture('../img/walKing.avi')
fps = cap.get(cv2.CAP_PROP_FPS)         # Frame number
delay = int(1000/fps)

# background subtract
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # background subtract mask
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('bgsub', fgmask)
    if cv2.waitKey(1) & 0xff == 27:
        break
cap.release()
cv2.destroyWindow()

