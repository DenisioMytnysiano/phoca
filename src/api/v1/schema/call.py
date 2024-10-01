from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, field_validator
from domain.features.call_analysis.core.call_url_validator import CallUrlValidator

url_validator = CallUrlValidator()


@dataclass
class CreateCallRequest(BaseModel):
    audio_url: str

    @field_validator("audio_url")
    @classmethod
    def validate_audio_url(cls, value):
        url_validator.validate(value)
        return value


@dataclass
class CreateCallResponse:
    id: str


class CallSentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    ANRGY = "Angry"


@dataclass
class GetCallResponse:
    id: str
    name: Optional[str]
    location: Optional[str]
    emotional_tone: CallSentiment
    text: str
    categories: List[str]
