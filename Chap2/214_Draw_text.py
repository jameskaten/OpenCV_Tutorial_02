# This demonstrates different font styles and text rendering in OpenCV
import cv2

# Load a blank white image (500x500 pixels)
img = cv2.imread('../img/blank_500.jpg')

# === SANS-SERIF FONTS ===
# FONT_HERSHEY_PLAIN: Simple and thin sans-serif font
# Parameters: image, text, position(x,y), font_face, font_scale, color(BGR), thickness=1
cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))

# FONT_HERSHEY_SIMPLEX: Normal size sans-serif font
# Standard choice for simple text
cv2.putText(img, "Simplex", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))

# FONT_HERSHEY_DUPLEX: More bold version of simplex
# Good for emphasis while maintaining sans-serif style
cv2.putText(img, "Duplex", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))

# Same simplex font with larger scale (2) and blue color
# Demonstrates size scaling and color effects
cv2.putText(img, "Simplex", (200,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250))

# === SERIF FONTS ===
# FONT_HERSHEY_COMPLEX_SMALL: Small serif font
# Good for detailed text that needs to remain readable
cv2.putText(img, "Complex Small", (50,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))

# FONT_HERSHEY_COMPLEX: Normal serif font
# More formal looking than sans-serif options
cv2.putText(img, "Complex", (50,220), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,0))

# FONT_HERSHEY_TRIPLEX: Bold serif font
# Good for headers or emphasis with serif style
cv2.putText(img, "Triplex", (50,260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))

# Same triplex font with larger scale (2) and red color
# Shows how serif fonts look when enlarged
cv2.putText(img, "Complex", (200,260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

# === SCRIPT STYLE ===
# FONT_HERSHEY_SCRIPT_SIMPLEX: Handwriting-style font
# Useful for creating a more personal or casual feel
cv2.putText(img, "Script Simplex", (50,330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,0))

# === ITALIC VARIATIONS ===
# Adding FONT_ITALIC flag to create italic versions
# Plain font with italic style
cv2.putText(img, "Plain Italic", (50,430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0,0,0))

# Complex (serif) font with italic style
# Combines serif formality with italic emphasis
cv2.putText(img, "Complex Italic", (50,470), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0,0,0))

# Display the result
cv2.imshow('circle', img)        # Show the image in a window titled 'circle'
cv2.waitKey(0)                   # Wait for any key press
cv2.destroyAllWindows()          # Clean up and close all windows
