import numpy as np
import cv2
from .orientation import compute_orientation

def rotate_filter(kernel: np.ndarray, theta: float) -> np.ndarray:
    h, w = kernel.shape
    center = (w // 2, h // 2)
    rot_mat = cv2.getRotationMatrix2D(center, np.degrees(theta), 1.0)
    return cv2.warpAffine(kernel, rot_mat, (w, h))

def extract_ibsif(image: np.ndarray,
                  filters: list,
                  block_size: int = 16) -> np.ndarray:
    """
    Orientation-guided I-BSIF feature extraction.
    """
    h, w = image.shape
    bits = []

    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = image[y:y+block_size, x:x+block_size]
            theta = compute_orientation(block)

            for f in filters:
                rf = rotate_filter(f, theta)
                response = np.sum(block * rf)
                bits.append(1 if response >= 0 else 0)

    return np.array(bits, dtype=np.uint8)
