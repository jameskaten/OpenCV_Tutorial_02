# Import required libraries
import cv2      # OpenCV library for image processing
import numpy as np    # NumPy library for numerical operations

# Read the input image from file
img = cv2.imread('../img/Chris01.jpg')

# Use OpenCV's built-in ROI selector
# Parameters:
#   'img': Window name
#   img: Source image
#   False: ShowCrosshair flag (whether to show crosshair in selection)
# Returns: tuple (x, y, w, h) where:
#   x, y: Top-left corner coordinates of selection
#   w, h: Width and height of selection
x,y,w,h = cv2.selectROI('img', img, False)

# Check if a valid selection was made (both width and height are non-zero)
if w and h:
    # Extract the ROI using array slicing
    # Format: img[y:y+h, x:x+w] where:
    #   y:y+h - Vertical slice from y to y+h
    #   x:x+w - Horizontal slice from x to x+w
    roi = img[y:y+h, x:x+w]
    
    # Display the cropped ROI in a new window
    cv2.imshow('cropped', roi)
    
    # Move the cropped window to the top-left corner of screen
    cv2.moveWindow('cropped', 0, 0)
    
    # Save the cropped ROI to a file
    cv2.imwrite('./cropped.jpg', roi)

# Display the original image
cv2.imshow('img', img)

# Wait for any key press (0 means wait indefinitely)
cv2.waitKey(0)

# Clean up and close all windows
cv2.destroyAllWindows()