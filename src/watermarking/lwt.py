import pywt
import numpy as np

def lwt2(image: np.ndarray):
    return pywt.dwt2(image, 'haar')

def ilwt2(coeffs):
    return pywt.idwt2(coeffs, 'haar')
