from typing import List, Protocol


class CallCategoryClassifier(Protocol):

    def classify(self, call_id: str, transcription: str):
        pass

    def get_result(self, call_id: str) -> List[str]:
        pass
