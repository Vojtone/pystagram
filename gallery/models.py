from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.username


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username + ' #' + str(self.id)
