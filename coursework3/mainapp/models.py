from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import json

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
            'profile': self.profile.to_dict() #if self.profile else None,

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

#Profile model 

class Profile(models.Model): 
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)
    #email = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images')
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.member_check})"


    def to_dict(self): #method is applied to all the profile objects
        return {
            'user': self.user.username,
            #'email': self.email,
            'DOB': self.user.date_of_birth,
            'image': self.image.url if self.image else None,
            'city': self.city,

        }

    @property
    def has_member(self):
        #True if this profile belongs to a Member
        return hasattr(self,self.user.username) and self.member is not None

    @property
    def member_check(self):
        #Either the username of the Member, or NONE'''
        return str(self, self.user.username) if self.has_member else 'NONE'


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
    
