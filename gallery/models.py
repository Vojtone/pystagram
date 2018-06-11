from django.db import models
from datetime import datetime


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_photo = models.FileField()

    def __str__(self):
        return self.username


# 'Post' would probably be better name
class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField()
    description = models.CharField(max_length=10000)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username + ' #' + str(self.id)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.content
