import os

class TransformerKeywordsConfig:
    MODEL = os.environ.get("KEY_WORDS_EMBEDDING_MODEL") or "all-MiniLM-L6-v2"