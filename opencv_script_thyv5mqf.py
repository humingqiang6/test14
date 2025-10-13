import cv2
import sys
import os

def main():
    # Load the image
    img_path = sys.argv[1]
    if not os.path.exists(img_path):
        print(f"Error: Image file {img_path} not found.")
        sys.exit(1)

    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Could not load image {img_path}. Check if it's a valid image file.")
        sys.exit(1)

    # Display the image
    cv2.imshow('Loaded Image', img)
    print("Displaying image. Press any key on the image window to continue...")
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the image window

    # Save the image with a new name
    output_path = sys.argv[2]
    success = cv2.imwrite(output_path, img)
    if success:
        print(f"Image saved successfully as {output_path}")
    else:
        print(f"Error: Could not save image as {output_path}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image> <output_image>")
        sys.exit(1)
    main()