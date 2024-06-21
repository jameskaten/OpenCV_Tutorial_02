import cv2
import numpy as np

win_title = 'Liquify'
half = 50           # 관심영역 절반 크기
isDragging = False  # 드래그 여부 플래그

def liquify(img, cx1, cy1, cx2, cy2):
    # 대상 영역 좌표와 크기 설정
    x, y, w, h = cx1-half, cy1-half, half*2, half*2
    # 관심영역 설정
    roi = img[y:y+h, x:x+w].copy()
    out = roi.copy()

    # 관심영역 기준으로 좌표 재설정
    offset_cx1, offset_cy1 = cx1-x, cy1-y
    offset_cx2, offset_cy2 = cx2-x, cy2-y

    # 변환 이전 4개의 삼각형 좌표
    tri1 = [[[0,0], [w,0], [offset_cx1, offset_cy1]],   #top
            [[0,0], [0,h], [offset_cx1, offset_cy1]],   #left
            [[w,0], [offset_cx1, offset_cy1], [w,h]],   #right
            [[0,h], [offset_cx1, offset_cy1], [w,h]]]   #bottom

    #변환 이후 4개의 삼각형 좌표
    tri2 = [[[0,0], [w,0], [offset_cx2, offset_cy2]],  # top
            [[0,0], [0,h], [offset_cx2, offset_cy2]],  # left
            [[w,0], [offset_cx2, offset_cy2], [w,h]],  # right
            [[0,h], [offset_cx2, offset_cy2], [w,h]]]  # bottom

    for i in range(4):
        #각각의 삼각형 좌표에 대해 어핀 변환 적용
        matrix = cv2.getAffineTransform(np.float32(tri1[i]),
                                        np.float32(tri2[i]))
        warped = cv2.warpAffine(roi.copy(), matrix, (w,h),
                                None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
        # 삼각형 모양의 마스크 생성
        mask = np.zeros((h,w), dtype=np.uint8)
        cv2.fillConvexPoly(mask, np.int32(tri2[i]), (255,255,255))

        #마스킹 후 합성
        warped = cv2.bitwise_and(warped, warped, mask=mask)
        out = cv2.bitwise_and(out, out, mask=cv2.bitwise_not(mask))
        out = out + warped

    # 관심영역을 원본 영상에 합성
    img[y:y+h, x:x+w] = out
    return img

# 마우스 이벤트 핸들 함수
def onMouse(event, x, y, flags, param):
    global cx1, cy1, isDragging, img
    #마우스 중심점을 기준으로 대상 영역 따라다니기
    if event == cv2.EVENT_MOUSEMOVE:
        if not isDragging:
            img_draw = img.copy()
            # 드래그 영역 표시
            cv2.rectangle(img_draw, (x-half, y-half),
                       (x+half, y+half), (0,255,0))
            cv2.imshow(win_title, img_draw)
    elif event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        cx1, cy1 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            # 드래그 시작 좌표와 끝 좌표로 리퀴파이 적용 함수 호출
            liquify(img, cx1, cy1, x, y)
            cv2.imshow(win_title, img)

if __name__ == '__main__':
    img = cv2.imread("../img/man_face.jpg")
    h,w = img.shape[:2]

    cv2.namedWindow(win_title)
    cv2.setMouseCallback(win_title, onMouse)
    cv2.imshow(win_title, img)
    while True:
        key = cv2.waitKey(1)
        if key & 0xFF ==27:
            break
    cv2.destroyAllWindows()


