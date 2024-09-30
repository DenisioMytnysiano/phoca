from typing import Protocol
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone


class CallEmotionalToneAnalyzer(Protocol):

    def analyze_emotional_tone(self, transcription: str) -> CallEmotionalTone:
        pass