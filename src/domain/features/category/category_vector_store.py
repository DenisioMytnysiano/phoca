from typing import Optional, Protocol, List
from domain.features.category.category import Category


class CategoryVectorStore(Protocol):

    def add_category(self, category: Category):
        pass

    def update_category(self, id: str, name: Optional[str], points: Optional[str]):
        pass

    def get_similar(self, categories: List[str]) -> list[str]:
        pass

    def delete_category(self, id: str):
        pass
