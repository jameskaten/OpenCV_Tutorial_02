import numpy as np, cv2

roi_hist = None     # 추적 객체 히스토그램 저장 변수
win_name = 'Camshift Tracking'
termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while cap.isOpened():
    ret, frame = cap.read()
    img_draw = frame.copy()

    if roi_hist is not None:    # 추적 대상 객체 히스토그램 등록 됨
        # 전체 영상 hsv 컬로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 전체 영상 히스토그램과 roi 히스토그램 역투영
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)
        # 역 투영 결과와 초기 추적 위치로 평균 이동 추적
        ret, (x,y,w,h) = cv2.CamShift(dst, (x,y,w,h), termination)
        # 새로운 위치에 사각현 표시
        cv2.rectangle(img_draw, (x,y), (x+w, y+h), (0,255,0),2)
        # 컬러 영상과 역투영 영상을 통합해서 출력
        result = np.hstack((img_draw, cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)))
    else:       # 추적 대상 객체 히스토그램 등록 안됨
        cv2.putText(img_draw, "Hit the Space to set target to track", \
                    (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),1,cv2.LINE_AA)
        result = img_draw

    cv2.imshow(win_name, result)
    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord(' '):   # Space bar, ROI 설정
        x,y,w,h = cv2.selectROI(win_name, frame, False)
        if w and h:     # ROI   가 제대로 설정됨
            # 초기 추적 대상 위치로 ROI 설정
            roi = frame[y:y+h, x:x+w]
            # roi를 HSV 컬러로 변경
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            mask = None
            # roi에 대한 히스토그램 계산
            roi_hist = cv2.calcHist([roi], [0], mask ,[180], [0,180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
        else:
            roi_hist = None
else:
    print('No camera!')
cap.release()
cv2.destroyWindow()
