from dataclasses import dataclass
from typing import List, Optional

from domain.features.category.category import Category


@dataclass
class GetCategoryResponse:
    id: str
    title: str
    points: List[str]

    @staticmethod
    def from_category(category: Category):
        return GetCategoryResponse(
            id=category.id, title=category.title, points=category.points)


@dataclass
class PostCategoryRequest:
    title: str
    points: List[str]


@dataclass
class UpdateCategoryRequest:
    title: Optional[str]
    points: List[str]
