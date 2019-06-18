from django.contrib import admin

from movie.models import Movie, Tag, Rating, Genre

admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Movie)
