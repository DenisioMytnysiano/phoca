from typing import List
from fastapi import APIRouter

from api.v1.schema.category import GetCategoryResponse, PostCategoryRequest, UpdateCategoryRequest


router = APIRouter()


@router.get("/", response_model=List[GetCategoryResponse])
def get_categories():
    pass


@router.post("/", response_model=GetCategoryResponse)
def add_category(request: PostCategoryRequest):
    pass


@router.put("/{category_id}", response_model=GetCategoryResponse)
def update_category(category_id: str, request: UpdateCategoryRequest):
    pass


@router.delete("/{category_id}")
def delete_category(category_id: str):
    pass
