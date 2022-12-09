from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    # image = models.ImageField(upload_to='images')
    date_of_birth = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.username

    def to_dict(self):
        return {
            'username': self.username,
            'date_of_birth': self.date_of_birth,
        }


# Auction model
class Item(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images')
    starting_price = models.FloatField()
    date_ends = models.DateTimeField(default=datetime.datetime.today)
    available = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'image': self.image.url if self.image else None,
            'starting_price': self.starting_price,
            'date_ends': self.date_ends,
            'available': self.available,
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
    
