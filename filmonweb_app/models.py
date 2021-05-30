from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Person(models.Model):
    """
    Information about persons, actors, directors, etc.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    """
    Genre of movies
    """
    name = models.CharField(max_length=255)


class Movie(models.Model):
    """
    Detail of movies
    """
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(1.0),
                                           MaxValueValidator(10.0)])
    director = models.ForeignKey(Person, on_delete=models.SET_NULL,
                                 related_name='director_rel', null=True)
    screenplay = models.ForeignKey(Person, on_delete=models.SET_NULL,
                                   related_name='screenplay_rel', null=True)
    genre = models.ManyToManyField(Genre)
    starring = models.ManyToManyField(Person, related_name='PersonMovie',
                                      through='PersonMovie')


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=255)
