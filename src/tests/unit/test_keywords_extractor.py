import pytest
from domain.ai.keywords.transformer.transformer_keywords_extractor import TransformerKeywordsExtractor

@pytest.fixture
def extractor():
    return TransformerKeywordsExtractor()

def test_given_empty_text_when_extracting_keywords_then_return_empty_list(extractor):
    result = extractor.embed("")
    assert isinstance(result, list)
    assert len(result) == 0

def test_given_single_word_when_extracting_keywords_then_return_lowercase_word(extractor):
    result = extractor.embed("Security")
    assert len(result) == 1
    assert result[0] == "security"

def test_given_short_text_when_extracting_keywords_then_return_non_empty_list_of_strings(extractor):
    result = extractor.embed("Diplomacy in international relations")
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(keyword, str) for keyword in result)

def test_given_long_text_when_extracting_keywords_then_return_list_of_up_to_20_strings(extractor):
    long_text = """
    Diplomacy is the art and practice of conducting negotiations between representatives of states or groups. 
    It usually refers to international diplomacy, the conduct of international relations through the 
    intercession of professional diplomats with regard to issues of peace-making, trade, war, economics, 
    culture, environment, and human rights. International treaties are usually negotiated by diplomats 
    prior to endorsement by national politicians.
    """
    result = extractor.embed(long_text)
    assert isinstance(result, list)
    assert len(result) > 0
    assert len(result) <= 20
    assert all(isinstance(keyword, str) for keyword in result)

test_cases = [
    ("The United Nations plays a crucial role in maintaining international peace and security.", ["united nations", "international peace", "security", "crucial role"]),
    ("The Paris Agreement aims to combat climate change and accelerate actions towards a sustainable low carbon future.", ["paris agreement", "climate change", "sustainable future", "low carbon"]),
    ("NATO, or the North Atlantic Treaty Organization, is a military alliance between 30 European and North American countries.", ["nato", "military alliance", "european countries", "north american"]),
    ("The World Trade Organization deals with the rules of trade between nations at a global or near-global level.", ["world trade", "trade organization", "trade rules", "global level"]),
    ("The International Court of Justice is the principal judicial organ of the United Nations.", ["international court", "judicial organ", "united nations"]),
    ("Diplomatic immunity is a form of legal immunity that ensures diplomats are given safe passage and are considered not susceptible to lawsuit or prosecution under the host country's laws.",["diplomatic immunity", "legal immunity", "safe passage", "host country"]),
    ("The G20 is an international forum for the governments and central bank governors from 19 countries and the European Union.", ["g20", "international forum", "central bank", "european union"]),
    ("The Non-Proliferation Treaty aims to prevent the spread of nuclear weapons and weapons technology, to promote cooperation in the peaceful uses of nuclear energy, and to further the goal of achieving nuclear disarmament.", ["non-proliferation", "nuclear weapons", "weapons technology", "nuclear energy", "nuclear disarmament"]),
    ("Soft power is the ability to attract and co-opt, rather than coerce. It is the ability to shape the preferences of others through appeal and attraction.", ["soft power", "attract", "co-opt", "shape preferences"]),
    ("The Vienna Convention on Diplomatic Relations of 1961 is an international treaty that defines a framework for diplomatic relations between independent countries.", ["vienna convention", "diplomatic relations", "international treaty", "independent countries"])
]

@pytest.mark.parametrize("text, expected_keywords", test_cases, ids=range(len(test_cases)))
def test_given_diplomatic_text_when_extracting_keywords_then_return_relevant_keywords(text, expected_keywords, extractor):
    result = extractor.embed(text)
    assert any(keyword in result for keyword in expected_keywords)

def test_given_text_with_multiple_words_when_extracting_keywords_then_return_keywords_of_up_to_two_words(extractor):
    text = "The Paris Agreement is an international treaty on climate change."
    result = extractor.embed(text)
    assert any(len(keyword.split()) <= 2 for keyword in result)

def test_given_text_with_stop_words_when_extracting_keywords_then_exclude_stop_words(extractor):
    text = "The and of in on are common stop words in English."
    result = extractor.embed(text)
    stop_words = ["the", "and", "of", "in", "on", "are"]
    assert all(keyword.lower() not in stop_words for keyword in result)

def test_given_same_text_when_extracting_keywords_multiple_times_then_return_consistent_results(extractor):
    text = "Diplomatic negotiations often involve complex international relations."
    result1 = extractor.embed(text)
    result2 = extractor.embed(text)
    assert result1 == result2

def test_given_different_texts_when_extracting_keywords_then_return_different_results(extractor):
    text1 = "Climate change is a global challenge."
    text2 = "Economic sanctions can be used as a diplomatic tool."
    result1 = extractor.embed(text1)
    result2 = extractor.embed(text2)
    assert result1 != result2

def test_given_any_text_when_extracting_keywords_then_return_list_of_strings(extractor):
    text = "Diplomacy requires skilled communication and negotiation."
    result = extractor.embed(text)
    assert isinstance(result, list)
    assert all(isinstance(keyword, str) for keyword in result)
