import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import string
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords


def generate_wordcloud(words, filename="wordcloud.png"):
    """ Vytvoří wordcloud z daného textu nebo seznamu slov """
    text = " ".join(words)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(filename)
    plt.show()


def display_sentiment_results(sentiment_results):
    """ Zobrazí tabulku sentimentu recenzí """
    df_sentiment = pd.DataFrame(sentiment_results, columns=["Review", "Sentiment", "Score"])
    df_sentiment["Score"] = df_sentiment["Score"].round(2)

    print("\n📊 Sentiment Analysis Table:\n")

    try:
        from tabulate import tabulate
        print(tabulate(df_sentiment, headers="keys", tablefmt="github"))
    except ImportError:
        print(df_sentiment.to_string(index=False))


def analyze_words(reviews):
    """ Analyzuje slova v recenzích – nejčastější a nejdelší slova """
    text = " ".join(reviews).lower()
    words = [word.strip(string.punctuation) for word in text.split()]

    # Odstranění stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word and word not in stop_words]

    # 30 nejčastějších slov
    most_common_words = [word for word, _ in Counter(words).most_common(30)]

    # 30 nejdelších slov
    longest_words = sorted(set(words), key=len, reverse=True)[:30]

    return most_common_words, longest_words


if __name__ == "__main__":
    test_reviews = [
        "This movie is absolutely fantastic! I loved every second of it.",
        "It was an average experience. Nothing special, nothing terrible.",
        "I really hated this movie. It was a complete waste of time."
    ]

    # Simulujeme analýzu sentimentu
    test_sentiments = [
        (test_reviews[0], "positive", 0.85),
        (test_reviews[1], "neutral", 0.00),
        (test_reviews[2], "negative", -0.75)
    ]

    # Generování wordcloudu pro recenze
    generate_wordcloud(test_reviews, "test_wordcloud.png")

    # Zobrazení tabulky sentimentu
    display_sentiment_results(test_sentiments)

    # Analýza nejčastějších a nejdelších slov
    most_common, longest = analyze_words(test_reviews)

    print("\n📌 30 nejpoužívanějších slov:\n", most_common)
    print("\n📌 30 nejdelších slov:\n", longest)

    # Generování wordcloudů pro nejčastější a nejdelší slova
    generate_wordcloud(most_common, "most_common_words.png")
    generate_wordcloud(longest, "longest_words.png")