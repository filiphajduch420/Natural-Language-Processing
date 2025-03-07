import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import string
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

def generate_wordcloud(words, filename="wordcloud.png"):
    """ Generates a word cloud from the given text or list of words """
    print("Generating word cloud...")
    text = " ".join(words)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(filename)
    plt.show()

def analyze_words(reviews):
    """ Analyzes words in reviews – most common and longest words """
    print("Analyzing words in reviews...")
    text = " ".join(reviews).lower()
    words = [word.strip(string.punctuation) for word in text.split()]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word and word not in stop_words]

    # 30 most common words
    most_common_words = [word for word, _ in Counter(words).most_common(30)]

    # 30 longest words
    longest_words = sorted(set(words), key=len, reverse=True)[:30]

    return most_common_words, longest_words

# if __name__ == "__main__":
#     test_reviews = [
#         "This movie is absolutely fantastic! I loved every second of it.",
#         "It was an average experience. Nothing special, nothing terrible.",
#         "I really hated this movie. It was a complete waste of time."
#     ]
#
#     # Simulate sentiment analysis
#     test_sentiments = [
#         (test_reviews[0], "positive", 0.85),
#         (test_reviews[1], "neutral", 0.00),
#         (test_reviews[2], "negative", -0.75)
#     ]
#
#     # Generate word cloud for reviews
#     generate_wordcloud(test_reviews, "test_wordcloud.png")
#
#     # Display sentiment table
#     display_sentiment_results(test_sentiments)
#
#     # Analyze most common and longest words
#     most_common, longest = analyze_words(test_reviews)
#
#     #print("\n📌 30 most used words:\n", most_common)
#     #print("\n📌 30 longest words:\n", longest)
#
#     # Generate word clouds for most common and longest words
#     generate_wordcloud(most_common, "most_common_words.png")
#     generate_wordcloud(longest, "longest_words.png")