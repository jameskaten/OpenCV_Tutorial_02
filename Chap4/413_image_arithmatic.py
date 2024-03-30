import cv2
import numpy as np

# array
a = np.uint8([[200, 50]])
b = np.uint8([[100, 100]])

# Numpy array
add1 = a + b
sub1 = a - b
mult1 = a * 2
div1 = a / 3

# OpenCV API를 이용한 연산
add2 = cv2.add(a, b)
sub2 = cv2.subtract(a, b)
mult2 = cv2.multiply(a, 2)
div2 = cv2.divide(a, 3)

# Print results
print(add1, add2)
print(sub1, sub2)
print(mult1, mult2)
print(div1, div2)