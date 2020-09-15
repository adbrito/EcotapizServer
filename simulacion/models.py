from django.db import models
from auto.models import Auto
from diseno.models import Diseno
from cotizacion.models import Cotizacion
from material.models import Material
from usuario.models import Usuario

# Create your models here.
class Simulacion(models.Model):
    idAuto        = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    idDiseno      = models.ForeignKey(Diseno, on_delete=models.SET_NULL, null=True)
    idCotizacion  = models.ForeignKey(Cotizacion, on_delete=models.SET_NULL, null=True)
    idUsuario     = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, default=1)
    fecha         = models.DateField(auto_now=True)
    idMaterial    = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
