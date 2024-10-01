import numpy as np
from typing import List, Protocol


class CallKeywordsVectorStore(Protocol):

    def insert(self, call_id: str, keywords: List[str]):
        pass

    def delete(self, call_id: str):
        pass

    def get(self, call_id: str) -> List[np.array]:
        pass
