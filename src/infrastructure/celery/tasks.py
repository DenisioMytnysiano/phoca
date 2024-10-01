from celery import chain, chord, group
from domain.features.call_analysis.core.call_analysis_status import CallAnalysisStatus
from infrastructure.celery.celery import app
from infrastructure.celery.deps import (
    analysis_state_repository,
    analysis_result_repository,
    speech_recognizer,
    emotional_tone_analyzer,
    entities_extractor,
    category_classifier
)


@app.task(queue="download-and-transcribe")
def download_and_transcribe_audio(call_id, audio_url: str):
    transcription = speech_recognizer.transcribe(audio_url)
    analysis_result_repository.set_transcription(call_id, transcription)
    return transcription


@app.task(queue="identify-call-entities")
def identify_call_entities(transcription, call_id):
    entities = entities_extractor.extract_entities(transcription)
    analysis_result_repository.set_extracted_entities(call_id, entities)


@app.task(queue="identify-emotional-tone")
def identify_emotional_tone(transcription, call_id):
    emotional_tone = emotional_tone_analyzer.analyze_emotional_tone(transcription)
    analysis_result_repository.set_emotional_tone(call_id, emotional_tone)


@app.task(queue="classify-category")
def classify_category(transcription, call_id):
    category_classifier.classify(call_id, transcription)


@app.task(queue="update-analysis-status")
def set_status(call_id: str, status: CallAnalysisStatus):
    analysis_state_repository.set_status(call_id, status)


@app.task(queue="analyze-call")
def analyze_call(call_id: str, audio_url: str):
    workflow = chain(
        set_status.si(call_id, CallAnalysisStatus.IN_PROGRESS),
        download_and_transcribe_audio.si(call_id, audio_url),
        chord(
            group(
                identify_call_entities.s(call_id),
                identify_emotional_tone.s(call_id),
                classify_category.s(call_id),
            ),
            set_status.si(call_id, CallAnalysisStatus.FINISHED),
        ),
    )

    workflow.apply_async(link_error=set_status.si(call_id, CallAnalysisStatus.FAILED))
