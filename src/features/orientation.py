import numpy as np
import cv2

def compute_orientation(block: np.ndarray) -> float:
    """
    Compute dominant ridge orientation using structure tensor.
    """
    gx = cv2.Sobel(block, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(block, cv2.CV_64F, 0, 1, ksize=3)

    num = 2 * np.sum(gx * gy)
    den = np.sum(gx**2 - gy**2)
    theta = 0.5 * np.arctan2(num, den)

    return theta
