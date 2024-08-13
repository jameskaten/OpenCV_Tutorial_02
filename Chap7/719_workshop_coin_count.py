import cv2
import numpy as np

img = cv2.imread('../img/coins_connected.jpg')
rows, cols = img.shape[:2]
cv2.imshow('original', img)

# 동전 표면을 흐릿하게 피라미드 평균 시프트 적용
mean = cv2.pyrMeanShiftFiltering(img, 20, 50)
cv2.imshow('mean', mean)
# Binary image
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh)
# 거리 변환
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 3)
# 거리 값을 0~255로 변환
dst = (dst/(dst.max() - dst.min()) * 255).astype(np.uint8)
cv2.imshow('dst', dst)

# 거리 변환 결과에서 로컬 최대값 구하기
# 팽창 적용 (동전 크기 정도의 구조화 요소 필요)
localMx = cv2.dilate(dst, np.ones((50,50), np.uint8))
# local max값을 저장할 배열 생성
lm = np.zeros((rows, cols), np.uint8)
# 팽창 적용 전 이미지와 같은 픽셀이 로컬 최대값이므로 255로 설정
lm[(localMx==dst) & (dst != 0)] = 255
cv2.imshow('localMx', lm)

# local Max 값으로 색 채우기
# local max 값이 있는 좌표 구하기
seeds = np.where(lm==255)
seed = np.stack((seeds[1], seeds[0]), axis=-1)
# 색 채우기를 위한 채우기 마스크 생성
fill_mask = np.zeros((rows+2, cols+2), np.uint8)
for x,y in seed:
    # local max값을 시드로 해서 평균 시프트 영상에 색 채우기
    ret = cv2.floodFill(mean, fill_mask, (x,y), (255,255,255), (10,10,10), (10,10,10))
cv2.imshow('floodFill', mean)

# 색 채우기를 적용한 영상에 다시 거리 변환 적용
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
dst = ((dst/(dst.max() - dst.min())) * 255).astype(np.uint8)
cv2.imshow('dst2', dst)

# 거리 변환 결과 값의 절반 이상을 차지한 영역은 확실한 전경으로 설정
ret, sure_fg = cv2.threshold(dst, 0.5*dst.max(), 255, 0)
cv2.imshow('sure_fg', sure_fg)

# 거리 변환 결과를 반전해서 확실한 배경 찾기
_, bg_th = cv2.threshold(dst, 0.3*dst.max(), 255, cv2.THRESH_BINARY_INV)
bg_dst = cv2.distanceTransform(bg_th, cv2.DIST_L2, 5)
bg_dst = ((bg_dst / (bg_dst.max() - bg_dst.min())) * 255).astype(np.uint8)
ret, sure_bg = cv2.threshold(bg_dst, 0.3*bg_dst.max(), 255, cv2.THRESH_BINARY)
cv2.imshow('sure_bg', sure_bg)

# 불확식한 영역 설정: 확실한 배경을 반전해서 확실한 전경을 빼기
ret, inv_sure_bg = cv2.threshold(sure_bg, 127, 255, cv2.THRESH_BINARY_INV)
unknown = cv2.subtract(inv_sure_bg, sure_fg)
cv2.imshow('unknown', unknown)

# 연결된 요소 labeling
_, markers = cv2.connectedComponents(sure_fg)

# lageling을 1씩 증가시키고 label을 알 수 없는 영역을 0번 label로 설정
markers = markers+1
markers[unknown == 255] = 0
print("before watershed: ", np.unique(markers))
colors = []
marker_show = np.zeros_like(img)
for mid in np.unique(markers):      # 선택한 마커 아이디 개수만큼 반복
    color = [int(j) for j in np.random.randint(0,255,3)]
    colors.append((mid, color))
    marker_show[markers==mid] = color
    coords = np.where(markers==mid)
    x, y = coords[1][0], coords[0][0]
    cv2.putText(marker_show, str(mid), (x+20, y+20), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255))
cv2.imshow('before', marker_show)

# Labeling이 완성된 marker를 이용하여 watershed 적용
markers = cv2.watershed(img, markers)
print("after watershed: ", np.unique(markers))

for mid, color in colors:       # 선택한 마커 아이디 개수만큼 반복
    marker_show[markers==mid] = color
    coords = np.where(markers==mid)
    if coords[0].size <= 0:
        continue
    x, y = coords[1][0], coords[0][0]
    cv2.putText(marker_show, str(mid), (x+20, y+20), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255))

marker_show[markers==-1] = (0,255,0)
cv2.imshow('watershed marker', marker_show)

img[markers==-1] = (0,255,0)
cv2.imshow('watershed', img)

# 동전 추출을 위한 마스킹 생성
mask = np.zeros((rows, cols), np.uint8)
# background mask
mask[markers!=1] = 255
# remove background
nobg = cv2.bitwise_and(img, img, mask=mask)
# 동전만 있는 label (배경(1), 경계(-1) 없는)
coin_label = [l for l in np.unique(markers) if (l != 1 and l != -1)]
# 동전 리벨을 순회하면서 동전 영역만 추출
for i, label in enumerate(coin_label):
    mask[:,:] = 0
    # 해당 동전 추출 마스크 생성
    mask[markers == label] = 255
    # 동전 영역만 마스크로 추출
    coins = cv2.bitwise_and(img, img, mask=mask)
    # 동전 하나만 있는 곳에서 최외곽 컨투어 추출
    contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
    # 동전을 감싸는 사각형 좌표
    x,y,w,h = cv2.boundingRect(contour[0])
    # 동전 영역만 추출해서 출력
    coin = coins[y:y+h, x:x+w]
    cv2.imshow('coin%d'%(i+1), coin)
    cv2.imwrite('../img/coin_test/coin%d.jpg'%(i+1), coin)
cv2.waitKey()
cv2.destroyAllWindows()





