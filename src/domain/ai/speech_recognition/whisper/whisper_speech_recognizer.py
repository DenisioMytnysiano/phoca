import whisperx
from domain.ai.speech_recognition.speech_recognizer import SpeechRecognizer
from domain.ai.speech_recognition.whisper.config import WhisperSpeechRecognizerConfig

class WhisperSpeechRecognizer(SpeechRecognizer):

    def __init__(self):
        self.model = whisperx.load_model(WhisperSpeechRecognizerConfig.MODEL, "cpu", compute_type="float32")
        model_a, metadata = whisperx.load_align_model(language_code="en", device="cpu")
        self.model_a = model_a
        self.metadata = metadata

    def transcribe(self, audio_path: str) -> str:
        audio = whisperx.load_audio(audio_path)
        result = self.model.transcribe(audio, batch_size=4)
        result = whisperx.align(result["segments"], self.model_a, self.metadata, audio, "cpu", return_char_alignments=False)
        result  = "".join([segment["text"] for segment in result["segments"]])
        return result.strip()
