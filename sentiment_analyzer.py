import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Stáhneme VADER lexikon, pokud není dostupný
nltk.download('vader_lexicon')

# Inicializace analyzátoru
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    """ Analyzuje sentiment textu a vrací kategorii a skóre """
    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score > 0.05:
        sentiment = "positive"
    elif sentiment_score < -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, sentiment_score


if __name__ == "__main__":
    test_text = "This series is absolutely amazing!"
    sentiment, score = analyze_sentiment(test_text)
    print(f"Text: {test_text}")
    print(f"Sentiment: {sentiment} (score: {score})")