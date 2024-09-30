from typing import List
from domain.features.call_analysis.category_classification.call_category_classifier import CallCategoryClassifier
from domain.ai.keywords.keywords_extractor import KeywordsExtractor
from domain.features.call_analysis.category_classification.vector_based.call_keywords_vector_store import CallKeywordsVectorStore
from domain.features.category.category_vector_store import CategoryVectorStore


class VectorBasedCallCategoryClassifier(CallCategoryClassifier):

    def __init__(
        self,
        keywords_extractor: KeywordsExtractor,
        keywords_store: CallKeywordsVectorStore,
        category_store: CategoryVectorStore,
    ):
        self.keywords_extractor = keywords_extractor
        self.keywords_store = keywords_store
        self.category_store = category_store

    def classify(self, call_id: str, transcription: str):
        keywords = self.keywords_extractor.extract(transcription)
        self.keywords_store.insert(call_id, keywords)

    def get_result(self, call_id: str) -> List[str]:
        result = set()
        keyword_vectors = self.keywords_store.get(call_id)
        for keyword_vector in keyword_vectors:
            for category in self.category_store.get_similar(keyword_vector):
                result.add(category)
        return result
