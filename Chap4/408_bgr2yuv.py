# Import required libraries
import cv2      # OpenCV library for image processing
import numpy as np    # NumPy library for numerical operations

# Create three different brightness levels in BGR color space
# Format: [[[Blue, Green, Red]]] with values 0-255
# All channels have same value to create grayscale colors
dark = np.array([[[0,0,0]]], dtype=np.uint8)      # Black pixel (0,0,0)
middle = np.array([[[127,127,127]]], dtype=np.uint8)  # Gray pixel (127,127,127)
bright = np.array([[[255,255,255]]], dtype=np.uint8)  # White pixel (255,255,255)

# Convert BGR colors to YUV color space
# YUV Components:
# Y: Luminance (brightness) - Similar to grayscale
# U: Blue projection (B-Y) - Blue-difference chroma
# V: Red projection (R-Y) - Red-difference chroma
dark_yuv = cv2.cvtColor(dark, cv2.COLOR_BGR2YUV)     # Convert black to YUV
middle_yuv = cv2.cvtColor(middle, cv2.COLOR_BGR2YUV)  # Convert gray to YUV
bright_yuv = cv2.cvtColor(bright, cv2.COLOR_BGR2YUV)  # Convert white to YUV

# Print YUV values for each brightness level
# Format: [[[Y, U, V]]]
print("dark: ", dark_yuv)     # Should show low Y value, neutral U/V
print("middle: ", middle_yuv)  # Should show medium Y value, neutral U/V
print("bright: ", bright_yuv)  # Should show high Y value, neutral U/V