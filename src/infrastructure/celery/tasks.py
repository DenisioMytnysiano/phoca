from celery import chain, chord, group
from infrastructure.celery.celery import app


@app.task(queue="download-and-transcribe")
def download_and_transcribe_audio(call_id, audio_url: str):
    print(f"accepted download {call_id} {audio_url}")
    return "Test transcription"


@app.task(queue="identify-caller-and-location")
def identify_caller_and_location(transcription, call_id):
    print(f"accepted caller {call_id} transcription {transcription}")


@app.task(queue="identify-emotional-tone")
def identify_emotional_tone(transcription, call_id):
    print(f"accepted emotional tone {call_id} transcription {transcription}")


@app.task(queue="embed-to-topics-space")
def embed_to_topics_space(transcription, call_id):
    print(f"accepted embed {call_id} transcription {transcription}")


@app.task(queue="update-analysis-status")
def set_status(call_id: str, status: str, exc=None, traceback=None):
    print(f"accepted set status {call_id} status {status}")


@app.task(queue="analyze-call")
def analyze_call(call_id: str, audio_url: str):
    workflow = chain(
        set_status.si(call_id, "Started"),
        download_and_transcribe_audio.si(call_id, audio_url),
        chord(
            group(
                identify_caller_and_location.s(call_id),
                identify_emotional_tone.s(call_id),
                embed_to_topics_space.s(call_id),
            ),
            set_status.si(call_id, "Finished"),
        ),
    )

    workflow.apply_async(link_error=set_status.si(call_id, "Failed"))
