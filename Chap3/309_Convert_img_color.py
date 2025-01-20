# Import required libraries
import cv2                        # OpenCV library for image processing
from matplotlib import pyplot as plt   # Matplotlib for image display

# Read an image file using OpenCV
# cv2.imread() loads the image in BGR format
# '../img/Chris01.jpg' specifies the path to the image file
# The '../' means go up one directory level from current location
img = cv2.imread('../img/Chris01.jpg')

# Display the image using matplotlib with color correction
# img[:,:,::-1] performs color channel reordering:
#   - First ':' means select all rows
#   - Second ':' means select all columns
#   - '::-1' means reverse the order of color channels (BGR → RGB)
# This is a quick way to convert BGR to RGB format
plt.imshow(img[:,:,::-1])

# Remove x-axis ticks for cleaner display
plt.xticks([])

# Remove y-axis ticks for cleaner display
plt.yticks([])

# Show the plot window with the correctly colored image
plt.show()