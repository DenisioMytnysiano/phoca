from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GetCategoryResponse:
    id: str
    title: str
    points: List[str]


@dataclass
class PostCategoryRequest:
    title: str
    points: List[str]

@dataclass
class UpdateCategoryRequest:
    title: Optional[str]
    points: List[str]
