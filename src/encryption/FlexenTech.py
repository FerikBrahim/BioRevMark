import numpy as np

class FlexenTech:
    """
    Lightweight permutation-based encryption for biometric vectors.
    """

    def __init__(self, B: int, K: int, rounds: int = 3):
        self.B = B
        self.K = K
        self.rounds = rounds

    def _perm_indices(self, n: int):
        values = [(self.B * (self.K - i)) % self.K for i in range(1, n + 1)]
        return np.argsort(values)

    def encrypt(self, bits: np.ndarray) -> np.ndarray:
        idx = self._perm_indices(len(bits))
        out = bits.copy()
        for _ in range(self.rounds):
            out = out[idx]
        return out

    def decrypt(self, bits: np.ndarray) -> np.ndarray:
        idx = self._perm_indices(len(bits))
        inv = np.argsort(idx)
        out = bits.copy()
        for _ in range(self.rounds):
            out = out[inv]
        return out
