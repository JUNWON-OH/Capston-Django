from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """ Movie Amin Definition """

    fieldsets = (
        (
            "Info",
            {
                "fields": (
                    "nv_code",
                    "poster",
                    "director",
                    "actor",
                    "kr_name",
                    "en_name",
                    "en_search",
                    "year",
                    "naver",
                    "rotten",
                    "imdb",
                    "users",
                    "movie_detail",
                )
            },
        ),
    )

    list_display = (
        "kr_name",
        "year",
        "actor",
        "naver",
        "rotten",
        "imdb",
        "count_users",
    )

    list_filter = ("users",)

    search_fields = ("kr_name", "en_name", "users__username")

    filter_horizontal = ("users",)

    def count_users(self, obj):
        for a in obj.users.all():
            print(a)
        print(obj.users.all())
        return obj.users.count()
