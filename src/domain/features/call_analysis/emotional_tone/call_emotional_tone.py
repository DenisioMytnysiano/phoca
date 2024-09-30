from enum import Enum


class CallEmotionalTone(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    ANGRY = "Angry"
