import requests
from bs4 import BeautifulSoup

def get_reviews(url):
    print("Scraping reviews...")
    headers = {"User-Agent": "Mozilla/5.0"}  # Adding User-Agent to avoid blocking
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []
    for review in soup.find_all("span", class_="comment", attrs={"data-film-comment-content": True}):
        reviews.append(review.text.strip())

    return reviews

#testing purposes
# if __name__ == "__main__":
#     url = "https://www.csfd.cz/film/237486-pernikovy-tata/recenze/"
#     reviews = get_reviews(url)
#     for i, review in enumerate(reviews, 1):
#         print(f"{i}. {review}")