from django.db import models
from django.urls import reverse
from core import models as core_models


class Movie(core_models.TimeStampedModel):

    """ Movie Model Definition """

    nv_code = models.CharField(max_length=100, blank=True)
    poster = models.CharField(max_length=100, blank=True)
    director = models.CharField(max_length=100, blank=True)
    actor = models.CharField(max_length=100, blank=True)
    kr_name = models.CharField(max_length=100, blank=True)
    en_name = models.CharField(max_length=100, blank=True)
    en_search = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=100, blank=True)
    naver = models.CharField(max_length=100, blank=True)
    naver_link = models.CharField(max_length=100, blank=True)
    rotten = models.CharField(max_length=100, blank=True)
    rotten_link = models.CharField(max_length=100, blank=True)
    imdb = models.CharField(max_length=100, blank=True)
    imdb_link = models.CharField(max_length=100, blank=True)
    movie_detail = models.TextField(blank=True)
    users = models.ManyToManyField("users.User", related_name="movies", blank=True)

    def __str__(self):
        return self.en_name
