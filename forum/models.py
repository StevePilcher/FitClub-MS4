from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=80)
    user_post = models.CharField(max_length=300)
    date_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.topic)

class Conversation(models.Model):
    forum = models.ForeignKey(Forum,blank=True,on_delete=models.CASCADE)
    chat = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)