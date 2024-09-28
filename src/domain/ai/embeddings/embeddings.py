from typing import Protocol
import numpy as np


class Embeddings(Protocol):

    def embed(self, text: str) -> np.array:
        pass
