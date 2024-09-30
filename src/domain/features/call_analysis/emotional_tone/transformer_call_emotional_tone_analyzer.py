from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.emotional_tone.call_emotional_tone_analyzer import CallEmotionalToneAnalyzer


class TransformerCallEmotionalToneAnalyzer(CallEmotionalToneAnalyzer):

    def analyze_emotional_tone(self, transcription: str) -> CallEmotionalTone:
        return CallEmotionalTone.NEUTRAL