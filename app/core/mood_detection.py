from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Example usage:
# print(sentiment_classifier("I feel amazing today!"))

def detect_mood_from_text(text: str) -> str:
    """
    Detect user's mood based on their text input.
    Returns: happy, sad, calm, energetic, or tender
    """
    result = sentiment_classifier(text)[0]
    label = result['label']  # POSITIVE or NEGATIVE
    score = result['score']  # confidence (0-1)

    if label == "POSITIVE":
        if score > 0.9:
            return "energetic"
        elif score > 0.7:
            return "happy"
        else:
            return "calm"
    else:  # NEGATIVE
        if score > 0.9:
            return "sad"
        else:
            return "tender"
