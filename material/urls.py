from django.urls import path
from .views import *


urlpatterns = [
	path('material/', getMaterial),
	path('material/<int:pk>', getOneMaterial)
]
