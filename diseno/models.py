from django.db import models

# Create your models here.
class Diseno(models.Model):
    nombre        = models.CharField(max_length=30)
    descripcion   = models.TextField(blank=True, null=True)
    imagen        = models.CharField(max_length=500)
    metros        = models.DecimalField(max_digits=10, decimal_places=2)
    ranking       = models.PositiveIntegerField()
    glb           = models.CharField(max_length=500)
