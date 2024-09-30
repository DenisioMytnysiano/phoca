from domain.features.call_analysis.core.call_analysis_state_repository import CallAnalysisStateRepository
from domain.features.call_analysis.core.call_analysis_status import CallAnalysisStatus

class MongoAnalysisStateRepository(CallAnalysisStateRepository):

    def accepted(self, call_id: str, audio_url: str):
        return super().accepted(call_id, audio_url)
    
    def in_progress(self, call_id):
        return super().in_progress(call_id)
    
    def completed(self, call_id):
        return super().completed(call_id)
    
    def failed(self, call_id: str):
        return super().failed(call_id)
    
    def get_status(self, call_id) -> CallAnalysisStatus:
        return super().get_status(call_id)