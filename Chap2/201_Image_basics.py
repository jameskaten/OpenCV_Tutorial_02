# Mac
import cv2
print(cv2.__version__)

# Image Loading

img_file = "../img/Chris01.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')