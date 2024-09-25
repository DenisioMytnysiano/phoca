from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


@dataclass
class CreateCallRequest:
    audio_url: str


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
