from .lwt import lwt2
from .spread_spectrum import extract_ss
from ..utils.random_utils import pn_sequence
import numpy as np

def extract(image, n_bits, key):
    LL, (LH, HL, HH) = lwt2(image)
    bits = []

    for i in range(n_bits):
        pn = pn_sequence(key, LH.shape, i)
        bit = extract_ss(LH, pn) + extract_ss(HL, pn)
        bits.append(1 if bit >= 0 else 0)

    return np.array(bits, dtype=np.uint8)
