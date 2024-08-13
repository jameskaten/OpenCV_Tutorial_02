import cv2
import numpy as np

img = cv2.imread('../img/taekwonv1.jpg')
img_draw = img.copy()
mask = np.zeros(img.shape[:2], dtype=np.uint8)
rect = [0,0,0,0]
mode = cv2.GC_EVAL  # Grabcut 초기 모드
# 배경 및 전경 모델 버퍼
bgdmodel = np.zeros((1,65), np.float64)
fgdmodel = np.zeros((1,65), np.float64)

def onMouse(event, x, y, flags, param):
    global mouse_mode, rect, mask, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags <= 1:  # 아무 키도 안 눌렀으면
            mode = cv2.GC_INIT_WITH_RECT    # 드래그 시작, 사각형 모드
            rect[:2] = x, y     # save the starting coordinate
    # Mouse starting to move, Lbutton down
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        if mode == cv2.GC_INIT_WITH_RECT:   # drag
            img_temp = img.copy()
            # show the drag rectangle
            cv2.rectangle(img_temp, (rect[0], rect[1]), (x,y), (0,255,0), 2)
            cv2.imshow('img', img_temp)
        elif flags > 1:     # Key pushed
            mode == cv2.GC_INIT_WITH_MASK       # Mask mode
            if flags & cv2.EVENT_FLAG_CTRLKEY:  # Cntr key
                # show a white dot
                cv2.circle(img_draw, (x,y), 3, (255,255,255), -1)
                # 마스크에 GC_FGD로 채우기
                cv2.circle(mask, (x,y),3,cv2.GC_FGD,-1)
            if flags & cv2.EVENT_FLAG_SHIFTKEY:     #Shift key
                # show a black dot
                cv2.circle(img_draw, (x,y), 3,(0,0,0), -1)
                cv2.circle(mask, (x,y), 3, cv2.GC_BGD, -1)
            cv2.imshow('img', img_draw)     # 그려진 모습을 출력
    elif event == cv2.EVENT_LBUTTONUP:
        if mode == cv2.GC_INIT_WITH_RECT:   # 사각형 그리기 종료
            rect[2:] = x,y      # 사각형 마지막 좌표
            cv2.rectangle(img_draw, (rect[0], rect[1]), (x,y), (255,0,0), 2)
            cv2.imshow('img', img_draw)
        # Grabcut
        cv2.grabCut(img, mask, tuple(rect), bgdmodel, fgdmodel, 1, mode)
        img2 = img.copy()
        # 마스크에 확실한 배경, 아마도 배경으로 표시된 영역을 0으로 채우기
        img2[(mask==cv2.GC_BGD)| (mask==cv2.GC_PR_BGD)] = 0
        cv2.imshow('grabcut', img2)
        mode = cv2.GC_EVAL      # grabcut mode reset

cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)    # set the event
while True:
    if cv2.waitKey(0) & 0xFF ==27:  #esc
        break
cv2.destroyAllWindows()


