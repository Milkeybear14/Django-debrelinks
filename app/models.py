from django.db import models

# Create your models here.
class results(models.Model):
    image = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length = 20)
    link= models.URLField(max_length = 50)
    paragraph = models.TextField()
