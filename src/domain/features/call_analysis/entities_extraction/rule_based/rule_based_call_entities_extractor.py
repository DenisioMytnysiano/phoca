from typing import Dict
from domain.features.call_analysis.entities_extraction.call_entities_extractor import CallEntitiesExtractor
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity
from domain.features.call_analysis.entities_extraction.rule_based.caller_patterns import patterns as caller_patterns
from domain.features.call_analysis.entities_extraction.rule_based.recipient_patterns import patterns as recipient_patterns
from domain.features.call_analysis.entities_extraction.rule_based.location_patterns import patterns as location_patterns


class RuleBasedCallEntitiesExtractor(CallEntitiesExtractor):

    def extract_entities(self, transcription: str) -> Dict[CallEntity, str]:
        return {}
