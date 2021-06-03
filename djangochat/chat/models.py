from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=999)

class Message(models.Model):
    value = models.CharField(max_length=999)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=999)
    room = models.CharField(max_length=999)
