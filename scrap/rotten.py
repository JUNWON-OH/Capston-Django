import requests
from bs4 import BeautifulSoup


def rotten(movie):
    rotten = []
    try:
        movie_english = str(movie["en_search"])
        movie_search = (
            movie_english.replace(" ", "_").replace(":", "").replace("_-_", "_").lower()
        )
        URL = f"https://www.rottentomatoes.com/m/{movie_search}"
        result = requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")
        pre_score = (
            soup.find("div", {"id": "main_container"})
            .find("div", {"id": "topSection"})
            .find("section", {"class": "mop-ratings-wrap__info"})
        )
        try:
            score = (
                pre_score.find("a", {"href": "#contentReviews"})
                .find("span", {"class": "mop-ratings-wrap__percentage"})
                .get_text(strip=True)
            )
            rotten.append({"link": URL, "Name": movie_search, "rotten": score})
        except:
            print("except")
            score = "0%"
            rotten.append({"link": URL, "Name": movie_search, "rotten": score})
    except:
        print("except")
        try:
            movie_search = str(movie["en_name"])
            URL = f"https://www.rottentomatoes.com/m/{movie_search}"
            result = requests.get(URL)
            soup = BeautifulSoup(result.text, "html.parser")
            pre_score = (
                soup.find("div", {"id": "main_container"})
                .find("div", {"id": "topSection"})
                .find("section", {"class": "mop-ratings-wrap__info"})
            )
            try:
                score = (
                    pre_score.find("a", {"href": "#contentReviews"})
                    .find("span", {"class": "mop-ratings-wrap__percentage"})
                    .get_text(strip=True)
                )
                rotten.append({"link": URL, "Name": movie_search, "rotten": score})
            except:
                print("except")
                score = "0%"
                rotten.append({"link": URL, "Name": movie_search, "rotten": score})
        except:
            print("except")
            score = "None"
            rotten.append({"link": URL, "Name": movie_search, "rotten": score})

    return rotten
