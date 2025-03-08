import scraper as sc
import translator as tr
import sentiment_analyzer as sa
import visualization as vz
import saver as sv
from saver import export_to_pdf

# Constants for mode selection (0 = use file, 1 = translate API)
USE_API = 1

if __name__ == '__main__':
    url = "https://www.csfd.cz/film/29952-plump-fiction/recenze/"

    if USE_API:  # If API is enabled, translate new reviews
        print("Translating reviews (API)...")
        reviews = sc.get_reviews(url)

        if reviews:
            translated_reviews = [tr.translate_text(review) for review in reviews]
            sv.save_translated_reviews(translated_reviews)  # Save for future use
        else:
            print("No reviews found!")
            exit()

    else:  # If API is not enabled, use saved reviews
        print("Using translated reviews from file...")
        translated_reviews = sv.load_translated_reviews()

        if not translated_reviews:
            print("File with translated reviews does not exist! Change USE_API to 1 and run again.")
            exit()

    #print("\nDownloaded, translated, and analyzed reviews:\n")
    sentiment_results = []
    for i, translated_review in enumerate(translated_reviews, 1):
        sentiment, score = sa.analyze_sentiment(translated_review)
        sentiment_results.append((translated_review, sentiment, score))

        #print(f"{i}. EN: {translated_review}")
        #print(f"   🔹 Sentiment: {sentiment} (score: {score})\n")

    # 📊 Visual outputs
    vz.generate_wordcloud(translated_reviews, "img/reviews_wordcloud.png")

    # 🔍 Word analysis (most common and longest)
    most_common, longest = vz.analyze_words(translated_reviews)

    #print("\n30 most used words:\n", most_common)
    #print("\n30 longest words:\n", longest)

    # Generate word clouds for most used and longest words
    vz.generate_wordcloud(most_common, "img/most_common_words.png")
    vz.generate_wordcloud(longest, "img/longest_words.png")

    # 📄 Export to PDF
    export_to_pdf(url, sentiment_results, most_common, longest, pdf_filename="report/sentiment_report_second.pdf")