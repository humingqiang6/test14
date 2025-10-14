import cv2
import sys
import os

# Load an image from file.
# For this example, we'll try to load an image named 'sample.jpg' in the current directory.
# You'll need to provide an actual image path for this script to work.
image_path = 'sample.jpg'
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    sys.exit(1)

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from '{image_path}'. Check if it's a valid image file.")
    sys.exit(1)

# Display the image in a window named 'Image'.
cv2.imshow('Image', image)

# Wait for a key press and then close the window.
print("Press any key on the image window to close it.")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the loaded image to a new file as an example of saving.
# In a real scenario, you might process the image before saving.
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)
print(f"Image saved as {output_path}.")
