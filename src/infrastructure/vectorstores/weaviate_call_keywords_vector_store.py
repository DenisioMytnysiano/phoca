import numpy as np
from typing import List
from domain.ai.embeddings.embeddings import Embeddings
from domain.features.call_analysis.category_classification.vector_based.call_keywords_vector_store import CallKeywordsVectorStore


class WeaviateCallKeywordsVectorStore(CallKeywordsVectorStore):
    def __init__(self, embeddings: Embeddings):
        self.embedding_model = embeddings
        
    def insert(self, call_id: str, keywords: List[str]):
        return super().insert(call_id, keywords)

    def get(self, call_id: str) -> List[np.array]:
        return super().get(call_id)
