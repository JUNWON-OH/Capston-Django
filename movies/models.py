from django.db import models
from django.urls import reverse
from core import models as core_models


class Movie(core_models.TimeStampedModel):

    """ Movie Model Definition """

    nv_code = models.CharField(max_length=50, blank=True)
    poster = models.ImageField(blank=True)
    kr_name = models.CharField(max_length=50, blank=True)
    en_name = models.CharField(max_length=50, blank=True)
    en_search = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=50, blank=True)
    naver = models.IntegerField()
    rotten = models.IntegerField()
    imbd = models.IntegerField()
    users = models.ManyToManyField("users.User", related_name="movies", blank=True)

    def __str__(self):
        return self.en_name
