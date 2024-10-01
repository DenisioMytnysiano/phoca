import pytest

from domain.ai.speech_recognition.whisper.whisper_speech_recognizer import WhisperSpeechRecognizer


@pytest.fixture
def transcriber():
    return WhisperSpeechRecognizer()

test_cases = [
    ("https://callhounds.com/wp-content/uploads/2020/10/Fundraising.mp3", "Good evening, this is Makkad Buu Chair of Team Auto Orleans.On behalf of Team Auto Orleans, I wish to invite you to join us as a barbecue this Saturday, October 1st from 11.30 to 2 p.m.at the Orleans Crime Servants Center on Central Boulevard.This event is open to all members of the community, so please come and have a burger with us.Volunteer donations on behalf of the Canadian Red Cross and support of the victim of Hurricane Katrina and Rita will be accepted. I look forward to meeting with you there."),
    ("https://callhounds.com/wp-content/uploads/2022/12/Technician-Assignment.wav", "Hello, is this Jeff?It sure is.Hi, this is Tella from Barrester.I'm calling because I have an open ticket for you in 100 East Tyler Street, Tampa, Florida.The zip code is 33606.And this is $0.04 Air Direct Unit to complete installation.Are you available for this work order? At the moment, I'm not in Tampa right now.I live in Orlando.You said it's an open ticket, like it's on my log or something.This is a work order for you.The work request number is 474424.But what I was saying, is this like a new order or no?Is this a new ticket?Sorry.Is this a new ticket?Yes, sir.Are you trying to?Oh, OK.That's what I'm saying.I don't live in Canada.It's kind of out of my way. I would be able to cover that this week or anything.Okay, how about this?Another ticket that I have here in 5281 Airport Service Road, Tampa, Florida.There's the code 33607.And this is for miscellaneous services.Right now, like this week, I live in Orlando, so I'm not anywhere near Tampa.I'm like two and a half away from Tampa, so I couldn't cover anything over there this week.All right, okay. So thank you so much for taking this call.Have a great day.")
]

@pytest.mark.parametrize("audio_url, expected_trancription", test_cases, ids=range(len(test_cases)))
def test_given_audio_url_when_transcribe_then_return_correct_transription(audio_url: str, expected_trancription: str, transcriber):
    assert transcriber.transcribe(audio_url) == expected_trancription
