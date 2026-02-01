import numpy as np
from .lwt import lwt2, ilwt2
from .spread_spectrum import embed_ss
from ..utils.random_utils import pn_sequence

def embed(image, bits, key, alpha=0.05):
    LL, (LH, HL, HH) = lwt2(image)

    for i, bit in enumerate(bits):
        pn = pn_sequence(key, LH.shape, i)
        LH = embed_ss(LH, bit, pn, alpha)
        HL = embed_ss(HL, bit, pn, alpha)

    return ilwt2((LL, (LH, HL, HH)))
