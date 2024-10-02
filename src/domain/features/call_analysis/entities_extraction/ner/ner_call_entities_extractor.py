from typing import Dict
import spacy
from spacy.cli import download
from domain.features.call_analysis.entities_extraction.call_entities_extractor import CallEntitiesExtractor
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity

class NerCallEntitiesExtractor(CallEntitiesExtractor):
    def __init__(self, model: str = "en_core_web_sm"):
        try:
            self.nlp = spacy.load(model)
        except:
            print(f"Model '{model}' not found. Attempting to download...")
            download(model)
            self.nlp = spacy.load(model)

    def extract_entities(self, transcription: str) -> Dict[CallEntity, str]:
        doc = self.nlp(transcription)
        entities = {}
        caller_found = False
        caller_location_found = False

        for i, ent in enumerate(doc.ents):
            if not caller_found and ent.label_ == "PERSON":
                full_name = self._extract_full_name(doc.ents, i)
                entities[CallEntity.CALLER] = full_name
                caller_found = True
            elif not caller_location_found and ent.label_ in ["GPE", "LOC"]:
                entities[CallEntity.CALLER_LOCATION] = ent.text
                caller_location_found = True

            if caller_found and caller_location_found:
                break

        return entities

    def _extract_full_name(self, ents, current_index):
        current_ent = ents[current_index]
        next_ent = ents[current_index + 1] if current_index + 1 < len(ents) else None

        if next_ent and next_ent.label_ == "PERSON" and next_ent.start == current_ent.end:
            return f"{current_ent.text} {next_ent.text}"
        else:
            return current_ent.text