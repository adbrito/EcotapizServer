from django.db import models

# Create your models here.
class Material(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    imagen      = models.CharField(max_length=500)
    ranking     = models.PositiveIntegerField()
    precio      = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
 
