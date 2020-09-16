from django.urls import path
from .views import *


urlpatterns = [
	path('usuario/', getUsuario),
	path('user/<int:pk>',getOneUsuario2),
]
