import cv2
import numpy as np

#BGR Color Space  to pixel
red_bgr = np.array([[[0,0,255]]], dtype=np.uint8)
green_bar = np.array([[[0,255,0]]], dtype=np.uint8)
blue_bar = np.array([[[255,0,0]]], dtype=np.uint8)
yellow_bar = np.array([[[0,255,255]]], dtype=np.uint8)

# Convert BGR TO HSV
red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV);
green_hsv = cv2.cvtColor(green_bar, cv2.COLOR_BGR2HSV);
blue_hsv = cv2.cvtColor(blue_bar, cv2.COLOR_BGR2HSV);
yellow_hsv = cv2.cvtColor(yellow_bar, cv2.COLOR_BGR2HSV);

# HSV로 변환된 픽셀 출력
print("red: ", red_hsv)
print("green: ", green_hsv)
print("blue: ", blue_hsv)
print("yellow: ", yellow_hsv)
