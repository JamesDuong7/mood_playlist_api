from transformers import pipeline   # type: ignore (transformers types unresolved by Pylance)
from typing import Any

# This sentiment pipeline analyzes text and determines if it's positive or negative.
sentiment_classifier = pipeline(    # type: ignore
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_mood_from_text(text: str) -> str:
    """
    Given a text input, determine and return a mood label:
    "happy", "sad", "calm", "energetic", or "tender".

    This function uses the sentiment analysis pipeline to first identify
    the sentiment (positive/negative) and then maps the result to a custom mood.
    """
    # Use sentiment classifier pipeline to analyze input text.
    result: list[dict[str, Any]] = sentiment_classifier(text)   # type: ignore (unclear pipeline return type)


    # Extract the label ("POSITIVE"/"NEGATIVE") from the classifier's result.
    label: str = str(result[0]['label'])        # type: ignore (partially unknown type from pipeline result)

    # Extract the confidence score (between 0 and 1) from the classifier's result.
    score: float = float(result[0]['score'])    # type: ignore (partially unknown type from pipeline result)

    # Map the sentiment result to your custom mood labels based on confidence levels.
    if label == "POSITIVE":
        if score > 0.9:
            return "energetic"
        elif score > 0.7:
            return "happy"
        else:
            return "calm"
    else:  # label is NEGATIVE
        if score > 0.9:
            return "sad"
        else:
            return "tender"
