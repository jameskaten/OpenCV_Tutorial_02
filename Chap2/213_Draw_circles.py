# This file demonstrates drawing circles and ellipses using OpenCV
import cv2

# Load a blank white image (500x500 pixels)
img = cv2.imread('../img/blank_500.jpg')

# === CIRCLES ===
# Draw a solid blue circle
# Parameters: image, center(x,y), radius, color(BGR), thickness(default=1)
cv2.circle(img, (150, 150), 100, (255,0,0))  # Blue circle, radius 100

# Draw a thick green circle outline
# thickness=5 creates a thicker outline
cv2.circle(img, (300, 150), 70, (0,255,0), 5)  # Green circle, radius 70

# === ELLIPSES ===
# Parameters for ellipse: image, center(x,y), (major_axis,minor_axis), 
# angle, startAngle, endAngle, color(BGR), thickness

# Full red ellipse (0-360 degrees)
cv2.ellipse(img, (50, 300), (50,50), 0, 0, 360, (0,0,255))  # Perfect circle using equal axes

# Half ellipses demonstrating angle ranges
# Blue bottom half (0-180 degrees)
cv2.ellipse(img, (150, 300), (50,50), 0, 0, 180, (255,0,0))
# Red top half (181-360 degrees)
cv2.ellipse(img, (200, 300), (50,50), 0, 181, 360, (0,0,255))

# Ellipses with different axis lengths
# Green wide ellipse (major_axis > minor_axis)
cv2.ellipse(img, (325,300), (75,50), 0, 0, 360, (0,255,0))
# Magenta tall ellipse (major_axis < minor_axis)
cv2.ellipse(img, (450,300), (50,75), 0, 0, 360, (255, 0, 255))

# Rotated ellipses
# Black ellipse rotated 15 degrees
cv2.ellipse(img, (50,425), (50,75), 15, 0, 360, (0,0,0))
# Black ellipse rotated 45 degrees
cv2.ellipse(img,(200,425), (50,75), 45, 0, 360, (0,0,0))

# Rotated half ellipses
# Red bottom half, rotated 45 degrees
cv2.ellipse(img, (350,425), (50,75), 45, 0, 180, (0,0,255))
# Blue top half, rotated 45 degrees
cv2.ellipse(img, (400,425), (50,75), 45, 181, 360, (255,0,0))

# Display the result
cv2.imshow('circle', img)        # Show the image in a window titled 'circle'
cv2.waitKey(0)                   # Wait for any key press
cv2.destroyAllWindows()          # Clean up and close all windows