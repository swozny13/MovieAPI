from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    rate = models.CharField(max_length=5, null=True, blank=True)
    movie_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.rate} - {self.movie_id}"


class Tag(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    ratings = models.ManyToManyField(Rating, blank=True)
    year = models.CharField(max_length=5, null=True, blank=True)
    link = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.title
