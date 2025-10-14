import cv2
import numpy as np
import os

# Load an image from file
# Using a placeholder path, you would need to provide an actual image path
image_path = '/workspace/placeholder_image.jpg' # This path might not exist, for demonstration only

# For the purpose of this script, let's create a simple synthetic image
# Create a 300x300 white image with some shapes
img = np.ones((300, 300, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (50, 50), (250, 250), (0, 0, 0), -1)  # Black square
cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)  # Blue circle

# The display functionality is removed for headless environments
# print("Display functionality skipped in headless environment.")

# Save the image to a file
output_path = '/workspace/generated_output.jpg'
cv2.imwrite(output_path, img)
print(f"Image saved to {output_path}")
