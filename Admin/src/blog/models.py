from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo      = models.CharField(max_length=30)
    imagen      = models.CharField(max_length=500)
    autor       = models.CharField(max_length=30)
    contenido   = models.TextField()
