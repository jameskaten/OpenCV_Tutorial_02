import cv2

img = cv2.imread('../img/pistol.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (16,16))

# Average
avg = gray.mean()
# convert the average to 0 and 1
bin = 1 * (gray > avg)
print(bin)

# 2진수 문자열을 16진수 문자열로 변환
dhash = []
for row in bin.tolist():
    s = ''.join([str(i) for i in row])
    dhash.append('%02x'%(int(s,2)))
dhash = ''.join(dhash)
print(dhash)

cv2.imshow('postol', img)
cv2.waitKey(0)
