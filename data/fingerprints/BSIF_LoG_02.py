import os
import cv2
import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt
import pandas as pd

def log_filter(size, sigma):
    """Generate a Laplacian of Gaussian filter."""
    n = size // 2
    y, x = np.ogrid[-n:n+1, -n:n+1]
    y_filter = np.exp(-(x*x + y*y) / (2. * sigma * sigma))
    y_filter /= y_filter.sum()
    y_filter = y_filter * (x*x + y*y - 2*sigma*sigma) / (sigma**4)
    return y_filter - y_filter.mean()

def bsif_feature_extraction(binary_image, log_filter, save_path):
    # Read the binary fingerprint image
    img = cv2.imread(binary_image, cv2.IMREAD_GRAYSCALE)

    # Ensure the image is binary (0 or 255)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Apply the LoG filter
    conv_result = cv2.filter2D(img, -1, log_filter)

    # Threshold the convolution result to get binary features
    _, binary_result = cv2.threshold(conv_result, 0, 255, cv2.THRESH_BINARY)

    # Save the result
    cv2.imwrite(save_path, binary_result.astype(np.uint8))

def convert_to_binarization(image, threshold):
    """Convert image to binary using a threshold value."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary

# Define the LoG filter parameters
filter_size = 5
sigma = 1.0
log_filt = log_filter(filter_size, sigma)

# Load the palmprint image
image_palm = cv2.imread('w.bmp', cv2.IMREAD_GRAYSCALE)  # Replace 's1.bmp' with your image file

# Apply Otsu's thresholding to obtain a binary image
_, binary_image = cv2.threshold(image_palm, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save the binary image
cv2.imwrite('binary_image.bmp', binary_image)

# Path to the binary fingerprint image
binary_image_path = 'binary_image.bmp'

# Path to save the LoG filtered image
log_image_save_path = 'log_image.bmp'

# Apply BSIF feature extraction using LoG filter
bsif_feature_extraction(binary_image_path, log_filt, log_image_save_path)

# Display the original binary image
plt.imshow(cv2.cvtColor(binary_image, cv2.COLOR_BGR2RGB))
plt.title('Fingerprint Binary Image')
plt.show()

# Load the saved LoG filtered image
log_image = cv2.imread(log_image_save_path, cv2.IMREAD_GRAYSCALE)

# Display the LoG filtered image
plt.imshow(log_image, cmap='gray')
plt.title('Palmprint LoG Filtered Image')
plt.show()
