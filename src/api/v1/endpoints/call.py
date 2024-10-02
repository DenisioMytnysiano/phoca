from uuid import uuid4
from fastapi import APIRouter, HTTPException

from api.v1.schema.call import CreateCallRequest, CreateCallResponse, GetCallResponse
from domain.features.call_analysis.core.call_analysis_status import CallAnalysisStatus
from domain.features.call_analysis.core.exceptions import CallNotFoundException
from domain.features.call_analysis.entities_extraction.call_entity import CallEntity
from infrastructure.celery.tasks import analyze_call
from api.v1.deps import analysis_state_repository, analysis_result_repository, category_classifier

router = APIRouter()


@router.post("/", response_model=CreateCallResponse)
def create_call(request: CreateCallRequest):
    call_id = str(uuid4())
    analyze_call.delay(call_id, request.audio_url)
    analysis_state_repository.set_status(call_id, CallAnalysisStatus.ACCEPTED)
    return CreateCallResponse(call_id)



@router.post("/{call_id}", response_model=GetCallResponse)
def get_call(call_id: str):
    try:
        current_status = analysis_state_repository.get_status(call_id)
        if current_status in [CallAnalysisStatus.ACCEPTED, CallAnalysisStatus.IN_PROGRESS]:
            raise HTTPException(status_code=202)
        if current_status == CallAnalysisStatus.FAILED:
            raise HTTPException(status_code=422, detail="Call analysis failed.")

        analysis_result = analysis_result_repository.get_result(call_id)
        categories = category_classifier.get_result(call_id)
        return GetCallResponse(
            analysis_result.call_id,
            analysis_result.extracted_entities.get(CallEntity.CALLER),
            analysis_result.extracted_entities.get(CallEntity.CALLER_LOCATION),
            analysis_result.emotional_tone,
            analysis_result.transcription,
            categories
        )

    except CallNotFoundException:
        raise HTTPException(status_code=404, detail="Call not found")
