from typing import List, Optional, Protocol

from domain.features.category.category import Category


class CategoryRepository(Protocol):

    def get_categories(self) -> Optional[Category]:
        pass

    def add_category(self, title: str, points: List[str]) -> Category:
        pass

    def update_category(self, id: str, title: Optional[str], points: Optional[str]) -> Category:
        pass

    def delete_category(self, id: str):
        pass
