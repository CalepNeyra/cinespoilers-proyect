from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "duration_minutes",
        "age_rating",
        "release_date",
        "is_showing",
    )
    list_filter = ("is_showing", "age_rating", "release_date")
    search_fields = ("title",)