from typing import List, Protocol


class KeywordsExtractor(Protocol):

    def extract(self, text: str) -> List[str]:
        pass
