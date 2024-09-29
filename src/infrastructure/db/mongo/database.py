from pymongo import MongoClient

from infrastructure.db.mongo.config import MongoConfig

client = MongoClient(MongoConfig.URL)
database = client.get_database(MongoConfig.DB_NAME)
