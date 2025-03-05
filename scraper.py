import requests
from bs4 import BeautifulSoup

def get_reviews(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Přidáváme User-Agent, aby se zabránilo blokování
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []
    for review in soup.find_all("span", class_="comment", attrs={"data-film-comment-content": True}):
        reviews.append(review.text.strip())

    return reviews
