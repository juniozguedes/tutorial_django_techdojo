from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=30)