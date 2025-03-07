import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not available
nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """ Analyzes the sentiment of the text and returns the category and score """
    print("Analyzing sentiment...")
    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score > 0.05:
        sentiment = "positive"
    elif sentiment_score < -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, sentiment_score
#
# if __name__ == "__main__":
#     test_text = "This series is absolutely amazing!"
#     sentiment, score = analyze_sentiment(test_text)
#     #print(f"Text: {test_text}")
#     #print(f"Sentiment: {sentiment} (score: {score})")