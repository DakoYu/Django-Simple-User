from statistics import mode
from django.db import models

# Create your models here.
class FavModel(models.Model):
    '''Favourite Model'''
    car = models.CharField(max_length=255)
    food = models.CharField(max_length=255)
    star = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.car