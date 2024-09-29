from pymongo import MongoClient

from infrastructure.db.mongo.config import MongoConfig

uri = f"mongodb://{MongoConfig.USER}:{MongoConfig.PASSWORD}@{MongoConfig.HOST}:{MongoConfig.PORT}"
client = MongoClient(uri)
database = client.get_database(MongoConfig.DB_NAME)
