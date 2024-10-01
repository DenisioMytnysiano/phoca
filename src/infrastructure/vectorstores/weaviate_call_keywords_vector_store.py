import numpy as np
from typing import List
from infrastructure.db.weaviate.client import client
from weaviate.classes.query import Filter
from domain.ai.embeddings.embeddings import Embeddings
from domain.features.call_analysis.category_classification.vector_based.call_keywords_vector_store import CallKeywordsVectorStore

class WeaviateCallKeywordsVectorStore(CallKeywordsVectorStore):
    def __init__(self, embeddings: Embeddings):
        self.collection=client.collections.get("call-keywords")
        self.embedding_model = embeddings
    
    def insert(self, call_id: str, keywords: List[str]):
        self.delete(call_id)
        self.__insert(call_id, keywords)

    def delete(self, call_id: str):
        return self.collection.data.delete_many(
            where=Filter.by_property("call_id").equal(call_id)
        )

    def get(self, call_id: str) -> List[np.array]:
        objects = self.collection.query.fetch_objects(
            filters=Filter.by_property("call_id").equal(call_id),
            include_vector=True
        )
        return [o.vector for o in objects]
 
    def __insert(self, call_id, keywords):
        vectors = [self.embedding_model.embed(keyword) for keyword in keywords]
        properties = [self.__create_keyword_document(call_id, keyword) for keyword in keywords]
        with self.collection.batch.dynamic() as batch:
            for p, vector in zip(properties, vectors):
                batch.add_object(
                    properties=p,
                    vector=vector
                )

    def __create_keyword_document(self, call_id, keyword):
        return {
            "call_id": call_id,
            "keyword": keyword
        }
