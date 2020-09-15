from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre      = models.CharField(max_length=30)
    apellido    = models.CharField(max_length=30)
    correo      = models.CharField(max_length=30)
    contrasena  = models.CharField(max_length=500)
 
