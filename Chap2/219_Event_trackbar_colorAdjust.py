import cv2
import numpy as np

win_name = 'Trackbar'                       # Window name constant

# Load a blank white image (500x500 pixels)
img = cv2.imread('../img/blank_500.jpg')
cv2.imshow(win_name, img)                   # Display initial white image

def onChange(x):
    """
    Trackbar callback function - updates image color when trackbar values change
    
    Parameters:
        x: Current position of the trackbar that triggered the callback
           (automatically provided by OpenCV)
    """
    print(x)                                # Print current trackbar value
    
    # Get current positions of all trackbars
    r = cv2.getTrackbarPos('R', win_name)   # Red value (0-255)
    g = cv2.getTrackbarPos('G', win_name)   # Green value (0-255)
    b = cv2.getTrackbarPos('B', win_name)   # Blue value (0-255)
    print(r, g, b)                          # Print current RGB values
    
    # Update entire image with new color
    # img[:] = [b,g,r] sets all pixels to the same BGR color
    # Note: OpenCV uses BGR order, not RGB
    img[:] = [b, g, r]
    cv2.imshow(win_name, img)               # Display updated image

# Create trackbars for RGB color control
# Parameters: trackbar_name, window_name, initial_value, max_value, callback_function
cv2.createTrackbar('R', win_name, 255, 255, onChange)  # Red trackbar
cv2.createTrackbar('G', win_name, 255, 255, onChange)  # Green trackbar
cv2.createTrackbar('B', win_name, 255, 255, onChange)  # Blue trackbar

# Main event loop
while True:
    if cv2.waitKey(1) & 0xFF == 27:        # Check for ESC key (27)
        break
cv2.destroyAllWindows()                     # Clean up and close all windows
