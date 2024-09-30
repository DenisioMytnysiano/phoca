from typing import Protocol
from domain.features.call_analysis.core.call_analysis_result import CallAnalysisResult
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity


class CallAnalysisResultRepository(Protocol):

    def set_transcription(self, call_id: str, transcription: str):
        pass

    def set_extracted_entities(self, call_id: str, extracted_entities: dict[str, CallEntity]):
        pass

    def set_emotional_tone(self, call_id: str, emotional_tone: CallEmotionalTone):
        pass

    def get_result(self, call_id: str) -> CallAnalysisResult:
        pass