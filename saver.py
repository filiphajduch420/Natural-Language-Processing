import os
from fpdf import FPDF

TRANSLATED_FILE = "reviews.txt"

def save_translated_reviews(translated_reviews):
    """ Saves translated reviews to a file """
    with open(TRANSLATED_FILE, "w", encoding="utf-8") as file:
        for review in translated_reviews:
            file.write(review + "\n")

def load_translated_reviews():
    """ Loads translated reviews from a file if it exists """
    if os.path.exists(TRANSLATED_FILE):
        with open(TRANSLATED_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return None

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # ✅ Přidání fontu při inicializaci třídy
        self.add_font('FreeSans', '', 'fonts/FreeSans.ttf', uni=True)
        self.add_font('FreeSans', 'B', 'fonts/FreeSansBold.ttf', uni=True)

    def header(self):
        self.set_font("FreeSans", "B", 16)  # ✅ Font je nyní zaregistrovaný!
        self.cell(200, 10, "Sentiment Analysis Report", ln=True, align="C")
        self.ln(10)

    def add_table(self, data, col_widths):
        """ Adds a table to the PDF """
        self.set_font("FreeSans", "", 10)
        for row in data:
            for i, item in enumerate(row):
                col_width = col_widths[i % len(col_widths)]
                self.cell(col_width, 10, str(item), border=1, align="L")
            self.ln()

def export_to_pdf(url, sentiment_results, most_common_words, longest_words, pdf_filename="report/sentiment_report.pdf"):
    """ Exports the sentiment analysis results to a PDF """
    print("Exporting results to PDF...")
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # 📌 Add URL
    pdf.set_font("FreeSans", "", 12)
    pdf.cell(200, 10, f"URL: {url}", ln=True, align="L")
    pdf.ln(5)

    # 📊 Count the number of reviews by sentiment
    total_reviews = len(sentiment_results)
    sentiment_counts = {
        "Positive": sum(1 for _, sentiment, _ in sentiment_results if sentiment == "positive"),
        "Neutral": sum(1 for _, sentiment, _ in sentiment_results if sentiment == "neutral"),
        "Negative": sum(1 for _, sentiment, _ in sentiment_results if sentiment == "negative"),
    }

    # 📌 Create the main table
    table_data = [
        ["Total Reviews", total_reviews],
        ["Positive Reviews", sentiment_counts["Positive"]],
        ["Neutral Reviews", sentiment_counts["Neutral"]],
        ["Negative Reviews", sentiment_counts["Negative"]],
    ]
    pdf.add_table(table_data, [100, 90])

    # 📌 Add most common words in a single cell
    pdf.ln(10)
    pdf.set_font("FreeSans", "B", 12)
    pdf.cell(200, 10, "30 Most Used Words", ln=True, align="L")
    pdf.ln(5)

    formatted_words = ", ".join(most_common_words)
    pdf.set_font("FreeSans", "", 10)
    pdf.multi_cell(0, 7, formatted_words, border=1, align="L")

    # 📌 Add word cloud image for most common words
    pdf.ln(10)
    pdf.image("img/most_common_words.png", x=None, y=None, w=150)

    # 📌 Add longest words in a single cell
    pdf.ln(10)
    pdf.set_font("FreeSans", "B", 12)
    pdf.cell(200, 10, "30 Longest Words", ln=True, align="L")
    pdf.ln(5)

    formatted_longest_words = ", ".join(longest_words)
    pdf.set_font("FreeSans", "", 10)
    pdf.multi_cell(0, 7, formatted_longest_words, border=1, align="L")

    # 📌 Add word cloud image for longest words
    pdf.ln(10)
    pdf.image("img/longest_words.png", x=None, y=None, w=150)

    # 📌 Save the PDF
    pdf.output(pdf_filename)
    print(f"Report saved as {pdf_filename}")