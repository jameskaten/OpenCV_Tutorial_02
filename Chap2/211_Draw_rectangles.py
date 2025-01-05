import cv2

# Load a blank white image (500x500 pixels)
img = cv2.imread("../img/blank_500.jpg")

# Draw a thin blue rectangle (default thickness=1)
# Parameters: image, start_point(x,y), end_point(x,y), color(BGR)
# This creates a 100x100 pixel rectangle at position (50,50)
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))  # Pure Blue: (255, 0, 0)

# Draw a thick green rectangle with thickness=10
# Note: When points are given in reverse order (end before start),
# OpenCV automatically adjusts the coordinates
# Parameters: image, start_point, end_point, color(BGR), thickness
cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 10)  # Pure Green: (0, 255, 0)

# Draw a filled red rectangle
# Parameters: image, start_point, end_point, color(BGR), thickness=-1
# When thickness=-1, the rectangle is filled with the specified color
# This creates a 250x250 pixel filled rectangle
cv2.rectangle(img, (450, 200), (200, 450), (0, 0, 255), -1)  # Pure Red: (0, 0, 255)

# Display the result
cv2.imshow('rectangle', img)     # Show the image in a window titled 'rectangle'
cv2.waitKey(0)                   # Wait for any key press
cv2.destroyAllWindows()          # Clean up and close all windows