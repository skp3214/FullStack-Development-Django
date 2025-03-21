from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.title