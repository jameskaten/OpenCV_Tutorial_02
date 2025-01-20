# Import required libraries
import cv2              # OpenCV library for image processing
import numpy as np      # NumPy library for numerical operations

# Create a black image of size 120x120 pixels with 3 color channels (BGR)
# Shape is (height, width, channels) where channels=3 for BGR
# dtype=np.uint8 specifies 8-bit unsigned integers (0-255 range for each color)
img = np.zeros((120, 120, 3), dtype=np.uint8)

# Create horizontal lines with different colors
img[25:35, :] = [255,0,0]     # Blue line (BGR format) from row 25 to 34
img[55:65, :] = [0,255,0]     # Green line from row 55 to 64
img[85:95, :] = [0,0,255]     # Red line from row 85 to 94

# Create vertical lines with mixed colors
img[:, 35:45] = [255,255,0]   # Cyan line (Blue + Green) from column 35 to 44
img[:, 75:85] = [255,0,255]   # Magenta line (Blue + Red) from column 75 to 84

# Display the resulting image
cv2.imshow('BGR', img)         # Show the image in a window titled 'BGR'
cv2.waitKey(0)                 # Wait for any key press
cv2.destroyAllWindows()        # Close all OpenCV windows