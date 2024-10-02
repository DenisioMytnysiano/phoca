from domain.features.call_analysis.core.call_analysis_state_repository import CallAnalysisStateRepository
from domain.features.call_analysis.core.call_analysis_status import CallAnalysisStatus
from domain.features.call_analysis.core.exceptions import CallNotFoundException
from infrastructure.db.mongo.database import database

class MongoAnalysisStateRepository(CallAnalysisStateRepository):

    def __init__(self):
        self.collection = database.get_collection("call-analysis-state")
        self.collection.create_index("call_id", unique=True)

    def set_status(self, call_id, status: CallAnalysisStatus):
        return self.collection.update_one(
            {"call_id": call_id},
            {"$set": {"status": status}
        }, upsert=True)

    def get_status(self, call_id) -> CallAnalysisStatus:
        result = self.collection.find_one({"call_id": call_id})
        if not result:
            raise CallNotFoundException(call_id)
        return result["status"]
