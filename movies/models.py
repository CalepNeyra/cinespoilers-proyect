from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    age_rating = models.CharField(max_length=10, blank=True)
    release_date = models.DateField()
    is_showing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title