from dataclasses import asdict
from typing import List, Optional
from uuid import uuid4
from domain.features.category.category import Category
from domain.features.category.category_repository import CategoryRepository
from domain.features.category.exceptions import CategoryNotFoundException, DuplicateCategoryException
from pymongo.errors import DuplicateKeyError
from infrastructure.db.mongo.database import database


class MongoCategoryRepository(CategoryRepository):

    def __init__(self):
        self.collection = database.get_collection("categories")
        self.collection.create_index("id", unique=True)
        self.collection.create_index("title", unique=True)

    def get_categories(self) -> List[Category]:
        return [self.__document_to_category(doc) for doc in self.collection.find({})]
    
    def get_category(self, id: str) -> Optional[Category]:
        result = self.collection.find_one({"id": id})
        if result:
            return self.__document_to_category(result)

    def add_category(self, title: str, points: List[str]) -> Category:
        try:
            category = Category(str(uuid4()), title, points)
            self.collection.insert_one(asdict(category))
            return category
        except DuplicateKeyError:
            raise DuplicateCategoryException(title)

    
    def update_category(self, id: str, title: Optional[str], points: Optional[str]) -> Category:
        try:
            update_document = self.__create_update_document(title, points)
            if update_document:
                result = self.collection.update_one({"id": id}, {"$set": update_document})
                if result.matched_count == 0:
                    raise CategoryNotFoundException(id)
            return self.get_category(id)
        except DuplicateKeyError:
            raise DuplicateCategoryException(title)
    
    def delete_category(self, id: str):
        result = self.collection.delete_one({"id": id})
        if result.deleted_count == 0:
            raise CategoryNotFoundException(id)
        
    def __document_to_category(self, doc) -> Category:
        return Category(
            id=doc["id"],
            title=doc["title"],
            points=doc["points"]
        )
        
    def __create_update_document(self,  title: Optional[str], points: Optional[str]):
        update_document = dict()
        if title: 
            update_document["title"] = title
        if points:
            update_document["points"] = points
        return update_document
