from domain.features.call_analysis.core.call_analysis_result import CallAnalysisResult
from domain.features.call_analysis.core.call_analysis_result_repository import CallAnalysisResultRepository
from domain.features.call_analysis.core.exceptions import CallNotFoundException
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity
from infrastructure.db.mongo.database import database

class MongoAnalysisResultRepository(CallAnalysisResultRepository):

    def __init__(self) -> None:
        self.collection = database.get_collection("call-analysis-result")
        self.collection.create_index("call_id", unique=True)

    def set_transcription(self, call_id: str, transcription: str):
        self.collection.update_one(
            {"call_id": call_id},
            {"$set":{"transcription": transcription}
        }, upsert=True)

    def set_extracted_entities(self, call_id: str, extracted_entities: dict[CallEntity, str]):
        self.collection.update_one(
            {"call_id": call_id},
            {"$set":{"extracted_entities": extracted_entities}
        }, upsert=True)

    def set_emotional_tone(self, call_id: str, emotional_tone: CallEmotionalTone):
        self.collection.update_one(
            {"call_id": call_id},
            {"$set":{"emotional_tone": emotional_tone}
        }, upsert=True)

    def get_result(self, call_id: str) -> CallAnalysisResult:
        result = self.collection.find_one({"call_id": call_id})
        if not result:
            raise CallNotFoundException(call_id)
        return result