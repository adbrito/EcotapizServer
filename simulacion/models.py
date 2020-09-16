from django.db import models
from auto.models import Auto
from diseno.models import Diseno
from cotizacion.models import Cotizacion
from material.models import Material
from usuario.models import Usuario
from auto import utils

# Create your models here.
class Simulacion(models.Model):
    id            = models.AutoField(primary_key=True)
    idAuto        = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    idDiseno      = models.ForeignKey(Diseno, on_delete=models.SET_NULL, null=True)
    idCotizacion  = models.ForeignKey(Cotizacion, on_delete=models.SET_NULL, null=True)
    idUsuario     = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, default=1)
    fecha         = models.DateField(auto_now=True)
    idMaterial    = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

    def to_string(self):
        return str(self.idAuto) + " - " + str(self.idDiseno) + " - " + str(self.idCotizacion) + " - " + str(self.idUsuario) + " - " + str(self.fecha) + " - " + str(self.idMaterial)

    def crearSimulacion(self, idAuto, idDiseno, idCotizacion, idUsuario, fecha, idMaterial):
        simulacion = Simulacion()
        simulacion.idAuto = Auto.objects.get(id=idAuto)
        simulacion.idDiseno = Diseno.objects.get(id=idDiseno)
        simulacion.idCotizacion = Cotizacion.objects.get(id=idCotizacion)
        simulacion.idUsuario = Usuario.objects.get(id=idUsuario)
        simulacion.fecha = fecha
        simulacion.idMaterial = Material.objects.get(id=idMaterial)
        simulacion.save()
        return simulacion

    def actualizarSimulacion(self, id, idAuto, idDiseno, idCotizacion, idUsuario, fecha, idMaterial):
        simulaciones = Simulacion.objects.filter(id=id)
        try:
            simulacion = simulaciones[0]
            simulacion.idAuto = Auto.objects.get(id=idAuto)
            simulacion.idDiseno = Diseno.objects.get(id=idDiseno)
            simulacion.idCotizacion = Cotizacion.objects.get(id=idCotizacion)
            simulacion.idUsuario = Usuario.objects.get(id=idUsuario)
            simulacion.fecha = fecha
            simulacion.idMaterial = Material.objects.get(id=idMaterial)
            simulacion.save()
            return simulacion
        except Exception as e:
            return None

    def eliminarSimulacion(self, id):
        simulaciones = Simulacion.objects.filter(id=id)
        try:
            simulacion = simulaciones[0]
            cotizaciones = Cotizacion.eliminarCotizacion(id=simulacion.idCotizacion.id)
            simulacion.delete()
            return utils.message_1("Simulacion",id)
        except Exception as e:
            print ("error: ",e)
            return e
