from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>", views.MovieDetail.as_view(), name="detail"),
]
