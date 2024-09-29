from celery import Celery
from infrastructure.messaging.rabbitmq.config import RabbitMQConfig
from infrastructure.db.mongo.config import MongoConfig
app = Celery()

# Create Celery app
app = Celery('phoca', include=["infrastructure.celery.tasks"])

app.conf.update(
    broker_url=RabbitMQConfig.URL,
    result_backend=MongoConfig.URL,
    mongodb_backend_settings = {
        "database": MongoConfig.DB_NAME,
        "taskmeta_collection": "celery-task-meta"
    },
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)
