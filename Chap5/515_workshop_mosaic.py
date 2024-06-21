import cv2

rate = 15
win_title = 'mosaic'
img = cv2.imread('../img/taekwonv1.jpg')

while True:
    x,y,w,h = cv2.selectROI(win_title, img, False)      # 관심영역
    if w and h:
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (w//rate, h//rate))   #1/rate 비율로 축소
        # 원래 크기로 확대
        roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)
        img[y:y+h, x:x+w] = roi
        cv2.imshow(win_title, img)
    else:
        break

cv2.destroyAllWindows()
