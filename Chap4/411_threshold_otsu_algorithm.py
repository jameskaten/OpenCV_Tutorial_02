# Import required libraries
import cv2          # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for image display

# Read the image in grayscale mode
# IMREAD_GRAYSCALE: Loads image as single-channel grayscale
# Using scanned paper image which has text - good for demonstrating Otsu's method
img = cv2.imread('../img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)

# Method 1: Simple Binary Thresholding
# Using fixed threshold value of 130
# Parameters:
#   - src: source image
#   - thresh: threshold value (130)
#   - maxval: maximum value (255)
#   - type: thresholding type (THRESH_BINARY)
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

# Method 2: Otsu's Thresholding
# Automatically determines optimal threshold value
# Parameters:
#   - src: source image
#   - thresh: ignored when using THRESH_OTSU (-1)
#   - maxval: maximum value (255)
#   - type: THRESH_BINARY | THRESH_OTSU
# Returns:
#   - t: computed optimal threshold value
#   - t_otsu: thresholded image
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold: ', t)  # Print the automatically determined threshold

# Create dictionary of images for display
imgs = {'Original': img,          # Original grayscale image
        't:130': t_130,          # Fixed threshold result
        'otsu:%d'%t: t_otsu}     # Otsu threshold result with computed value

# Display all results using matplotlib
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)         # Create 1x3 subplot grid
    plt.title(key)                 # Set title for each subplot
    plt.imshow(value, cmap='gray') # Display image in grayscale
    plt.xticks([])                 # Hide x-axis ticks
    plt.yticks([])                 # Hide y-axis ticks

# Show the plot window
plt.show()

