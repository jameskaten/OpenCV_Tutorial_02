# Import required libraries
import cv2                        # OpenCV library for image processing
from matplotlib import pyplot as plt   # Matplotlib for image display

# Read an image file using OpenCV
# cv2.imread() loads the image in BGR format
# '../img/Chris01.jpg' specifies the path to the image file
# The '../' means go up one directory level from current location
img = cv2.imread('../img/Chris01.jpg')

# Display the image using matplotlib
# Note: imshow() expects RGB format, but OpenCV loads in BGR
# This might cause colors to appear incorrect (blue and red channels swapped)
plt.imshow(img)

# Show the plot window with the image
# This command is required to actually display the image
plt.show()