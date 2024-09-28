import os


class WhisperSpeechRecognizerConfig:

    MODEL = os.environ.get("WHISPER_MODEL") or "base.en"
