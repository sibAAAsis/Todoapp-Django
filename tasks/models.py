#this is the models of the app to store data in database
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(default='') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

def __str__(self):
        return self.title