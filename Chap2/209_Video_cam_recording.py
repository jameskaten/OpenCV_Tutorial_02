import cv2  # Import OpenCV library

# Initialize video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)

if cap.isOpened():      # Check if camera is successfully opened
    # Define output video file settings
    file_path = './record.mp4'    # Output video file path
    fps = 25.40                   # Frames per second for output video
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # Video codec (DIVX compression)
    
    # Get the camera's frame dimensions
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # Get frame width
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # Get frame height
    size = (int(width), int(height))            # Create tuple of frame dimensions
    
    # Create VideoWriter object to save the video
    out = cv2.VideoWriter(file_path, fourcc, fps, size)
    
    while True:
        ret, frame = cap.read()   # Capture frame-by-frame
                                 # ret: boolean (success/failure)
                                 # frame: captured image
        if ret:  # If frame is successfully captured
            cv2.imshow('camera-recording', frame)  # Display the frame
            out.write(frame)                      # Write frame to output video
            
            # Break loop if any key is pressed
            if cv2.waitKey(1) != -1:
                break
        else:  # If frame capture fails
            print('no frame')
            break
            
    out.release()  # Release the VideoWriter
else:
    print("can't open video.")  # Camera initialization failed

# Cleanup
cap.release()           # Release the camera
cv2.destroyAllWindows() # Close all OpenCV windows
