from typing import List
from uuid import uuid4
from fastapi import APIRouter

from api.v1.schema.call import CreateCallRequest, CreateCallResponse, GetCallResponse
from infrastructure.celery.tasks import analyze_call


router = APIRouter()


@router.post("/", response_model=CreateCallResponse)
def create_call(request: CreateCallRequest):
    call_id = str(uuid4())
    analyze_call.delay(call_id, request.audio_url)
    return CreateCallResponse(call_id)


@router.post("/{call_id}", response_model=GetCallResponse)
def get_call(call_id: str):
    pass
