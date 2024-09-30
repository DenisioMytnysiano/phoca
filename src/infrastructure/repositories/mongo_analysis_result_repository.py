from domain.features.call_analysis.core.call_analysis_result import CallAnalysisResult
from domain.features.call_analysis.core.call_analysis_result_repository import CallAnalysisResultRepository
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity


class MongoAnalysisResultRepository(CallAnalysisResultRepository):
    
    def set_transcription(self, call_id: str, transcription: str):
        return super().set_transcription(call_id, transcription)
    
    def set_extracted_entities(self, call_id: str, extracted_entities: dict[str, CallEntity]):
        return super().set_extracted_entities(call_id, extracted_entities)
    
    def set_emotional_tone(self, call_id: str, emotional_tone: CallEmotionalTone):
        return super().set_emotional_tone(call_id, emotional_tone)
    
    def get_result(self, call_id: str) -> CallAnalysisResult:
        return super().get_result(call_id)