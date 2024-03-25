# this file explains Key Events

import cv2

img_file = "../img/Chris01.jpg"
img = cv2.imread(img_file)
title = 'IMG'
x, y = 100, 100     #initial coordinate

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무한 대기, 8비트 마스크 처리
    print(key, chr(key))    # print key character
    if key == ord('h'):
        x -= 10
    elif key == ord('j'):
        y += 10
    elif key == ord('k'):
        y -= 10
    elif key == ord('l'):
        x += 10
    elif key == ord('q') or key == 27:  #esc
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)