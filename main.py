import scraper as sc
import translator as tr
import sentiment_analyzer as sa
import os

# Konstanty pro výběr režimu (0 = použít soubor, 1 = přeložit API)
USE_API = 0
TRANSLATED_FILE = "reviews.txt"


def save_translated_reviews(translated_reviews):
    """ Uloží přeložené recenze do souboru """
    with open(TRANSLATED_FILE, "w", encoding="utf-8") as file:
        for review in translated_reviews:
            file.write(review + "\n")


def load_translated_reviews():
    """ Načte přeložené recenze ze souboru, pokud existuje """
    if os.path.exists(TRANSLATED_FILE):
        with open(TRANSLATED_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return None


if __name__ == '__main__':
    url = "https://www.csfd.cz/film/237486-pernikovy-tata/recenze/"

    if USE_API:  # Pokud je API zapnuté, přeložíme nové recenze
        print("📌 Překládám recenze (API)...")
        reviews = sc.get_reviews(url)

        if reviews:
            translated_reviews = [tr.translate_text(review) for review in reviews[:5]]
            save_translated_reviews(translated_reviews)  # Uložíme pro další použití
        else:
            print("❌ Žádné recenze nebyly nalezeny!")
            exit()

    else:  # Pokud API není zapnuté, použijeme uložené recenze
        print("📌 Používám přeložené recenze ze souboru...")
        translated_reviews = load_translated_reviews()

        if not translated_reviews:
            print("❌ Soubor s přeloženými recenzemi neexistuje! Změň USE_API na 1 a spusť znovu.")
            exit()

    print("\n📌 Stažené, přeložené a analyzované recenze:\n")
    for i, translated_review in enumerate(translated_reviews, 1):
        sentiment, score = sa.analyze_sentiment(translated_review)

        print(f"{i}. EN: {translated_review}")
        print(f"   🔹 Sentiment: {sentiment} (score: {score})\n")