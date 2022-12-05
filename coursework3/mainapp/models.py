from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    test = models.CharField(max_length=50, unique=True, default='rwf')
    image = models.ImageField(upload_to='images')
    date_of_birth = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.username

    def to_dict(self):
        return {
            'username': self.username,
            'image': self.image.url if self.image else None,
            'date_of_birth': self.date_of_birth,
        }


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
    
