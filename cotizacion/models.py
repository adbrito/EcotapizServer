from django.db import models
from auto import utils

# Create your models here.
class Cotizacion(models.Model):
    id        = models.AutoField(primary_key=True)
    subtotal  = models.DecimalField(max_digits=10, decimal_places=2)
    total     = models.DecimalField(max_digits=10, decimal_places=2)
    iva       = models.DecimalField(max_digits=10, decimal_places=2)

    def to_string(self):
        return str(self.subtotal) + '-' + str(self.total) + '-' + str(self.iva)

    def crearCotizacion(self,subtotal,total,iva):
        cotizacion = Cotizacion()
        cotizacion.subtotal = subtotal
        cotizacion.total = total
        cotizacion.iva = iva
        cotizacion.save()
        return cotizacion

    def actualizarCotizacion(self, id, subtotal, total, iva):
        cotizaciones = Cotizacion.objects.filter(id=id)
        try:
            cotizacion = cotizaciones[0]
            cotizacion.subtotal = subtotal
            cotizacion.total = total
            cotizacion.iva = iva
            cotizacion.save()
            return cotizacion
        except Exception as e:
            return None

    def eliminarCotizacion(id):
        cotizaciones = Cotizacion.objects.filter(id=id)
        try:
            cotizacion = cotizaciones[0]
            cotizacion.delete()
            return utils.message_1("Cotizacion",id)
        except Exception as e:
            return ""