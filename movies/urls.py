from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("nv_code=<int:nv_code>", views.MovieDetail, name="detail"),
]
