import os


class RabbitMQConfig:
    HOST = os.environ.get("RABBITMQ_HOST") or "localhost"
    PORT = os.environ.get("RABBITMQ_PORT") or 5672
    USER = os.environ.get("RABBITMQ_USER") or "user"
    PASSWORD = os.environ.get("RABBITMQ_PASSWORD") or "password"
    URL = f"amqp://{USER}:{PASSWORD}@{HOST}:{PORT}"
