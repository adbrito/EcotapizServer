from django.urls import path
from .views import *


urlpatterns = [
	path('simulacion/', getSimulacion),
	path('simulacion/<int:id>', getSimulaciones),
	path('simulacion/usuario/<int:id>', getSimulaciones)
]
