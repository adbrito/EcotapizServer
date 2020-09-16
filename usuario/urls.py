from django.urls import path
from .views import *


urlpatterns = [
	path('usuario/', getUsuario),
	path('usuario/<int:pk>',getOneUsuario),
]
