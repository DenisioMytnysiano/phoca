from domain.features.category.category_service import CategoryService
from infrastructure.repositories.mongo_category_repository import MongoCategoryRepository
from infrastructure.vectorstores.weaviate_category_vector_store import WeaviateCategoryVectorStore


category_repository = MongoCategoryRepository()
category_vector_store = WeaviateCategoryVectorStore()
category_service = CategoryService(category_repository, category_vector_store)