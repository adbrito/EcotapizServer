from django.db import models
from auto import utils

# Create your models here.
class Usuario(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=30)
    apellido    = models.CharField(max_length=30)
    correo      = models.CharField(max_length=30)
    contrasena  = models.CharField(max_length=500)

    def to_string(self):
        return str(self.nombre) + '-' + str(self.apellido) + '-' + str(self.correo) + '-' + str(self.contrasena)

    def crearUsuario(self,nombre, apellido, correo, contrasena):
        usuario = Usuario()
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.correo = correo
        usuario.contrasena = contrasena
        usuario.save()
        return usuario

    def actualizarUsuario(self,id,nombre, apellido, correo, contrasena):
        usuarios = Usuario.objects.filter(id=id)
        try:
            usuario = usuarios[0]
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo = correo
            usuario.contrasena = contrasena
            usuario.save()
            return usuario
        except Exception as e:
            return None

    def eliminarUsuario(self,id):
        usuarios = Usuario.objects.filter(id=id)
        try:
            usuario = usuarios[0]
            usuario.delete()
            return utils.message_1("Usuario",id)
        except Exception as e:
            return ""
 
