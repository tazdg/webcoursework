from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username


class Recipe(models.Model):
    name = models.CharField(max_length=350)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'popular': self.popular,
        }
    