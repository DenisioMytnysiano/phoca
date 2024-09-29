import numpy as np
from sentence_transformers import SentenceTransformer
from domain.ai.embeddings.embeddings import Embeddings
from domain.ai.embeddings.transformer.config import TransformerEmbeddingsConfig


class TransformerEmbeddings(Embeddings):

    def __init__(self) -> None:
        self.model = SentenceTransformer(TransformerEmbeddingsConfig.MODEL)

    def embed(self, text: str) -> np.array:
        return self.model.encode(text)


embeddings = TransformerEmbeddings()
