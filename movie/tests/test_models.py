from unittest import TestCase

from movie.models import Genre


class GenreTest(TestCase):

    def setUp(self):
        print("Setup objects for genre model")
        self.genre = Genre.objects.create(name='Comedy')
        self.another_genre = Genre.objects.create(name='Crime')

    def tearDown(self):
        print("Remove objects")
        self.genre.delete()
        self.another_genre.delete()

    def test_genre_instance(self):
        self.assertTrue(isinstance(self.genre, Genre))
