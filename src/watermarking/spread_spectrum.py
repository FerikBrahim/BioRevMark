import numpy as np

def embed_ss(coeffs: np.ndarray, bit: int, pn: np.ndarray, alpha: float):
    return coeffs + alpha * bit * pn

def extract_ss(coeffs: np.ndarray, pn: np.ndarray):
    return np.sign(np.sum(coeffs * pn))
