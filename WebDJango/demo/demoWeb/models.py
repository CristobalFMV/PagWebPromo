from django.db import models

# Create your models here.
class foto(models.Model):
    nombre=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='images/')