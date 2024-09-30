from domain.ai.speech_recognition.speech_recognizer import SpeechRecognizer
from domain.features.call_analysis.transcription.call_downloader import CallDownloader


class CallTranscriber:

    def __init__(self, speech_recognizer: SpeechRecognizer, downloader: CallDownloader):
        self.speech_recognizer = speech_recognizer
        self.downloader = downloader

    def transcribe(self, audio_url: str) -> str:
        return "TEST TRANSCRIPTION"
        path = self.downloader.download(audio_url)
        transcription = self.speech_recognizer.transcribe(path)
        self.downloader.delete(path)
        return transcription
