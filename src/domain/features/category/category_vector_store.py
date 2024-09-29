import numpy as np
from typing import Protocol, List
from domain.features.category.category import Category


class CategoryVectorStore(Protocol):

    def add_category(self, category: Category):
        pass

    def update_category(self, category: Category):
        pass

    def get_similar(self, vectors: List[np.array]) -> list[str]:
        pass

    def delete_category(self, id: str):
        pass
