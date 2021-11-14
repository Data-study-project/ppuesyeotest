from django.db import models

# Create your models here.

class BMI(models.Model):
    sex = models.CharField(max_length=10)
    body_mass = models.FloatField()
    age = models.IntegerField()


class Walk(models.Model):
    sex = models.CharField(max_length=10)
    walk_cnt = models.IntegerField()
    age = models.IntegerField()


class Animal(models.Model):
    name = models.CharField(max_length=100)
    content1 = models.CharField(max_length=100)
    content2 = models.CharField(max_length=100)
    animal_num = models.IntegerField()