from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    sports = models.CharField(max_length=200)
    addr = models.CharField(max_length=300)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    tel = models.CharField(max_length=200, blank=True)
