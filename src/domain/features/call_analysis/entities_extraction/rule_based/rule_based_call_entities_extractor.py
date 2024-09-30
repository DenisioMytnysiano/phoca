from domain.features.call_analysis.entities_extraction.call_entities_extractor import CallEntitiesExtractor
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity


class RuleBasedCallEntitiesExtractor(CallEntitiesExtractor):

    def extract_entities(self, transcription: str) -> dict[str, CallEntity]:
        return {
            "PERSON1": CallEntity.CALLER,
            "LOCATION1": CallEntity.CALLER_LOCATION
        }
