import re

URL_REGEX = re.compile(
    r'^(http:\/\/|https:\/\/)'
    r'([a-zA-Z0-9\-._~:/?#\[\]@!$&\'()*+,;=]+)'
)

SUPPORTED_EXTENSIONS = ('.wav', '.mp3')

class CallUrlValidator:

    def validate(self, audio_url: str):
        if not URL_REGEX.match(audio_url):
            raise ValueError("Invalid URL format.")
        
        if not audio_url.lower().endswith(SUPPORTED_EXTENSIONS):
            raise ValueError("Invalid file extension. Only '.wav' and '.mp3' files are supported.")
