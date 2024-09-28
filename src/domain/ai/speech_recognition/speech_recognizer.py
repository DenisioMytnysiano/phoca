import numpy as np
from typing import Protocol


class SpeechRecognizer(Protocol):

    def transcribe(self, audio: np.array) -> str:
        pass
