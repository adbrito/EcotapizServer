from django.db import models
from auto import utils

# Create your models here.
class Auto(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    glb         = models.CharField(max_length=500)
    imagen      = models.CharField(max_length=500)
    ranking     = models.PositiveIntegerField()

    def _str_(self):
        return self.nombre + '-' + self.descripcion + '-' + self.glb + '-' + self.imagen + '-' + self.ranking

    def crearAuto(self,nombre, descripcion, glb, imagen, ranking):
        auto = Auto()
        auto.nombre = nombre
        auto.descripcion = descripcion
        auto.glb = glb
        auto.imagen = imagen
        auto.ranking = ranking
        auto.save()
        return auto

    def actualizarAuto(self,id,nombre, descripcion, glb, imagen, ranking):
        autos = Auto.objects.filter(id=id)
        try:
            auto = autos[0]
            auto.nombre = nombre
            auto.descripcion = descripcion
            auto.glb = glb
            auto.imagen = imagen
            auto.ranking = ranking
            auto.save()
            return auto
        except Exception as e:
            return None

    def eliminarAuto(self,id):
        autos = Auto.objects.filter(id=id)
        try:
            auto = autos[0]
            auto.delete()
            return utils.message_1("Auto",id)
        except Exception as e:
            return ""
