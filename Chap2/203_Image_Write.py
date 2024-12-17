import cv2

# Image Loading

img_file = "../img/Chris02.jpg"
save_file = "Chris02_saved.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)       # Reading Gray scale
cv2.imshow('IMG', img)
cv2.imwrite(save_file, img)         # Save file
cv2.waitKey()
cv2.destroyAllWindows()
