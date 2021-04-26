from django.db import models
from django.contrib.auth.models import User
class task(models.Model):
    
    coloumn_id=models.IntegerField()
    name=models.CharField(max_length=100)
    Iamge=models.URLField(max_length=5000)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
