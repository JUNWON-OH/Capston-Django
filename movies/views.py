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
    movie_detail = detail(nv_code)
    rotten_score = rotten(movie_detail)[0]
    imdb_score = imdb(movie_detail)[0]
    return render(
        request,
        "movies/movie_detail.html",
        {"detail": movie_detail, "rotten": rotten_score, "imdb": imdb_score},
    )
