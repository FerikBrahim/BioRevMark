import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def psnr(original, watermarked):
    return peak_signal_noise_ratio(original, watermarked)

def ssim(original, watermarked):
    return structural_similarity(original, watermarked)

def mse(original, watermarked):
    return np.mean((original - watermarked) ** 2)
