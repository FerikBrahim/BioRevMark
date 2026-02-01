import numpy as np

def ber(original, extracted):
    return np.mean(original != extracted)

def ncc(original, extracted):
    return np.corrcoef(original, extracted)[0, 1]
