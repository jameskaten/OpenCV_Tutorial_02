# Import required libraries
import cv2      # OpenCV library for image processing
import numpy as np    # NumPy library for numerical operations

# Read the image in three different ways:

# 1. Default reading mode (same as IMREAD_COLOR)
# This loads the image in BGR color format
img = cv2.imread('../img/OpenCV_logo_black.png')

# 2. Explicit color reading mode
# IMREAD_COLOR: Loads image in BGR color format (8-bit per channel)
bgr = cv2.imread('../img/OpenCV_logo_black.png', cv2.IMREAD_COLOR)

# 3. Read with alpha channel
# IMREAD_UNCHANGED: Loads image as-is including alpha channel (transparency)
# Results in BGRA format where A is the alpha channel
bgra = cv2.imread('../img/OpenCV_logo_black.png', cv2.IMREAD_UNCHANGED)

# Print the shape of each loaded image
# Shape format is (height, width, channels)
# - BGR images have 3 channels
# - BGRA images have 4 channels (including alpha)
print("default: ", img.shape, "color: ", bgr.shape, "unchanged: ", bgra.shape)

# Display the different versions of the image
cv2.imshow('bgr', bgr)      # Show BGR version
cv2.imshow('bgra', bgra)    # Show BGRA version (with alpha)
cv2.imshow('alpha', bgra[:,:,3])  # Show only the alpha channel (4th channel)

# Wait for any key press (0 means wait indefinitely)
cv2.waitKey(0)

# Clean up and close all windows
cv2.destroyAllWindows()
