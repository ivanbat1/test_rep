from django.db import models

# Create your models here.
class UserAPI(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    img = models.ImageField(upload_to='image/', default='image/images.jpg')
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)