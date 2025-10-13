import cv2
import numpy as np

# Load an image from file
image_path = '{image_path}'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {{image_path}}.")
    exit()

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
