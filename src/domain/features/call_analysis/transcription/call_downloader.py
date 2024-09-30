import os


class CallDownloaderConfig:
    TMP_FOLDER = os.environ.get("TMP_FOLDER") or "/tmp"


class CallDownloader:

    def __init__(self, directory: str):
        self.directory = directory

    def download(self, audio_url: str) -> str:
        pass

    def delete(self, audio_url: str) -> str:
        pass
