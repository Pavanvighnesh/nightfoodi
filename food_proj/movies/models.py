from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=200,default='action')
   


    def __str__(self):
        return self.name