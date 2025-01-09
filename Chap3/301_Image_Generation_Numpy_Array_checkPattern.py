# Import required libraries
import cv2              # OpenCV library for image processing
import numpy as np      # NumPy library for numerical operations

# Create a black image of size 120x120 pixels
# np.zeros creates an array filled with zeros
# dtype=np.uint8 specifies 8-bit unsigned integers (0-255 range for grayscale)
img = np.zeros((120, 120), dtype=np.uint8)

# Create horizontal lines at different positions with different gray values
img[25:35, :] = 45     # Dark gray line from row 25 to 34
img[55:65, :] = 115    # Medium gray line from row 55 to 64
img[85:95, :] = 160    # Light gray line from row 85 to 94

# Create vertical lines at different positions with different gray values
img[:, 35:45] = 205    # Very light gray line from column 35 to 44
img[:, 75:85] = 255    # White line from column 75 to 84

# Display the resulting image
cv2.imshow('Gray', img)        # Show the image in a window titled 'Gray'
cv2.waitKey(0)                 # Wait for any key press
cv2.destroyAllWindows()        # Close all OpenCV windows