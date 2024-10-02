import pytest
from typing import Optional

from domain.features.call_analysis.entities_extraction.call_entity import CallEntity
from domain.features.call_analysis.entities_extraction.ner.ner_call_entities_extractor import NerCallEntitiesExtractor


@pytest.fixture
def extractor():
    return NerCallEntitiesExtractor()

test_cases = [
    ("Hello, this is John Smith calling from Washington D.C. May I speak with Lee Jung-hoon, please? Certainly, Mr. Smith. This is Lee Jung-hoon speaking from Seoul. How can I assist you today? Thank you for taking my call, Mr. Lee. I'm reaching out regarding the upcoming trade negotiations between our countries. Of course, Mr. Smith. I've been briefed on the matter. What specific aspects would you like to discuss?",
     "John Smith", "Washington"),
    ("Good morning, I'm calling about the upcoming G20 summit. Is this the office of Prime Minister Trudeau? Yes, this is Justin Trudeau's office in Ottawa. How may I help you? I'm with the summit organizing committee, and we need to confirm some details about the Prime Minister's attendance. Certainly, I'd be happy to help with that. What information do you need?",
     "Trudeau", "Ottawa"),
    ("Hello, my name is Angela Merkel calling from Berlin. I'd like to speak with President Macron, please. Bonjour, Chancellor Merkel. This is President Macron. I'm currently in a secure location for a briefing. How can I assist you? Hello, President Macron. I wanted to discuss the upcoming EU budget negotiations. Do you have a few minutes?",
     "Angela Merkel", "Berlin"),
    ("Good day, this is Prime Minister Boris Johnson. One moment please, I'll see if the Chancellor is available. Hello, Prime Minister Johnson. This is Olaf Scholz. What can I do for you today? Chancellor Scholz, thank you for taking my call. I wanted to discuss the recent developments in our joint defense initiative.",
     "Boris Johnson", None),
    ("Hello, this is President Xi Jinping. I'm sorry, but President is currently unavailable. Would you like to leave a message or have him call you back? I see. Please inform him that I called regarding our upcoming bilateral summit. It's quite urgent that we speak soon.",
     "Xi Jinping", None),
    ("Good evening, this is Prime Minister Narendra Modi. May I speak with Prime Minister Kishida, please? Hello, Prime Minister Modi. This is Fumio Kishida speaking. How can I help you? Prime Minister Kishida, I'm calling to discuss the Quad meeting scheduled for next month. Do you have a few minutes to go over the agenda?",
     "Narendra Modi", None), 
    ("Hello, is this the foreign ministry? Yes, this is the foreign ministry. How may I assist you? I'm calling about the diplomat exchange program. I was told to contact this number for more information. Certainly, I can help you with that. What specific information are you looking for regarding the exchange program?",
     None, None),
    ("Hello, this is Ambassador Chen Wei calling from Beijing. I'm trying to reach Foreign Minister Youssef Bouhlel. One moment please. Hello, Ambassador Chen. This is Minister Bouhlel speaking from Tunis. I understand you're calling on behalf of President Xi? Yes, that's correct. President Xi has asked me to coordinate with you regarding his upcoming visit to Tunisia. Excellent, I'd be happy to discuss the details of President Xi's visit. What specific arrangements do we need to address?",
     "Chen Wei", "Beijing")
]
@pytest.mark.parametrize("transcription, expected_caller, expected_caller_location", test_cases, ids=range(len(test_cases)))
def test_given_transcription_when_extracting_entities_then_return_expected_entities(transcription: str, expected_caller: Optional[str], expected_caller_location: Optional[str], extractor):
    extracted_entities = extractor.extract_entities(transcription)
    expected_entities = {
        CallEntity.CALLER: expected_caller,
        CallEntity.CALLER_LOCATION: expected_caller_location,
    }
    expected_entities = {k: v for k, v in expected_entities.items() if v is not None}
    assert extracted_entities == expected_entities, f"Failed on transcription: {transcription}"

def test_given_empty_string_when_extracting_entities_then_return_empty_dict(extractor):
    assert extractor.extract_entities("") == {}