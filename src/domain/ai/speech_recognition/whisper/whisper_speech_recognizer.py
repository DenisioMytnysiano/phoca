import whisper
import numpy as np
from features.speech_recognition.speech_recognizer import SpeechRecognizer
from features.speech_recognition.whisper.config import WhisperSpeechRecognizerConfig


class WhisperSpeechRecognizer(SpeechRecognizer):

    def __init__(self):
        self.model = whisper.load_model(WhisperSpeechRecognizerConfig.MODEL)

    def transcribe(self, audio: np.array) -> str:
        return self.model.transcribe(audio).text


recognizer = WhisperSpeechRecognizer()