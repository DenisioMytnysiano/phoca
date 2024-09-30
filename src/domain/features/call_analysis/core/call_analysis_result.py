from dataclasses import dataclass

from domain.features.call_analysis.entities_extraction.call_entity import CallEntity


@dataclass
class CallAnalysisResult:
    call_id: str
    transcription: str
    emotional_tone: str
    extracted_entities: dict[CallEntity, str]

