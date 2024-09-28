from dataclasses import dataclass
from typing import List


@dataclass
class Category:
    id: str
    title: str
    points: List[str]
