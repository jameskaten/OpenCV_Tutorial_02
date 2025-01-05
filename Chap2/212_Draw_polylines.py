# This file draws polylines

import cv2
import numpy as np

# Load a blank white image (500x500 pixels)
img = cv2.imread('../img/blank_500.jpg')

# Define point arrays for different shapes
# Each point array contains [x,y] coordinates in sequence
# dtype=np.int32 ensures coordinates are stored as integers

# Thunder/Lightning bolt shape - 4 points
# Creates a zigzag pattern from top-left towards bottom-right
pts1 = np.array([[50, 50], [150, 150], [100, 140], [200, 240]], dtype=np.int32)

# Triangle shape at top-right - 3 points
# Creates an inverted triangle in the upper right quadrant
pts2 = np.array([[350, 50], [250,200], [450,200]], dtype=np.int32)

# Triangle shape at bottom-left - 3 points
# Creates a regular triangle in the lower left quadrant
pts3 = np.array([[150, 300], [50,450], [250,450]], dtype=np.int32)

# Pentagon shape at bottom-right - 5 points
# Creates a pentagon in the lower right quadrant
pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype=np.int32)

# Draw polylines using cv2.polylines()
# Parameters: image, [points], isClosed, color(BGR), thickness=1

# Draw thunder shape in blue, open path (isClosed=False)
cv2.polylines(img, [pts1], False, (255,0,0))  # Blue: (255,0,0)

# Draw top triangle in black with thick lines (thickness=10)
cv2.polylines(img, [pts2], False, (0,0,0), 10)  # Black: (0,0,0)

# Draw bottom-left triangle in red with thick lines and closed path
cv2.polylines(img, [pts3], True, (0,0,255), 10)  # Red: (0,0,255)

# Draw pentagon in black with default thickness, closed path
cv2.polylines(img, [pts4], True, (0,0,0))  # Black: (0,0,0)

# Display the result
cv2.imshow('polyline', img)      # Show the image in a window titled 'polyline'
cv2.waitKey(0)                   # Wait for any key press
cv2.destroyAllWindows()          # Clean up and close all windows