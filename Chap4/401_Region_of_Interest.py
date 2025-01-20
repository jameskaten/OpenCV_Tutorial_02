# Import required libraries
import cv2  # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations

# Read the image from file
img = cv2.imread('../img/Chris01.jpg')

# Define the region of interest (ROI) coordinates
x=320; y=150  # Starting coordinates (x,y) of the ROI
w=200; h=200  # Width and height of the ROI

# Extract the ROI using array slicing
# Format is img[y_start:y_end, x_start:x_end]
roi = img[y:y+h, x:x+w]

# Print the shape of ROI (height, width, channels)
print(roi.shape)

# Draw a green rectangle on the ROI with thick lines
# Parameters: image, start_point(0,0), end_point(h-1,w-1), color(0,255,0), thickness=3
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0), 20)

# Display the original image (which now includes the rectangle in the ROI)
cv2.imshow("img", img)

# Wait for any keyboard input (0 means wait indefinitely)
cv2.waitKey(0)

# Clean up and close all windows
cv2.destroyAllWindows()