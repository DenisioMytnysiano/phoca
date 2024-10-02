import os

class TransformerEmbeddingsConfig:
    MODEL = os.environ.get("EMBEDDING_MODEL") or "all-mpnet-base-v2"