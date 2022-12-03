from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username