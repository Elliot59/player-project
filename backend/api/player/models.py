from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=500, default=None)
    confirm_password = models.CharField(max_length=500, default=None)
    is_admin = models.BooleanField(default=False)
    is_captain = models.BooleanField(default=False)
    is_player = models.BooleanField(default=True)
    is_guest = models.BooleanField(default=False)

    def __str__(self):
        return self.name
