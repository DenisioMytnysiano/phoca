from typing import List
from fastapi import APIRouter

from api.v1.schema.call import CreateCallRequest, CreateCallResponse, GetCallResponse


router = APIRouter()


@router.post("/", response_model=List[CreateCallResponse])
def create_call(request: CreateCallRequest):
    pass


@router.post("/{call_id}", response_model=GetCallResponse)
def get_call(call_id: str):
    pass
