## Tecnhological Stack
Project is tightly related to AI/ML, thai is why i chose Python to implement the solution.

The main libraries used in the project include:
fastapi, pydantic, celery, sentence_transformers, keybert, pytorch, whisperx, pytest, pymongo, 

As the storage for analysis results I selected MongoDB, as a higly scalable and efficient document based database, and Weaviate as the storage for the vector embeddings (refer to section 'Calls Categorization').

As the communication transport between backend and workers I selected RabbitMQ, since it is de-facto standard approach for tasks distribution in python applications and it has great support in celery.


## Solution Architecture
As the main purpose of the solution is to analyze big amounts of phone calls data, this system was designed as highly scalable and distributed. Currenty the system consists of:
- backend that is responsible for extracting the results and presenting them to user via API
- workers that are responsible for audio and text analysis tasks

The following architecture allows to scale components individually according to hardware requirements, traffic load etc.

![](images/architecture.png)

On the component level I used hexagonal architecture. It allows to build modular and highly testable systems that are able to be easily adjusted to new requirements. There are three layers:
- api: this layer is responsible for REST API, it's schema and input validation
- domain: this layer contains adapter for AI models and business logic regarding categories and call analysis
- infrastructure: this layer contains implementation for DB adapters, repositories and workflow setup for call analysis

## Text Analysis
Text processing pipeline is optimized to be highly distributed and parallel. At first, audio call transcription is obtained. Then three parallel jobs are triggered: emotional tone analysis, entities extraction and categorization. In celery worflow looks the following way:
```python
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
```
Result of the call analysis are stored in MongoDB with the following data model:
```json
{
    "call_id": "string",
    "emotional_tone": "string",
    "transcription": "string",
    "extracted_entities": {
        "ENTITY_TYPE_1": "string",
        "ENTITY_TYPE_2": "string"
    }
}
```
### Phone Call Transcription

### Emotional Tone Analysis

### Call Entities Extraction

### Calls Categorization

## How To Start Application
To start an application please use the following command:
```
docker compose up --build
```

## Testing
To run unit tests in docker container please use the following command: 
```
docker exec devchallenge-xxi-backend bash -c "cd /app/tests && pytest -v"
```

## Corner Cases Covered
- **large files handling:** in case file content cannot fit into the model, it is splitted into chunks and then results are aggregated
- **calls categorization after category updates and deletes:** by utilizing shared latent vector space for key topics in categories and keywords in calls it is not needed to recalculate all categorization results for each of the calls

- **in case of error during the analysis user will be given a correspoding details**

- **system works correstly in case there is noise in the input audio**

- **system works correctly for different accents in english**

- **all components of the system don't send data to external APIs which is critical for such a solution**

- **system chooses the surname and name of the caller in case both are present**

- **each call can have multiple categories or no category at all**

- **concurrent analysis runs and asynchronous processing**: system can handle multiple analysis requests simultaneously balancing the load between workers

## Further Steps
- Deploy application in the cloud

- Utilize GPU for faster speech-to-text

- Speech diarization in processing pipeline

- LLM based embeddings for categories classification

- Open souce LLM (like llama) to conduct text analysis
