from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    # image = models.ImageField(upload_to='images')
    date_of_birth = models.DateField(default=datetime.date.today)


    questionanswers = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='QuestionAnswer',
        related_name='related_to'
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def to_dict(self):
        return {
            'username': self.username,
            'date_of_birth': self.date_of_birth,
            'questionanswers': [questionanswer.to_dict() for questionanswer in self.questionanswers]
        }

    @property
    def questionanswers(self):
        '''Q&As sent and received by this user'''

        return (self.sent.all() | self.received.all()).order_by("-time")

    def questionanswers_with(self, view_user):
        '''Messages visible between two users'''

        # public messages that 'view_user' has received
        m1 = QuestionAnswer.objects.filter(recip=view_user)
        # public messages that 'view_user' has sent
        m2 = QuestionAnswer.objects.filter(sender=view_user)
        # messages 'user' sent 'view_user'
        # m3 = QuestionAnswer.objects.filter(sender=self, recip=view_user)
        # # messages 'view_user' sent 'user'
        # m4 = QuestionAnswer.objects.filter(sender=view_user, recip=self)
        # union of the four query sets
        return m1.union(m2).order_by('-time')


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
    


class QuestionAnswer(models.Model):
    '''
    The Message models is the 'through' model for
    the 'message' ManyToMany relationship between Members
    '''

    sender = models.ForeignKey(
        to=User,
        related_name='sent',
        on_delete=models.CASCADE
    )
    recip = models.ForeignKey(
        to=User,
        related_name='received',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=4096)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"From {self.sender} to {self.recip}"

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender.username,
            'recip': self.recip.username,
            'text': self.text,
            'time': self.time.strftime("%Y-%d-%mT%H:%M"),
        }