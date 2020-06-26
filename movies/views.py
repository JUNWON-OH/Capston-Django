from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms
from scrap.naver import pre_link, detail
from scrap.rotten import rotten
from scrap.imdb import imdb

# Create your views here.


class HomeView(ListView):
    model = models.Movie
    context_object_name = "movies"


class SearchView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        kr_name = request.GET.get("movie")
        nv_result = pre_link(kr_name)
        return render(
            request,
            "movies/search.html",
            {"nv_result": nv_result, "kr_name": kr_name, "form": form},
        )


def MovieDetail(request, nv_code):
    user = request.user
    movie_detail = detail(nv_code)
    rotten_score = rotten(movie_detail)[0]
    imdb_score = imdb(movie_detail)[0]
    try:
        movie_exist = models.Movie.objects.get(nv_code=nv_code)
        movie_exist.rotten = rotten_score["rotten"]
        movie_exist.imdb = imdb_score["score"]
        movie_exist.users.add(user)
        movie_exist.save()
    except models.Movie.DoesNotExist:
        movie = models.Movie.objects.create(
            nv_code=nv_code,
            poster=movie_detail["poster"],
            kr_name=movie_detail["kr_name"],
            en_name=movie_detail["en_name"],
            director=movie_detail["director"],
            actor=movie_detail["actor"],
            year=movie_detail["year"],
            naver=movie_detail["naver"],
            naver_link=movie_detail["link"],
            rotten=rotten_score["rotten"],
            rotten_link=rotten_score["link"],
            imdb=imdb_score["score"],
            imdb_link=imdb_score["link"],
            movie_detail=movie_detail["story_detail"],
        )
        movie.users.add(user)
        movie.save()
    return render(
        request,
        "movies/movie_detail.html",
        {"detail": movie_detail, "rotten": rotten_score, "imdb": imdb_score},
    )
