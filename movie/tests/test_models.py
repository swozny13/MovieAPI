import datetime
from unittest import TestCase

from django.contrib.auth.models import User

from movie.models import Genre, Rating, Tag, Movie


class GenreTest(TestCase):

    def setUp(self):
        print("Setup objects for genre model")
        self.genre = Genre.objects.create(name='Comedy')
        self.another_genre = Genre.objects.create(name='Crime')

    def tearDown(self):
        print("Remove genres objects")
        self.genre.delete()
        self.another_genre.delete()

    def test_genre_instance(self):
        self.assertTrue(isinstance(self.genre, Genre))


class RatingTest(TestCase):

    def setUp(self):
        print("Setup objects for rating model")
        self.user = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        self.date = datetime.datetime.now()
        self.rating = Rating.objects.create(
            user=self.user,
            rate='5.0',
            movie_id='1',
            date=self.date
        )

    def tearDown(self):
        print("Remove ratings objects")
        self.rating.delete()
        self.user.delete()

    def test_rating_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))


class TagTest(TestCase):

    def setUp(self):
        print("Setup objects for tag model")
        self.user = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        self.tag = Tag.objects.create(
            user=self.user,
            name='great book'
        )

    def tearDown(self):
        print("Remove tag objects")
        self.tag.delete()
        self.user.delete()

    def test_tag_instance(self):
        self.assertTrue(isinstance(self.tag, Tag))


class MovieTest(TestCase):

    def setUp(self):
        print("Setup objects for tag model")
        self.genre = Genre.objects.create(name='Comedy')
        self.another_genre = Genre.objects.create(name='Crime')
        self.user = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        self.date = datetime.datetime.now()
        self.rating = Rating.objects.create(
            user=self.user,
            rate='5.0',
            movie_id='1',
            date=self.date
        )
        self.tag = Tag.objects.create(
            user=self.user,
            name='great movie'
        )
        self.movie = Movie.objects.create(
            title='King Lion',
            year='1999',
            link='http://imdb.com/tt/12312312'
        )
        self.movie.genres.add(self.genre)
        self.movie.genres.add(self.another_genre)
        self.movie.ratings.add(self.rating)

    def tearDown(self):
        print("Remove movie objects")
        self.movie.delete()
        self.user.delete()
        self.genre.delete()
        self.another_genre.delete()

    def test_movie_instance(self):
        self.assertTrue(isinstance(self.movie, Movie))
