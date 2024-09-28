from typing import List
from fastapi import APIRouter, HTTPException
from api.v1.deps import category_service
from api.v1.schema.category import GetCategoryResponse, PostCategoryRequest, UpdateCategoryRequest
from domain.features.category.exceptions import CategoryNotFoundException, DuplicateCategoryException


router = APIRouter()


@router.get("/", response_model=List[GetCategoryResponse])
def get_categories():
    return [GetCategoryResponse.from_category(category)
             for category in category_service.get_categories()]


@router.post("/", response_model=GetCategoryResponse, status_code=200)
def add_category(request: PostCategoryRequest):
    try:
        category = category_service.add_category(request.title, request.points)
        return GetCategoryResponse.from_category(category)
    except DuplicateCategoryException:
        raise HTTPException(status_code=422, detail=f"Category with title '{request.title}' is already present.")
    

@router.put("/{category_id}", response_model=GetCategoryResponse, status_code=201)
def update_category(category_id: str, request: UpdateCategoryRequest):
    try:
        new_category = category_service.update_category(category_id, request.title, request.points)
        return GetCategoryResponse.from_category(new_category)
    except DuplicateCategoryException:
        raise HTTPException(status_code=422, detail=f"Category with title '{request.title}' is already present.")
    except CategoryNotFoundException:
        raise HTTPException(status_code=404, detail="Category not found")

@router.delete("/{category_id}")
def delete_category(category_id: str):
    try:
        category_service.delete_category(category_id)
    except CategoryNotFoundException:
        raise HTTPException(status_code=404, detail="Category not found")
