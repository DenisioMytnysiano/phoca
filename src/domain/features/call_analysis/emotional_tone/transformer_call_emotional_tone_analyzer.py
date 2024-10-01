import torch
from typing import List, Dict
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from domain.features.call_analysis.emotional_tone.call_emotional_tone import CallEmotionalTone
from domain.features.call_analysis.emotional_tone.call_emotional_tone_analyzer import CallEmotionalToneAnalyzer

class TransformerCallEmotionalToneAnalyzer(CallEmotionalToneAnalyzer):

    def __init__(self, emotion_model_name: str = "j-hartmann/emotion-english-distilroberta-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
        self.max_length = self.tokenizer.model_max_length

    def analyze_emotional_tone(self, transcription: str) -> CallEmotionalTone:
        chunks = self._split_into_chunks(transcription)
        emotion_scores = self.__analyze_emotions(chunks)
        combined_tone = self.__combine_predictions(emotion_scores)
        return combined_tone

    def _split_into_chunks(self, text: str) -> List[str]:
        tokens = self.tokenizer.encode(text, add_special_tokens=False)
        chunks = []

        for i in range(0, len(tokens), self.max_length-2):
            chunk_tokens = tokens[i:i + self.max_length-2]
            chunk_text = self.tokenizer.decode(chunk_tokens)
            chunks.append(chunk_text)

        return chunks

    def __analyze_emotions(self, chunks: List[str]) -> Dict[str, float]:
        emotion_scores = {
            "anger": 0.0, "disgust": 0.0, "fear": 0.0, "joy": 0.0, 
            "neutral": 0.0, "sadness": 0.0, "surprise": 0.0
        }

        for chunk in chunks:
            inputs = self.tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=self.max_length)
            with torch.no_grad():
                outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            for emotion, score in zip(emotion_scores.keys(), probs[0].tolist()):
                emotion_scores[emotion] += score

        return emotion_scores

    def __combine_predictions(self, emotion_scores: Dict[str, float]) -> CallEmotionalTone:
        combined_scores = {
            CallEmotionalTone.ANGRY: emotion_scores["anger"],
            CallEmotionalTone.POSITIVE: emotion_scores["joy"],
            CallEmotionalTone.NEGATIVE: emotion_scores["disgust"] + emotion_scores["sadness"] + emotion_scores["fear"],
            CallEmotionalTone.NEUTRAL: emotion_scores["neutral"] + emotion_scores["surprise"]
        }
        return max(combined_scores, key=combined_scores.get)
