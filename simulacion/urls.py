from django.urls import path
from .views import *


urlpatterns = [
	path('simulacion/', getSimulacion),
	path('simulacion/<int:id>', getSimulacionesids),
	path('simulacion/usuario/<int:id>', getSimulaciones)
]
