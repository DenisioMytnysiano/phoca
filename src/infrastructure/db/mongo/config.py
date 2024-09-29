import os


class MongoConfig:
    HOST = os.environ.get("MONGO_HOST") or "localhost"
    PORT = os.environ.get("MONGO_PORT") or 27017
    USER = os.environ.get("MONGO_USER") or "root"
    PASSWORD = os.environ.get("MONGO_PASSWORD") or "password"
    DB_NAME = os.environ.get("MONGO_DB_NAME") or "devchallenge-xxi"
