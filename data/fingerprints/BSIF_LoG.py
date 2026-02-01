import os
import cv2
import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt
import pandas as pd

def bsif_feature_extraction(binary_image, filterbank, save_path):
    # Read the binary fingerprint image
    img = cv2.imread(binary_image, cv2.IMREAD_GRAYSCALE)

    # Ensure the image is binary (0 or 255)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Initialize an empty array for the BSIF features
    bsif_img = np.zeros_like(img)

    # Apply the BSIF filterbank
    for i, filter in enumerate(filterbank):
        # Convolve the image with the filter
        conv_result = cv2.filter2D(img, -1, filter)

        # Threshold the convolution result to get binary features
        _, binary_result = cv2.threshold(conv_result, 0, 255, cv2.THRESH_BINARY)

        # Update the BSIF image with the binary features
        bsif_img += (binary_result // 255) * (2 ** i)

    # Save the BSIF image
    cv2.imwrite(save_path, bsif_img.astype(np.uint8))

def convert_to_binarization(image, threshold):
    """
    Convert image to binary using a threshold value
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary

# Define the LoG filter
log_filter = np.array([
    [0,  0, -1,  0,  0],
    [0, -1, -2, -1,  0],
    [-1, -2, 16, -2, -1],
    [0, -1, -2, -1,  0],
    [0,  0, -1,  0,  0]
], dtype=np.float32)

# Create a filter bank with the LoG filter
filterbank = [log_filter]

# Load the palmprint image
image_palm = cv2.imread('102_5.png', cv2.IMREAD_GRAYSCALE)  # Replace 'W_512.bmp' with your image file

# Apply Otsu's thresholding to obtain a binary image
_, binary_image = cv2.threshold(image_palm, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save the binary image
cv2.imwrite('binary_image_2.bmp', binary_image)

# Path to the binary fingerprint image
binary_image_path = 'binary_image_2.bmp'

# Path to save the BSIF image
bsif_image_save_path = 'bsif_image.bmp'

# Apply BSIF feature extraction
bsif_feature_extraction(binary_image_path, filterbank, bsif_image_save_path)

# Display the original binary image
plt.imshow(binary_image, cmap='gray')
plt.title('Palmprint Binary Image')
plt.show()

# Load the saved BSIF image
bsif_image = cv2.imread(bsif_image_save_path, cv2.IMREAD_GRAYSCALE)

# Display the BSIF image
plt.imshow(bsif_image, cmap='gray')
plt.title('Palmprint BSIF Filtered Image')
plt.show()
