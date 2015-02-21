from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
