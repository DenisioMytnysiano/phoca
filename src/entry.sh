#!/bin/bash
if [ "$APP_MODE" = "backend" ]; then
    echo "Starting FastAPI application..."
    exec python main.py
elif [ "$APP_MODE" = "celery" ]; then
    echo "Starting Celery worker..."
    exec celery -A infrastructure.celery.celery  worker --loglevel=INFO -Q download-and-transcribe,identify-call-entities,identify-emotional-tone,classify-category,update-analysis-status,analyze-call
else
    echo "Invalid APP_MODE. Please set APP_MODE to 'fastapi' or 'celery'."
    exit 1
fi