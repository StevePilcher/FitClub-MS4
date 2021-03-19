from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    originator = models.ForeignKey(User, related_name='topics')

class Board(model.Models):