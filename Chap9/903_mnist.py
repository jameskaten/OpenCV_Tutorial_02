import numpy as np, cv2

data = None
k = list(range(10))  # [0,1,2,3,4,5,6,7,8,9]

# reading image data
def load():
    global data
    # 0~9 각각 500(5x100)개, 총5000(50x100)개, 한 숫자당 400(20x20)픽셀
    image = cv2.imread('../img/digits.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 숫자 한개(20x20)씩 구분하기 위해 행별(50)로 나누고 열별(100)로 나누기
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
    # 리스트를 NumPy 배열로  변환 (50 x 100 x 20 x 20 )
    data = np.array(cells)

    # 모든 숫자 데이타 반환
    def getData(reshape=True):
        if data is None: load()  # reading image
        # 모든 데이터를 N X 400 형태로 변환
        if reshape:
            full = data.reshape(-1, 400).astype(np.float32) # 5000x400
        else:
            full = data
        labels = np.repeat(k, 500).reshape(-1, 1)   # 각 숫자당 500번 반복(10x500)
        return (full, labels)

    # 훈련용 데이터 반환
    def getTrain(reshape=True):
        if data is None: load()     # reading image
        # 50x100 중에 90열만 훈련 데이타로 사용
        train=data[:, :90]
        if reshape:
            # 훈련 데이타를 N X 400으로 변환
            train = train.reshape(-1, 400).astype(np.float32)   # 4500x400
        # create label
        train_labels = np.repeat(k,450).reshape(-1,1) # 각 숫자당 45번 반복 (10x450)
        return (train, train_labels)

    # 테스트용 데이타 반환
    def getTest(reshape=True):
        if data is None: load()
        # 50x100 중에 마지막 10열만 훈련 데이타로 사용
        test = data[:, 90:100]
        # test data를 N x 400으로 변환
        if reshape:
            test = test.reshape(-1,400).astype(np.float32) # 500x400
        test_labels = np.repeat(k,50).reshape(-1,1)
        return (test, test_labels)

    # 손글씨 숫자 한 개를 20x20로 변환 후에 1x400 형태로 변환
    def digit2data(src, reshape=True):
        h, w = src.shape[:2]
        square = src
        # square
        if h > w:
            pad = (h - w)//2
            square = np.zeros((h,h), dtype=np.uint8)
            square[:, pad:pad+w] = src
        elif w > h:
            pad = (w - h)//2
            square = np.zeros((w, w), dtype=np.uint8)
            square[pad:pad+h, :] = src
        # 0으로 채워진 20x20 이미지 생성
        px20 = np.zeros((20,20), np.uint8)
        # 원본을 16x16으로 축소해서 테두리 2픽셀 확보
        px20[2:18, 2:18] = cv2.resize(square, (16,16), interpolation=cv2.INTER_AREA)
        if reshape:
            # 1x400형태로 변환
            px20 = px20.reshape((1,400)).astype(np.float32)
        return px20

