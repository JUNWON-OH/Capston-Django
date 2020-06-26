import requests
from bs4 import BeautifulSoup


def pre_link(movie):
    link_list = []
    try:
        link = f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=movie&ie=utf8"
        result = requests.get(link)
        soup = BeautifulSoup(result.text, "html.parser")
        movie_soups = (
            soup.find("div", {"id": "content"})
            .find("div", {"id": "old_content"})
            .find("ul", {"class": "search_list_1"})
            .find_all("li")
        )
        for soup in movie_soups:
            fake_link = soup.find("a")["href"]
            nv_code = fake_link.replace("/movie/bi/mi/basic.nhn?code=", "")
            movie_link = f"https://movie.naver.com{fake_link}"
            img_link = soup.find("img")["src"]
            movie_name = soup.find("dl").find("dt").find("a").get_text("", strip=True)

            movie_infos = soup.find("dd", {"class": "etc"}).get_text("", strip=True)
            link_list.append(
                {
                    "nv_code": int(nv_code),
                    "movie_link": movie_link,
                    "img_link": img_link,
                    "movie_name": movie_name,
                    "movie_infos": movie_infos,
                }
            )
        return link_list

    except:
        link_list.append({"Name": movie, "Link": "Error"})
        return link_list


def detail(code):
    movie_detail = {}
    link = f"https://movie.naver.com/movie/bi/mi/basic.nhn?code={code}"
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    img_link = (
        f"https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={code}"
    )
    img_result = requests.get(img_link)
    img_soup = BeautifulSoup(img_result.text, "html.parser")
    poster = img_soup.find("img")["src"]
    movie_info = (
        soup.find("div", {"id": "container"})
        .find("div", {"id": "content"})
        .find("div", {"class": "mv_info_area"})
    )
    people = movie_info.find("dl", {"class": "info_spec"}).find_all("dd")
    director = people[1].get_text("", strip=True)
    actor = people[2].get_text("", strip=True).replace("더보기", "")
    kr_name = movie_info.find("h3", {"class": "h_movie"}).get_text("", strip=True)
    english = movie_info.find("strong", {"class": "h_movie2"}).get_text("", strip=True)
    english_list = str(english).split(",")
    en_name = english_list[-2].rstrip().lstrip()
    year = english_list[-1].lstrip().rstrip()
    en_search = en_name + "_" + year
    naver = (
        soup.find("div", {"id": "content"})
        .find("div", {"class": "section_group"})
        .find("div", {"class": "score_area"})
        .find("div", {"class": "netizen_score"})
        .find("div", {"class": "star_score"})
        .find("em")
        .get_text("", strip=True)
    )

    story_detail = (
        soup.find("div", {"id": "content"})
        .find("div", {"class": "section_group"})
        .find("div", {"class": "story_area"})
        .find("p")
        .get_text("", strip=True)
    )
    movie_detail["link"] = link
    movie_detail["director"] = director
    movie_detail["actor"] = actor
    movie_detail["poster"] = poster
    movie_detail["kr_name"] = kr_name
    movie_detail["English"] = english
    movie_detail["en_name"] = en_name
    movie_detail["en_search"] = en_search
    movie_detail["year"] = year
    movie_detail["naver"] = naver
    movie_detail["story_detail"] = story_detail
    return movie_detail
