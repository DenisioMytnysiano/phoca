from typing import Protocol
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity


class CallEntitiesExtractor(Protocol):
    
    def extract_entities(self, transcription: str) -> dict[CallEntity, str]:
        pass
