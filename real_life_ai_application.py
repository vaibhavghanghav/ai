

#this is another 


import cv2
import numpy as np

# Load an image
image = cv2.imread('irrigation.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', edges)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
