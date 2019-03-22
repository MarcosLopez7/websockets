from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30)
    word = models.CharField(max_length=30)