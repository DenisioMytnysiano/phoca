import os

class TransformerEmbeddingsConfig:
    MODEL = os.environ.get("EMBEDDING_MODEL") or "all-MiniLM-L6-v2"