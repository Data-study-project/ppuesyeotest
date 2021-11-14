from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Survey(models.Model):
    RANKS = [ (1, '10대'), (2, '20대'), (3, '30대'), (4, '40대'), (5, '50대'), (6, '60대'), (7, '70대'), (8, '80대 이상'), ]
    SEXS = [('F', '여자'), ('M', '남자')]
    INDOORS = [(1, '실내'), (0, '실외')]
    ALONES = [(1, '혼자'), (0, '같이')]
    LIGHTS = [(1, '가볍게'), (0, '제대로')]
    age = models.IntegerField(choices=RANKS)
    sex = models.CharField(choices=SEXS, max_length=10)   
    height = models.FloatField()
    weight = models.FloatField()
    walk_cnt = models.IntegerField()
    
    
    indoor = models.IntegerField(choices=INDOORS) 
    alone = models.IntegerField(choices=ALONES) 
    light = models.IntegerField(choices=LIGHTS)  


