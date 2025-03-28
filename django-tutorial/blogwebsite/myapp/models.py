from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.title