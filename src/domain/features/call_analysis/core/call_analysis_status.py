from enum import Enum


class CallAnalysisStatus(str, Enum):
    ACCEPTED = "Accepted"
    IN_PROGRESS = "In Progress"
    FINISHED = "Finished"
    FAILED = "Failed"
