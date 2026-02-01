import numpy as np

def pn_sequence(key, shape, idx):
    rng = np.random.default_rng(abs(hash((key, idx))) % (2**32))
    return rng.choice([-1, 1], size=shape)
