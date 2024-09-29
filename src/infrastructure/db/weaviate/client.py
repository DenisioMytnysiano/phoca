import weaviate
from infrastructure.db.weaviate.config import WeaviateConfig

client = weaviate.connect_to_local(
    host=WeaviateConfig.HOST,
    port=WeaviateConfig.PORT,
    grpc_port=WeaviateConfig.GRPC_PORT,
)