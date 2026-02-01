import numpy as np

def entropy(bits):
    p = np.mean(bits)
    if p in (0, 1):
        return 0.0
    return -(p*np.log2(p) + (1-p)*np.log2(1-p))

def bit_balance(bits):
    return np.mean(bits)

def correlation(a, b):
    return np.corrcoef(a, b)[0, 1]
