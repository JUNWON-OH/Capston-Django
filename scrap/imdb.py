import requests
from bs4 import BeautifulSoup


def imdb(movie):
    imbd = []
    try:
        movie_english = movie["en_search"]
        movie_search = (
            movie_english.replace(" ", "_")
            .replace(":", "")
            .replace("_-_", "_")
            .replace("_", "+")
        )
        movie_url = f"https://www.boxofficemojo.com/search/?q={movie_search}"
        result_mojo = requests.get(movie_url)
        soup_mojo = BeautifulSoup(result_mojo.text, "html.parser")
        link = (
            soup_mojo.find("div", {"class": "a-fixed-left-grid"})
            .find("div", {"class": "a-col-left"})
            .find("a")["href"]
        )
        url = f"https://www.imdb.com{link}"
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        score = (
            soup.find("div", {"id": "title-overview-widget"})
            .find("div", {"class": "title_block"})
            .find("div", {"class": "ratingValue"})
            .find("strong")
            .find("span", {"itemprop": "ratingValue"})
            .get_text(strip=True)
        )
        imbd.append({"link": url, "Name": movie_english, "score": score})
    except:
        imbd.append({"link": url, "Name": movie["English"], "score": "Error"})
    return imbd
