import numpy as np
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from domain.ai.embeddings.embeddings import Embeddings
from domain.ai.keywords.transformer.config import TransformerKeywordsConfig


class TransformerKeywordsExtractor(Embeddings):

    def __init__(self):
        self.model = KeyBERT(SentenceTransformer(TransformerKeywordsConfig.MODEL))

    def embed(self, text: str) -> np.array:
        return [
            item[0]
            for item in self.model.extract_keywords(
                text,
                keyphrase_ngram_range=(1, 2),
                stop_words="english",
                top_n=20,
                use_mmr=True,
                diversity=0.3,
            )
        ]
