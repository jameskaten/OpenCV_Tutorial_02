# Import required libraries
import cv2  # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations

# Global variables for tracking mouse interaction
isDragging = False      # Tracks if mouse is currently dragging
x0, y0, w, h = -1, -1, -1, -1      # Initial coordinates and dimensions for selection
blue, red = (255,0,0), (0,0,255)    # Color constants for drawing rectangles

def onMouse(event, x, y, flags, param):
    """
    Mouse callback function that handles all mouse events
    Parameters:
        event: Type of mouse event (click, move, etc.)
        x, y: Current mouse coordinates
        flags: Any relevant mouse flags
        param: Optional parameters
    """
    global isDragging, x0, y0, img
    
    if event == cv2.EVENT_LBUTTONDOWN:  # When left mouse button is pressed
        isDragging = True
        x0 = x    # Store initial x coordinate
        y0 = y    # Store initial y coordinate
    
    elif event == cv2.EVENT_MOUSEMOVE:  # When mouse is moving
        if isDragging:  # Only draw if we're in dragging mode
            img_draw = img.copy()    # Create a copy to draw on
            cv2.rectangle(img_draw, (x0, y0), (x,y), blue, 2)   # Draw blue rectangle during drag
            cv2.imshow('img', img_draw)
    
    elif event == cv2.EVENT_LBUTTONUP:  # When left mouse button is released
        if isDragging:
            isDragging = False
            w = x - x0    # Calculate width of selection
            h = y - y0    # Calculate height of selection
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            
            if x>0 and h>0:  # Ensure valid selection (dragged from top-left to bottom-right)
                img_draw = img.copy()
                # Draw final selection rectangle in red
                cv2.rectangle(img_draw, (x0, y0), (x,y), red, 2)
                cv2.imshow('img', img_draw)     
                
                # Extract and save the ROI
                roi = img[y0:y0+h, x0:x0+w]    # Slice the ROI from main image
                cv2.imshow('cropped', roi)      # Show cropped image
                cv2.moveWindow('cropped', 0, 0) # Move cropped window to top-left
                cv2.imwrite('./cropped.jpg', roi)  # Save cropped image
                print("cropped.")
            else:
                cv2.imshow('img', img)
                print("좌측 상단에서 우측 하단으로 드래그")  # "Drag from top-left to bottom-right"

# Load and display the image
img = cv2.imread('../img/Chris01.jpg')
cv2.imshow('img', img)

# Set up mouse callback
cv2.setMouseCallback('img', onMouse)

# Wait for key press and clean up
cv2.waitKey()
cv2.destroyAllWindows()

