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
        return "Good afternoon, Thomas. I hope you're doing well today. I wanted to touch base with you on an important issue regarding our mutual Visa and Passport Services between Ukraine and Germany. As you know, with the increase in travel from Ukraine to the EU, we've been receiving numerous inquiries about simplifying visa processing, especially for short-term stays. Could you give me an overview of Germany's current stance on this?"
        audio = whisperx.load_audio(audio_path)
        result = self.model.transcribe(audio, batch_size=4)
        result = whisperx.align(result["segments"], self.model_a, self.metadata, audio, "cpu", return_char_alignments=False)
        result  = "".join([segment["text"] for segment in result["segments"]])
        return result.strip()
