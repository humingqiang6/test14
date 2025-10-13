import numpy as np
import cv2

# Create a placeholder image (a simple gradient or pattern)
height, width = 512, 512
channels = 3
image = np.zeros((height, width, channels), dtype=np.uint8)

# Draw a simple pattern (e.g., a colored square)
image[100:400, 100:400] = [255, 100, 50]  # BGR color

# Save the generated image
cv2.imwrite('/workspace/placeholder_image.jpg', image)
print("Placeholder image created: /workspace/placeholder_image.jpg")