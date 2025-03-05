import scraper as sc

if __name__ == '__main__':
    url = "https://www.csfd.cz/film/237486-pernikovy-tata/recenze/"
    reviews = sc.get_reviews(url)

    print("Stažené recenze:")
    for i, review in enumerate(reviews[:5], 1):
        print(f"{i}. {review}\n")
