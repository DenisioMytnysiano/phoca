import os

class WeaviateConfig:
    HOST = os.environ.get("WEAVIATE_HOST") or "localhost"
    PORT = os.environ.get("WEAVIATE_PORT") or 8090
    GRPC_PORT = os.environ.get("WEAVIATE_GRPC_PORT") or 50051