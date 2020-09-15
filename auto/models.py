from django.db import models

# Create your models here.
class Auto(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    glb         = models.CharField(max_length=500)
    imagen      = models.CharField(max_length=500)
    ranking     = models.PositiveIntegerField()
