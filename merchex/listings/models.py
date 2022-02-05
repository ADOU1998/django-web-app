from pyexpat import model
from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.()
class Band(models.Model):

    # classe de la liste de choix
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_HOP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5) # liste de choix
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    offials_homepage = models.fields.URLField(null=True, blank=True)

# modele=Table listing
class Listing(models.Model):

    # classe de la liste de choix type
    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MIS'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1100)
    sold = models.fields.IntegerField(max_length=10)
    type = models.fields.CharField(choices=Type.choices, max_length=15)
