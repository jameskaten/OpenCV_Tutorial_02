import cv2
import numpy as np

# Create a blank white image
# np.full parameters:
#   - shape: (500, 500, 3) means 500x500 pixels with 3 color channels (BGR)
#   - value: 255 means white (in all channels)
#   - dtype: np.uint8 means 8-bit unsigned integer (0-255 range)
img = np.full((500, 500, 3), 255, dtype=np.uint8)

# Save the blank white image
cv2.imwrite('../img/blank_500.jpg', img)