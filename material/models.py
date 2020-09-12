from django.db import models
from auto import utils

# Create your models here.
class Material(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    imagen      = models.CharField(max_length=500)
    ranking     = models.PositiveIntegerField()
    precio      = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def to_string(self):
        return str(self.nombre) + '-' + str(self.descripcion) + '-' + str(self.imagen) + '-' + str(self.ranking) + '-' + str(self.precio)

    def crearMaterial(self,nombre, descripcion, imagen, ranking, precio):
        material = Material()
        material.nombre = nombre
        material.descripcion = descripcion
        material.imagen = imagen
        material.ranking = ranking
        material.precio = precio
        material.save()
        return material

    def actualizarMaterial(self,id,nombre, descripcion, imagen, ranking, precio):
        materiales = Material.objects.filter(id=id)
        try:
            material = materiales[0]
            material.nombre = nombre
            material.descripcion = descripcion
            material.imagen = imagen
            material.ranking = ranking
            material.precio = precio
            material.save()
            return material
        except Exception as e:
            return None

    def eliminarMaterial(self,id):
        materiales = Material.objects.filter(id=id)
        try:
            material = materiales[0]
            material.delete()
            return utils.message_1("Material",id)
        except Exception as e:
            return ""
