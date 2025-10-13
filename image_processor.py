import cv2
import numpy as np
import os

def load_and_display_image(image_path):
    """
    Loads an image, displays it, and saves it with a random name.
    """
    # Load the image
    img = cv2.imread(image_path)

    # Check if image is loaded successfully
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Display the image
    cv2.imshow('Loaded Image', img)
    cv2.waitKey(0) # Wait for a key press
    cv2.destroyAllWindows() # Close the display window

    # Generate a random filename for the output image
    random_filename = f"random_image_{np.random.randint(10000, 99999)}.jpg"

    # Save the image with the random filename
    success = cv2.imwrite(random_filename, img)

    if success:
        print(f"Image saved successfully as {random_filename}")
    else:
        print("Error: Could not save the image.")

# Example usage:
# load_and_display_image("path/to/your/input/image.jpg")