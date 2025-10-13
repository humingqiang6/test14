import cv2
import numpy as np
import os

# Load an image from file
# Replace 'path/to/your/image.jpg' with the actual path to your image
image_path = '/workspace/placeholder_image.jpg'  # Using the generated placeholder image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}. Please check the path.")
    exit()

# Print a message indicating the image was loaded successfully (GUI not available)
print(f"Image loaded successfully from {image_path}. Skipping display in headless environment.")

# Save the script with a random name
# This part is a bit meta, as the script is already written.
# We can simulate saving a version of the core logic with a random name.
script_content = '''import cv2
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
'''

import random
import string
random_filename = "opencv_script_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"

with open(random_filename, 'w') as f:
    f.write(script_content)

print(f"Script saved with a random name: {random_filename}")
