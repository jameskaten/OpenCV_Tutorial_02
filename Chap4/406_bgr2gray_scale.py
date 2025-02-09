# Import required libraries
import cv2      # OpenCV library for image processing
import numpy as np    # NumPy library for numerical operations

# Read the input image in BGR format
img = cv2.imread('../img/Chris04.jpg')

# Method 1: Manual Grayscale Conversion
# Convert image to 16-bit to prevent overflow during addition
img2 = img.astype(np.uint16)    

# Split the image into its BGR channels
# b: Blue channel
# g: Green channel
# r: Red channel
b,g,r = cv2.split(img2)         

# Calculate grayscale by averaging all channels
# (B + G + R) / 3
# Convert back to 8-bit format for display
gray1 = ((b + g + r)/3).astype(np.uint8)    

# Method 2: OpenCV's Built-in Conversion
# Uses weighted formula: 0.299R + 0.587G + 0.114B
# This better represents human perception of brightness
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display all versions of the image
cv2.imshow('original', img)    # Original BGR image
cv2.imshow('gray1', gray1)     # Simple average grayscale
cv2.imshow('gray2', gray2)     # Weighted grayscale (OpenCV method)

# Wait for any key press (0 means wait indefinitely)
cv2.waitKey(0)

# Clean up and close all windows
cv2.destroyAllWindows()
