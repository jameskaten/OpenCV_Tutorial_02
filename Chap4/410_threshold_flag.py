# Import required libraries
import cv2          # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for image display

# Read the image in grayscale mode
# IMREAD_GRAYSCALE: Loads image as single-channel grayscale
img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

# Apply different thresholding methods
# Parameters for cv2.threshold:
#   - src: source image
#   - thresh: threshold value (127)
#   - maxval: maximum value to use (255)
#   - type: thresholding type

# Binary Thresholding
# Pixels > thresh -> maxval
# Pixels <= thresh -> 0
_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Inverse Binary Thresholding
# Pixels > thresh -> 0
# Pixels <= thresh -> maxval
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Truncate Thresholding
# Pixels > thresh -> thresh
# Pixels <= thresh -> unchanged
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# Threshold to Zero
# Pixels > thresh -> unchanged
# Pixels <= thresh -> 0
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# Inverse Threshold to Zero
# Pixels > thresh -> 0
# Pixels <= thresh -> unchanged
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# Create dictionary of images for display
imgs = {'origin': img,           # Original grayscale image
        'BINARY': t_bin,         # Binary threshold result
        'BINARY_INV': t_bininv,  # Inverse binary result
        'TRUNC': t_truc,         # Truncate result
        'TOZERO': t_2zr,         # Threshold to zero result
        'TOZERO_INV': t_2zrinv}  # Inverse threshold to zero result

# Display all results using matplotlib
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)         # Create 2x3 subplot grid
    plt.title(key)                   # Set title for each subplot
    plt.imshow(value, cmap='gray')   # Display image in grayscale
    plt.xticks([])                   # Hide x-axis ticks
    plt.yticks([])                   # Hide y-axis ticks

# Show the plot window
plt.show()



