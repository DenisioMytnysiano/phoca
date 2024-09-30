from typing import Protocol
from domain.features.call_analysis.core.call_analysis_status import CallAnalysisStatus


class CallAnalysisStateRepository(Protocol):

    def set_status(self, call_id, status: CallAnalysisStatus):
        pass

    def get_status(self, call_id) -> CallAnalysisStatus:
        pass
