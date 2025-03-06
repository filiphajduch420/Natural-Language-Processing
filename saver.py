import os
import pandas as pd
from fpdf import FPDF

TRANSLATED_FILE = "reviews.txt"


# 📌 Funkce pro ukládání a načítání recenzí
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


# 📌 Funkce pro export do PDF
def export_to_pdf(sentiment_results, most_common_words, longest_words, pdf_filename="report.pdf"):
    """ Exportuje výsledky analýzy do PDF """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    # Titulek
    pdf.cell(200, 10, "Sentiment Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Počet recenzí
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Number of Reviews: {len(sentiment_results)}", ln=True)
    pdf.ln(5)

    # Výsledky sentimentu
    df_sentiment = pd.DataFrame(sentiment_results, columns=["Review", "Sentiment", "Score"])
    pdf.set_font("Arial", "", 10)
    for index, row in df_sentiment.iterrows():
        pdf.multi_cell(0, 7, f"{index + 1}. [{row['Sentiment']}] {row['Review'][:100]}... (Score: {row['Score']})")
    pdf.ln(5)

    # Nejčastější slova
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "30 Most Used Words:", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 7, ", ".join(most_common_words))
    pdf.ln(5)

    # Nejdelší slova
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "30 Longest Words:", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 7, ", ".join(longest_words))
    pdf.ln(5)

    # Uložení PDF
    pdf.output(pdf_filename)
    print(f"📄 Report uložen jako {pdf_filename}")