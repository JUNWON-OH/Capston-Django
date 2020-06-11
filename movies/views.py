from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms
from scrap.naver import pre_link

# Create your views here.


class HomeView(ListView):
    model = models.Movie
    context_object_name = "movies"


class SearchView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        kr_name = request.GET.get("kr_name")
        nv_result = pre_link(kr_name)
        return render(
            request,
            "movies/search.html",
            {"nv_result": nv_result, "kr_name": kr_name, "form": form},
        )
        """
        if kr_name:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                kr_name = form.cleaned_data.get("kr_name")
                filter_args = {}
                if kr_name is not None:
                    filter_args["kr_name__startswith"] = kr_name
                qs = models.Movie.objects.filter(**filter_args)
                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                movies = paginator.get_page(page)
                get_copy = request.GET.copy()
                address = get_copy.pop("page", True) and get_copy.urlencode()
                return render(
                    request,
                    "movies/search.html",
                    {"form": form, "movies": movies, "address": address},
                )
        else:
            form = forms.SearchForm()
        return render(request, "movies/search.html", {"form": form})
        """


class MovieDetail(DetailView):

    model = models.Movie
