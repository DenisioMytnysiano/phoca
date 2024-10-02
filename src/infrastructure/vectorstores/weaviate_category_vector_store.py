from typing import List
import numpy as np
from domain.features.category.category import Category
from domain.features.category.category_vector_store import CategoryVectorStore
from infrastructure.db.weaviate.client import client
from domain.ai.embeddings.embeddings import Embeddings
from weaviate.classes.query import Filter, MetadataQuery

class WeaviateCategoryVectorStore(CategoryVectorStore):

    def __init__(self, embeddings: Embeddings):
        if not client.collections.exists("categories"):
            client.collections.create("categories")
        self.collection = client.collections.get("categories")
        self.embedding_model = embeddings

    def add_category(self, category: Category):
        properties = self.__create_properties(category)
        vectors = self.__embed_text(properties)
        with self.collection.batch.dynamic() as batch:
            for p, vector in zip(properties, vectors):
                batch.add_object(
                    properties=p,
                    vector=vector
                )

    def update_category(self, category: Category):
        self.delete_category(category.id)
        self.add_category(category)

    def get_similar(self, vectors: List[np.array], threshold=0.5) -> list[str]:
        result = set()
        for vector in vectors:
            response = self.collection.query.near_vector(
                near_vector=vector,
                distance=threshold,
                return_metadata=MetadataQuery(distance=True)
            )
            for o in response.objects:
                result.add(o.properties["category"])
        return list(result)


    def delete_category(self, id: str):
        self.collection.data.delete_many(where=Filter.by_property("category_id").equal(id))

    def __create_properties(self, category):
        properties = []
        properties.extend([self.__create_key_point_document(category.id, category.title, point) for point in category.points])
        properties.append(self.__create_category_document(category.id, category.title))
        return properties
    
    def __embed_text(self, properties):
        return [self.embedding_model.embed(prop["text"]) for prop in properties]

    def __create_category_document(self, id, topic):
        return {
            "category_id": id,
            "type": "category",
            "category": topic,
            "text": topic
        }
    
    def __create_key_point_document(self, id, category, point):
        return {
            "category_id": id,
            "category": category,
            "type": "key-point",
            "text": point
        }
