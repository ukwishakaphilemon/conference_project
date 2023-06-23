
from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=200)
    dates = models.DateField()
    location = models.CharField(max_lenght=100)
    topics = models.CharField(max_length=500)
    description = models.TextField()




    def __str__(self):
        return self.name




