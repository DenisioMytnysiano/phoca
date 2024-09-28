from typing import List, Optional
from domain.features.category.category import Category
from domain.features.category.category_repository import CategoryRepository
from domain.features.category.category_vector_store import CategoryVectorStore


class CategoryService:

    def __init__(self, repository: CategoryRepository, vectorstore: CategoryVectorStore):
        self.repository = repository
        self.vectorstore = vectorstore

    def get_categories(self) -> List[Category]:
        return self.repository.get_categories()

    def add_category(self, name: str, points: List[str]) -> Category:
        category = self.repository.add_category(name, points)
        self.vectorstore.add_category(category)
        return category

    def update_category(self, id: str, name: Optional[str], points: Optional[str]) -> Category:
        category = self.repository.update_category(id, name, points)
        self.vectorstore.update_category(id, name, points)
        return category

    def delete_category(self, id: str):
        self.repository.delete_category(id)
        self.vectorstore.delete_category(id)