# This file demonstrates various window operations in OpenCV
# including window creation, positioning, and resizing

import cv2

# Load image in both color and grayscale formats
file_path = '../img/Chris02.jpg'
img = cv2.imread(file_path)                          # Load color image
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Load grayscale image

# Create windows with different behaviors
# WINDOW_AUTOSIZE: Window size matches image size, cannot be resized manually
cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)   

# WINDOW_NORMAL: Window can be resized manually by user
# Useful when dealing with large images or when you need flexible window sizes
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)

# Display both images in their respective windows
cv2.imshow('origin', img)      # Show color image in 'origin' window
cv2.imshow('gray', img_gray)   # Show grayscale image in 'gray' window

# Position windows on screen
# moveWindow(window_name, x, y) - positions top-left corner of window
cv2.moveWindow('origin', 0, 0)        # Position 'origin' window at (0,0)
cv2.moveWindow('gray', 100, 100)      # Position 'gray' window at (100,100)

# Wait for user input before proceeding
cv2.waitKey(0)

# Resize windows programmatically
# Note: Only works for WINDOW_NORMAL windows
cv2.resizeWindow('origin', 200, 200)  # Try to resize 'origin' window (won't work due to AUTOSIZE)
cv2.resizeWindow('gray', 100, 100)    # Resize 'gray' window to 100x100

# Wait for user input again
cv2.waitKey(0)

# Close specific window
cv2.destroyAllWindows("gray")  # Close only the 'gray' window

# Wait for final user input
cv2.waitKey(0)

# Clean up: close all remaining windows
cv2.destroyAllWindows()