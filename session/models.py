from django.db import models

# Create your models here.
class User_Session(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)