from contextlib import asynccontextmanager
import uvicorn
from dotenv import load_dotenv
from api.v1.api import api_router
from api.v1.deps import category_service
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domain.features.category.exceptions import DuplicateCategoryException
from infrastructure.db.weaviate.client import client as weaviate
from infrastructure.db.mongo.database import client as mongo

load_dotenv()

def initialize_categories():
    predefined_categories = [
        "Visa and Passport Services",
        "Diplomatic Inquiries",
        "Travel Advisories",
        "Consular Assistance",
        "Trade and Economic Cooperation"
    ]
    try:
        for category in predefined_categories:
            category_service.add_category(category, [])
    except DuplicateCategoryException:
        pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_categories()
    yield
    weaviate.close()
    mongo.close()


app = FastAPI(lifespan=lifespan, title="Phoca", openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, lifespan="on")
