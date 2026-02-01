import cv2
import numpy as np
import os
import math

# --- Configuration ---
# **IMPORTANT:** Replace this with the path to your input fingerprint image
input_image_path = 'Finger.png' # Example: 'fingerprint.tif'

# **IMPORTANT:** Specify the directory where you want to save the rotated images
output_directory = 'rotated_fingerprints' # Example: 'rotated_fingerprints'

# Define the angles for rotation in degrees
rotation_angles = [30, 45, 90, 180, 270]

# --- Create Output Directory ---
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created output directory: {output_directory}")
else:
    print(f"Output directory already exists: {output_directory}")

# --- 1. Load the Fingerprint Image ---
# Load the image in grayscale
print(f"Loading image from: {input_image_path}")
img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Check if image loaded successfully
if img is None:
    print(f"Error: Could not load image from {input_image_path}")
    print("Please ensure the path is correct and the image file exists.")
    exit() # Exit the script if the image cannot be loaded

print("Image loaded successfully.")

# Get image dimensions
height, width = img.shape
center_x, center_y = width // 2, height // 2 # Center of the image

# --- 2. Rotate and Save Images for Each Angle ---
print("\nStarting image rotation process...")

for angle in rotation_angles:
    print(f"Rotating image by {angle} degrees...")

    # Calculate the rotation matrix
    # cv2.getRotationMatrix2D(center, angle, scale)
    # center: Center of rotation (tuple of x, y)
    # angle: Rotation angle in degrees (positive values mean counter-clockwise rotation)
    # scale: Scaling factor (1.0 means no scaling)
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1.0)

    # Calculate the new bounding dimensions of the rotated image to prevent cropping
    # This ensures the entire rotated image fits within the output canvas.
    # The new width and height are calculated based on the corners of the original image
    # transformed by the rotation matrix.
    cos = np.abs(rotation_matrix[0, 0])
    sin = np.abs(rotation_matrix[0, 1])

    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))

    # Adjust the translation part of the rotation matrix to center the rotated image
    # The translation needed is half the difference between the new dimensions
    # and the original dimensions.
    rotation_matrix[0, 2] += (new_width / 2) - center_x
    rotation_matrix[1, 2] += (new_height / 2) - center_y

    # Apply the affine transformation (rotation)
    # cv2.warpAffine(src, M, dsize)
    # src: Input image
    # M: 2x3 transformation matrix (our adjusted rotation_matrix)
    # dsize: Size of the output image (new_width, new_height)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (new_width, new_height), borderValue=(0)) # borderValue=0 for black padding

    # --- 3. Save the Rotated Image ---
    # Create a filename based on the original name and the angle
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    output_filename = f"{base_name}_rotated_{angle}deg.png"
    output_path = os.path.join(output_directory, output_filename)

    cv2.imwrite(output_path, rotated_img)
    print(f"Saved rotated image to: {output_path}")

print("\nImage rotation and saving process completed.")
