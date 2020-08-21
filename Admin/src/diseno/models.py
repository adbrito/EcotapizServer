from django.db import models

# Create your models here.
class Diseno(models.Model):
    nombre        = models.CharField(max_length=30)
    descripcion   = models.TextField(blank=True, null=True)
    numMateriales = models.IntegerField()
    imagen        = models.CharField(max_length=500)
    ranking       = models.PositiveIntegerField()
    precio        = models.DecimalField(max_digits=10, decimal_places=2)
    gld           = models.CharField(max_length=500)
    campo         = models.TextField()
