from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.TextField()
    gene = models.TextField()

class User_two(models.Model):
    username = models.CharField(max_length=60, primary_key=True)
    password = models.CharField(max_length=60)