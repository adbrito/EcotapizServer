from django.db import models

# Create your models here.
class Material(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen      = models.CharField(max_length=500)
    ranking     = models.PositiveIntegerField()
    precio      = models.DecimalField(max_digits=10, decimal_places=2)
