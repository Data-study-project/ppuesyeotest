from django.db import models

# Create your models here.
class Health(models.Model):
    name_animal = models.CharField(max_length=50)
    name_exercise = models.CharField(max_length=50)
    content = models.CharField(max_length=200, default='hello')

    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name_animal