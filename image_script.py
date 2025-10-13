import cv2
import numpy as np
import os

# Load an image from the current directory, assuming 'sample.jpg' exists.
# If not, we'll create a blank image for demonstration.
image_path = 'sample.jpg'
if os.path.exists(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not load image from {image_path}. Creating a blank image.")
        image = np.zeros((300, 300, 3), dtype=np.uint8)
else:
    print(f"Image file {image_path} not found. Creating a blank image.")
    image = np.zeros((300, 300, 3), dtype=np.uint8)



# Save the script itself to a randomly named .py file
import random
import string

random_name = "random_script_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"
with open(random_name, 'w') as f:
    f.write('# This is a randomly named script.\n')
    f.write('# Original script content would be written here.\n')
    f.write('# For this example, we just write a placeholder.\n')
    f.write('print("Hello from the random script!")\n')

print(f"Script saved to {random_name}")
