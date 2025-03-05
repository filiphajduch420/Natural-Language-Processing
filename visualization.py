import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd


def generate_wordcloud(reviews, filename="wordcloud.png"):
    """ Vytvoří a uloží wordcloud ze seznamu recenzí """
    text = " ".join(reviews)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(filename)
    plt.show()


def display_sentiment_results(sentiment_results):
    """ Zobrazí tabulku sentimentu recenzí v konzoli """
    df_sentiment = pd.DataFrame(sentiment_results, columns=["Review", "Sentiment", "Score"])
    df_sentiment["Score"] = df_sentiment["Score"].round(2)

    print("\n📊 Sentiment Analysis Table:\n")

    try:
        from tabulate import tabulate
        print(tabulate(df_sentiment, headers="keys", tablefmt="github"))
    except ImportError:
        print(df_sentiment.to_string(index=False))
