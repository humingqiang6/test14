import cv2
import numpy as np
import os

# Load an image from the workspace directory. Using a common default name, or a random one if it doesn't exist.
image_path = 'sample_image.jpg' # This name is assumed for the example. If the file doesn't exist, we'll create a dummy one.
if not os.path.exists(image_path):
    print(f"Image {image_path} not found. Creating a dummy image.")
    # Create a dummy image if the file doesn't exist
    dummy_img = np.zeros((300, 300, 3), dtype=np.uint8)
    dummy_img[:] = [255, 0, 0]  # Fill with blue color
    cv2.imwrite(image_path, dummy_img)

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")

    # Display the image in a window
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window

    # Save the loaded image to a new file with a random name
    import random
    import string
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.jpg'
    cv2.imwrite(random_name, image)
    print(f"Image saved as {random_name}")
