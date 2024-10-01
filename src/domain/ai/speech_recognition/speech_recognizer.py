from typing import Protocol


class SpeechRecognizer(Protocol):

    def transcribe(self, audio_path: str) -> str:
        pass
