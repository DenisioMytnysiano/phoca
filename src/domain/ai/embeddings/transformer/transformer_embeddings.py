import numpy as np
from sentence_transformers import SentenceTransformer
from features.embeddings.embeddings import Embeddings
from features.embeddings.transformer.config import TransformerEmbeddingsConfig


class TransformerEmbeddings(Embeddings):

    def __init__(self) -> None:
        self.model = SentenceTransformer(TransformerEmbeddingsConfig.MODEL)

    def embed(self, text: str) -> np.array:
        return self.model.encode(text)


embeddings = TransformerEmbeddings()
