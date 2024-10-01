import pytest
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.emotional_tone.transformer_call_emotional_tone_analyzer import TransformerCallEmotionalToneAnalyzer

test_cases = [
    (
        """We are delighted to announce that both parties have reached a mutually beneficial agreement 
        after months of intense negotiations. This landmark deal represents a significant step forward 
        in our bilateral relations and opens up new avenues for cooperation in trade, technology, and 
        cultural exchange. We look forward to the positive impact this will have on our respective economies 
        and the well-being of our citizens.""",
        CallEmotionalTone.POSITIVE
    ),
    (
        """The delegation expresses its profound disappointment in the lack of progress during recent negotiations. 
        Despite our best efforts and numerous concessions, we find ourselves at an impasse. The current 
        proposals fall far short of addressing the critical issues at hand, and we are concerned about 
        the long-term implications of this stalemate. We urge our counterparts to reconsider their position 
        and return to the table with a more constructive approach.""",
        CallEmotionalTone.NEGATIVE
    ),
    (
        """Our nation categorically rejects these baseless accusations and demands an immediate retraction. 
        We are outraged by the blatant disregard for diplomatic norms and the deliberate attempt to 
        undermine our sovereignty. Such provocative statements not only damage bilateral relations but 
        also threaten regional stability. We reserve the right to take all necessary measures to defend 
        our national interests and call on the international community to condemn these unfounded allegations.""",
        CallEmotionalTone.ANGRY
    ),
    (
        """While we appreciate the efforts made and acknowledge the potential benefits of the proposed agreement, 
        we must regrettably decline the current offer. After careful consideration and extensive 
        consultations with our experts, we have concluded that several key provisions are not aligned 
        with our long-term strategic interests. We remain open to further dialogue and hope that future 
        negotiations can address these concerns in a manner satisfactory to all parties involved.""",
        CallEmotionalTone.NEGATIVE
    ),
    (
        """We are pleased to report significant advancements in our bilateral relations following the 
        recent high-level summit. The constructive dialogue has led to breakthroughs in several 
        long-standing issues, including trade imbalances, security cooperation, and environmental 
        protection initiatives. These positive developments pave the way for a new era of partnership 
        and mutual prosperity. We commend the spirit of cooperation demonstrated by all participants 
        and look forward to building on this momentum.""",
        CallEmotionalTone.POSITIVE
    ),
    (
        """The ministry strongly condemns these provocative actions and calls for an immediate cessation 
        of hostilities. The recent escalation of military activities in the disputed region not only 
        violates multiple UN resolutions but also poses a grave threat to regional peace and stability. 
        We demand that all parties involved immediately withdraw their forces and return to the 
        negotiating table. Any further aggression will be met with a firm and decisive response.""",
        CallEmotionalTone.ANGRY
    ),
    (
        """We extend our warmest congratulations on the successful conclusion of the trade negotiations. 
        This comprehensive agreement marks a milestone in our economic partnership and reflects the 
        shared commitment to fostering growth and innovation. The provisions outlined in the deal 
        will create numerous opportunities for businesses and entrepreneurs, stimulate job creation, 
        and enhance competitiveness in global markets. We look forward to the swift implementation 
        of this agreement and the prosperity it will bring to both our nations.""",
        CallEmotionalTone.POSITIVE
    ),
    (
        """The delegation expresses deep concern over the recent developments and urges all parties to 
        exercise restraint. The escalating tensions in the region have the potential to undermine 
        years of diplomatic efforts and jeopardize the fragile peace process. We are disappointed 
        by the lack of adherence to previously agreed-upon frameworks and call on all stakeholders 
        to recommit to dialogue and de-escalation. It is imperative that we work collectively to 
        address the root causes of the conflict and find a sustainable, peaceful resolution.""",
        CallEmotionalTone.NEGATIVE
    )
]

@pytest.fixture
def analyzer():
    return TransformerCallEmotionalToneAnalyzer()

@pytest.mark.parametrize("diplomatic_text, expected_tone", test_cases, ids=range(len(test_cases)))
def test_given_diplomatic_text_when_analyzing_emotional_tone_then_correct_tone_is_returned(analyzer, diplomatic_text, expected_tone):
    assert analyzer.analyze_emotional_tone(diplomatic_text) == expected_tone
