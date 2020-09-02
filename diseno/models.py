from django.db import models
from auto import utils

# Create your models here.
class Diseno(models.Model):
    id            = models.AutoField(primary_key=True)
    nombre        = models.CharField(max_length=30)
    descripcion   = models.TextField(blank=True, null=True)
    imagen        = models.CharField(max_length=500)
    metros        = models.DecimalField(max_digits=10, decimal_places=2)
    ranking       = models.PositiveIntegerField()
    glb           = models.CharField(max_length=500)

    def to_string(self):
        return str(self.nombre) + '-' + str(self.descripcion) + '-' + str(self.imagen) + '-' + str(self.metros) + '-' + str(self.ranking) + '-' + str(self.glb) 

    def crearDiseno(self,nombre, descripcion, imagen, metros, ranking, glb):
        diseno = Diseno()
        diseno.nombre = nombre
        diseno.descripcion = descripcion
        diseno.imagen = imagen
        diseno.metros = metros
        diseno.ranking = ranking
        diseno.glb = glb
        diseno.save()
        return diseno

    def actualizarDiseno(self,id,nombre, descripcion, imagen, metros, ranking, glb):
        disenos = Diseno.objects.filter(id=id)
        try:
            diseno = disenos[0]
            diseno.nombre = nombre
            diseno.descripcion = descripcion
            diseno.imagen = imagen
            diseno.metros = metros
            diseno.ranking = ranking
            diseno.glb = glb
            diseno.save()
            return diseno
        except Exception as e:
            return None

    def eliminarDiseno(self,id):
        disenos = Diseno.objects.filter(id=id)
        try:
            diseno = disenos[0]
            diseno.delete()
            return utils.message_1("Diseno",id)
        except Exception as e:
            return ""