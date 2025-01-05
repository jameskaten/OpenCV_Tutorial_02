import cv2

# Load a blank white image (500x500 pixels)
img = cv2.imread('../img/blank_500.jpg')

# Draw thin lines (1 pixel) in primary colors
# BGR format: (Blue, Green, Red) - OpenCV uses BGR instead of RGB
cv2.line(img, (50, 50), (150, 50), (255, 0, 0))   # Pure Blue:   (255, 0, 0)
cv2.line(img, (200, 50), (300, 50), (0, 255, 0))  # Pure Green:  (0, 255, 0)
cv2.line(img, (350, 50), (450, 50), (0, 0, 255))  # Pure Red:    (0, 0, 255)

# Draw thick lines (10 pixels) with secondary colors and other combinations
# Parameters: image, start_point, end_point, color, thickness
cv2.line(img, (100, 100), (400, 100), (255, 255, 0), 10)  # Sky Blue:   B + G = (255, 255, 0)
cv2.line(img, (100, 150), (400, 150), (255, 0, 255), 10)  # Pink:       B + R = (255, 0, 255)
cv2.line(img, (100, 200), (400, 200), (0, 255, 255), 10)  # Yellow:     G + R = (0, 255, 255)
cv2.line(img, (100, 250), (400, 250), (200, 200, 200), 10)# Gray:       Partial mix of all = (200, 200, 200)
cv2.line(img, (100, 300), (400, 300), (0, 0, 0), 10)      # Black:      No color = (0, 0, 0)

# Demonstrate different line types
# LINE_4:  4-connected line - creates more jagged diagonal lines
cv2.line(img, (100, 350), (400, 400), (0, 0, 255), 20, cv2.LINE_4)

# LINE_8:  8-connected line - default, smoother than LINE_4
cv2.line(img, (100, 400), (400, 450), (0, 0, 255), 20, cv2.LINE_8)

# LINE_AA: Anti-aliased line - smoothest appearance
cv2.line(img, (100, 450), (400, 500), (0, 0, 255), 20, cv2.LINE_AA)

# Draw diagonal line from top-left to bottom-right
cv2.line(img, (0,0), (500, 500), (0, 0, 255))

# Display the result
cv2.imshow('lines', img)         # Show the image in a window titled 'lines'
cv2.waitKey(0)                   # Wait for any key press
cv2.destroyAllWindows()          # Clean up and close all windows